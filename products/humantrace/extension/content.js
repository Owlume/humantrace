// content.js
// HumanTrace Extension — Content Script
// Runs on every page. Handles:
// - Selection text retrieval for popup pre-fill
// - Scan result overlay display on page

// ── Message listener ──────────────────────────────────────────────────────────

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === 'get-selection') {
    const selected = window.getSelection()?.toString()?.trim() || '';
    sendResponse({ text: selected });
    return true;
  }

  if (message.type === 'scanning') {
    showToast('🔍 Scanning with HumanTrace...', 'info');
    return true;
  }

  if (message.type === 'result') {
    showResultOverlay(message.result);
    return true;
  }

  if (message.type === 'error') {
    showToast('⚠ HumanTrace scan failed: ' + message.message, 'error');
    return true;
  }
});

// ── Toast notification ────────────────────────────────────────────────────────

function showToast(text, type = 'info') {
  const existing = document.getElementById('ht-toast');
  if (existing) existing.remove();

  const toast = document.createElement('div');
  toast.id = 'ht-toast';
  toast.style.cssText = `
    position: fixed;
    bottom: 24px;
    right: 24px;
    background: #111118;
    color: #e8e8f0;
    border: 1px solid ${type === 'error' ? '#ff4458' : '#2e2e42'};
    border-radius: 8px;
    padding: 10px 16px;
    font-family: 'DM Sans', -apple-system, sans-serif;
    font-size: 13px;
    z-index: 2147483647;
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    animation: htSlideIn 0.3s ease;
    max-width: 320px;
  `;
  toast.textContent = text;

  const style = document.createElement('style');
  style.textContent = `
    @keyframes htSlideIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
  `;
  document.head.appendChild(style);
  document.body.appendChild(toast);

  setTimeout(() => toast.remove(), 3000);
}

// ── Result overlay ────────────────────────────────────────────────────────────

function showResultOverlay(result) {
  const existing = document.getElementById('ht-overlay');
  if (existing) existing.remove();

  const signal = result.signal || 'yellow';
  const confidence = Math.round((result.confidence || 0.5) * 100);
  const plainEnglish = result.plain_english || result.plainEnglish || '';
  const action = result.recommended_action || result.recommendedAction || '';

  const colors = {
    red: { bg: '#3d1018', border: '#ff4458', label: '#ff4458', icon: '⚠' },
    yellow: { bg: '#2e2200', border: '#f0b429', label: '#f0b429', icon: '◐' },
    green: { bg: '#0a2e18', border: '#2ecc71', label: '#2ecc71', icon: '✓' },
  };
  const c = colors[signal] || colors.yellow;

  const labels = {
    red: 'LOW HUMAN PRESENCE',
    yellow: 'SIGNAL UNCLEAR',
    green: 'HUMAN PRESENT',
  };

  const overlay = document.createElement('div');
  overlay.id = 'ht-overlay';
  overlay.style.cssText = `
    position: fixed;
    bottom: 24px;
    right: 24px;
    width: 320px;
    background: ${c.bg};
    border: 1px solid ${c.border};
    border-radius: 12px;
    padding: 16px;
    font-family: 'DM Sans', -apple-system, sans-serif;
    font-size: 13px;
    color: #e8e8f0;
    z-index: 2147483647;
    box-shadow: 0 4px 24px rgba(0,0,0,0.5);
    animation: htSlideIn 0.3s ease;
  `;

  overlay.innerHTML = `
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;">
      <div style="display:flex;align-items:center;gap:8px;">
        <span style="font-size:18px;">${c.icon}</span>
        <div>
          <div style="font-family:monospace;font-size:9px;letter-spacing:0.1em;color:${c.label};">
            HUMANTRACE · ${labels[signal]}
          </div>
          <div style="font-size:13px;font-weight:500;">${confidence}% confidence</div>
        </div>
      </div>
      <button id="ht-close" style="background:transparent;border:none;color:#6e6e88;cursor:pointer;font-size:16px;padding:0 4px;">✕</button>
    </div>
    <div style="font-size:12px;color:#9e9eb8;line-height:1.5;margin-bottom:8px;font-style:italic;">
      ${plainEnglish}
    </div>
    ${action ? `<div style="font-size:11px;color:#6e6e88;line-height:1.4;padding-top:8px;border-top:1px solid rgba(255,255,255,0.06);">
      ${action}
    </div>` : ''}
  `;

  document.body.appendChild(overlay);

  document.getElementById('ht-close').addEventListener('click', () => overlay.remove());

  // Auto-dismiss after 8 seconds
  setTimeout(() => {
    if (document.getElementById('ht-overlay')) overlay.remove();
  }, 8000);
}
