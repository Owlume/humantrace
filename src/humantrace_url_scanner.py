# src/humantrace_url_scanner.py
# HumanTrace — URL / Domain Scanner
# Powered by Owlume
#
# Purpose:
#   Analyse a suspicious URL or email address for fraud signals.
#   Lightweight alternative to full message scan when user has a link.
#
# What it analyses:
#   - Domain reputation patterns
#   - Typosquatting against known legitimate domains
#   - Suspicious TLD patterns
#   - URL structure anomalies
#   - Subdomain abuse
#   - IP address as host (never legitimate)
#   - Suspicious keywords in domain/path
#
# Governance:
#   Output kind: SIGNAL — not ACTION, ADVICE, or INSTRUCTIONS.
#   Never accuses. Surfaces reasoning signals only.
#   Human makes the final judgment.

from __future__ import annotations

import re
import json
import os
import uuid
import datetime as dt
from typing import Dict, List, Optional, Any, Tuple
from urllib.parse import urlparse


# ── Paths ─────────────────────────────────────────────────────────────────────

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATTERNS_PATH = os.path.join(ROOT, "data", "fraud_domain_patterns.json")


# ── Load patterns ─────────────────────────────────────────────────────────────

def _load_patterns() -> Dict[str, Any]:
    try:
        with open(PATTERNS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


# ── URL/Email extraction ──────────────────────────────────────────────────────

URL_PATTERN = re.compile(
    r'https?://[^\s<>"{}|\\^`\[\]]+',
    re.IGNORECASE
)

EMAIL_PATTERN = re.compile(
    r'\b[A-Za-z0-9._%+\-]+@([A-Za-z0-9.\-]+\.[A-Z|a-z]{2,})\b'
)

BARE_DOMAIN_PATTERN = re.compile(
    r'\b([a-zA-Z0-9][a-zA-Z0-9\-]{1,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?)\b'
)

IP_PATTERN = re.compile(
    r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b'
)


def extract_urls_and_domains(text: str) -> Dict[str, List[str]]:
    """Extract all URLs, email addresses and bare domains from text."""
    text = text or ""
    urls = URL_PATTERN.findall(text)
    emails = EMAIL_PATTERN.findall(text)  # returns domain groups
    ips = IP_PATTERN.findall(text)
    return {
        "urls": list(set(urls)),
        "email_domains": list(set(emails)),
        "ip_addresses": list(set(ips)),
    }


def parse_domain(url_or_domain: str) -> Optional[str]:
    """Extract the registrable domain from a URL or domain string."""
    s = url_or_domain.strip()
    if not s:
        return None

    # Add scheme if missing for urlparse
    if not s.startswith(("http://", "https://")):
        s = "http://" + s

    try:
        parsed = urlparse(s)
        host = parsed.hostname or ""
        return host.lower() if host else None
    except Exception:
        return None


# ── Detection layers ──────────────────────────────────────────────────────────

def _check_ip_as_host(domain: str) -> Optional[str]:
    """Legitimate services never use raw IP addresses as their domain."""
    if IP_PATTERN.fullmatch(domain.strip()):
        return f"IP address used as host ({domain}) — legitimate services always use domain names"
    return None


def _check_suspicious_tld(domain: str, patterns: Dict) -> Optional[str]:
    """Free/abused TLDs are disproportionately used for fraud."""
    tlds = patterns.get("suspicious_tld_patterns", [])
    for tld in tlds:
        if domain.endswith(tld):
            return f"Suspicious TLD '{tld}' — heavily associated with fraud infrastructure"
    return None


def _check_typosquatting(domain: str, patterns: Dict) -> Optional[str]:
    """Check for common typosquatting patterns against legitimate brands."""
    targets = patterns.get("known_fraud_indicators", {}).get("typosquatting_targets", [])
    domain_lower = domain.lower()
    for target in targets:
        if target.lower() in domain_lower:
            return f"Typosquatting pattern detected: '{target}' in domain '{domain}'"

    # Check edit distance against legitimate Australian domains
    legit = patterns.get("legitimate_Australian_domains", [])
    for legit_domain in legit:
        legit_base = legit_domain.split(".")[0].lower()
        domain_base = domain.split(".")[0].lower()
        # Simple check: same length ±1, mostly same chars
        if abs(len(legit_base) - len(domain_base)) <= 1 and len(legit_base) >= 4:
            # Count matching characters
            matches = sum(1 for a, b in zip(legit_base, domain_base) if a == b)
            similarity = matches / max(len(legit_base), len(domain_base))
            if 0.70 <= similarity < 1.0:  # Similar but not identical
                if domain != legit_domain:
                    return f"Possible typosquatting of '{legit_domain}' — domain '{domain}' is suspiciously similar"
    return None


def _check_suspicious_keywords(domain: str, path: str, patterns: Dict) -> List[str]:
    """Check for fraud-indicative keywords in domain and path."""
    findings = []
    suspicious = patterns.get("suspicious_domain_patterns", [])
    full_url = (domain + "/" + path).lower()

    for pattern in suspicious:
        if re.search(pattern, full_url, re.IGNORECASE):
            readable = pattern.replace(".*", " ").replace("[0-9]", "#")
            findings.append(f"Suspicious keyword pattern: '{readable}'")

    return findings


def _check_subdomain_abuse(domain: str, patterns: Dict) -> Optional[str]:
    """Excessive subdomains are used to make fake URLs look legitimate."""
    max_subdomains = patterns.get("known_fraud_indicators", {}).get("excessive_subdomains", 3)
    parts = domain.split(".")
    subdomains = len(parts) - 2  # subtract domain + TLD
    if subdomains >= max_subdomains:
        return f"Excessive subdomains ({subdomains}) — used to disguise fraudulent domains as legitimate"
    return None


def _check_legitimate(domain: str, patterns: Dict) -> bool:
    """Check if domain is a known legitimate Australian domain."""
    legit = patterns.get("legitimate_Australian_domains", [])
    return domain.lower() in [d.lower() for d in legit]


def _check_suspicious_port(url: str, patterns: Dict) -> Optional[str]:
    """Legitimate sites don't use non-standard ports."""
    ports = patterns.get("known_fraud_indicators", {}).get("suspicious_port", [])
    for port in ports:
        if f":{port}" in url:
            return f"Non-standard port :{port} — legitimate services use standard ports 80/443"
    return None


# ── Main URL scan ─────────────────────────────────────────────────────────────

def scan_url(url_or_domain: str) -> Dict[str, Any]:
    """
    Scan a URL, domain, or email address for fraud signals.

    Returns a result dict compatible with HumanTrace ScanResult structure.
    """
    url_or_domain = (url_or_domain or "").strip()
    if not url_or_domain:
        return _empty_result(url_or_domain)

    patterns = _load_patterns()

    # Parse domain
    domain = parse_domain(url_or_domain)
    if not domain:
        return _empty_result(url_or_domain)

    # Extract path for keyword checking
    try:
        parsed = urlparse(
            url_or_domain if url_or_domain.startswith("http")
            else "http://" + url_or_domain
        )
        path = parsed.path + "?" + parsed.query if parsed.query else parsed.path
    except Exception:
        path = ""

    findings = []
    synthetic_score = 0.0
    human_score = 0.0

    # Check if known legitimate
    if _check_legitimate(domain, patterns):
        human_score += 0.60
        findings.append(f"Domain '{domain}' is a known legitimate Australian service")

    # Layer 1: IP as host
    ip_finding = _check_ip_as_host(domain)
    if ip_finding:
        synthetic_score += 0.40
        findings.append(ip_finding)

    # Layer 2: Suspicious TLD
    tld_finding = _check_suspicious_tld(domain, patterns)
    if tld_finding:
        synthetic_score += 0.25
        findings.append(tld_finding)

    # Layer 3: Typosquatting
    typo_finding = _check_typosquatting(domain, patterns)
    if typo_finding:
        synthetic_score += 0.35
        findings.append(typo_finding)

    # Layer 4: Suspicious keywords
    keyword_findings = _check_suspicious_keywords(domain, path, patterns)
    if keyword_findings:
        synthetic_score += 0.15 * len(keyword_findings)
        findings.extend(keyword_findings[:3])

    # Layer 5: Subdomain abuse
    subdomain_finding = _check_subdomain_abuse(domain, patterns)
    if subdomain_finding:
        synthetic_score += 0.20
        findings.append(subdomain_finding)

    # Layer 6: Suspicious port
    port_finding = _check_suspicious_port(url_or_domain, patterns)
    if port_finding:
        synthetic_score += 0.25
        findings.append(port_finding)

    # No findings
    if not findings:
        findings.append(f"No known fraud patterns detected for domain '{domain}'")
        findings.append("This does not confirm the URL is safe — verify independently")

    # Determine signal
    net_score = synthetic_score - human_score
    if net_score >= 0.35:
        signal = "red"
        confidence = min(0.55 + net_score, 0.95)
    elif net_score >= 0.15:
        signal = "yellow"
        confidence = 0.55 + net_score * 0.5
    elif human_score >= 0.60:
        signal = "green"
        confidence = 0.70
    else:
        signal = "yellow"
        confidence = 0.50

    # Plain English
    plain_english = _plain_english(signal, confidence, domain, findings)
    recommended_action = _recommended_action(signal, domain)
    analyst_questions = _analyst_questions(signal, domain, findings)

    return {
        "scan_id": str(uuid.uuid4()),
        "timestamp": dt.datetime.utcnow().isoformat() + "Z",
        "signal": signal,
        "confidence": round(confidence, 3),
        "first_contact": True,
        "fraud_category": "phishing" if synthetic_score >= 0.35 else None,
        "plain_english": plain_english,
        "recommended_action": recommended_action,
        "analyst_questions": analyst_questions,
        "layers": [
            {
                "layer": "domain_reputation",
                "signal": signal,
                "confidence": round(confidence, 3),
                "findings": findings,
            }
        ],
        "meta": {
            "input_method": "url",
            "scanned_domain": domain,
            "original_input": url_or_domain,
            "synthetic_score": round(synthetic_score, 3),
            "human_score": round(human_score, 3),
            "governance": {
                "output_kind": "SIGNAL",
                "stage14_applies": False,
                "interpretation": "narrow",
            }
        }
    }


def _plain_english(signal: str, confidence: float, domain: str, findings: List[str]) -> str:
    pct = int(confidence * 100)
    if signal == "red":
        return (
            f"This domain '{domain}' shows multiple fraud indicators ({pct}% confidence). "
            f"Do not click this link or provide any information. "
            f"Verify through an official channel independently."
        )
    if signal == "green":
        return (
            f"Domain '{domain}' appears to be a known legitimate service ({pct}% confidence). "
            f"Standard caution still applies — confirm the full URL matches exactly."
        )
    return (
        f"Domain '{domain}' shows some unusual patterns ({pct}% confidence) "
        f"but no definitive fraud indicators. Verify independently before clicking or responding."
    )


def _recommended_action(signal: str, domain: str) -> str:
    if signal == "red":
        return (
            f"Do not click this link or visit '{domain}'. "
            f"If you need to contact this organisation, find their official website independently."
        )
    if signal == "green":
        return (
            f"Domain appears legitimate. Confirm the full URL exactly matches "
            f"the official address before entering any personal information."
        )
    return (
        f"Before clicking: search for '{domain}' independently to verify it is legitimate. "
        f"Do not use any contact details provided in the message containing this link."
    )


def _analyst_questions(signal: str, domain: str, findings: List[str]) -> List[str]:
    questions = [
        f"Did you receive this link from someone who contacted you — or did you find it yourself?"
    ]
    if signal == "red":
        questions.append(
            f"Can you find '{domain.split('.')[0]}' by searching independently — "
            f"without using any link provided in the message?"
        )
        questions.append(
            "Is there any reason a legitimate organisation would send you this link "
            "rather than asking you to visit their official website directly?"
        )
    else:
        questions.append(
            "Does the full URL exactly match what you would expect — "
            "including every character in the domain name?"
        )
        questions.append(
            "Was this link sent to you unsolicited, or did you request it?"
        )
    return questions[:4]


def _empty_result(input_text: str) -> Dict[str, Any]:
    return {
        "scan_id": str(uuid.uuid4()),
        "timestamp": dt.datetime.utcnow().isoformat() + "Z",
        "signal": "yellow",
        "confidence": 0.0,
        "first_contact": True,
        "fraud_category": None,
        "plain_english": "Could not parse a valid domain from the provided input.",
        "recommended_action": "Please provide a complete URL or domain name.",
        "analyst_questions": [],
        "layers": [],
        "meta": {"input_method": "url", "error": "invalid_input"}
    }
