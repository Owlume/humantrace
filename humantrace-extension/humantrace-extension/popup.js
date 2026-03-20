// popup.js
// HumanTrace Extension — Popup Logic

let serverUrl = 'http://localhost:8000';

// ── Init ──────────────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', async () => {
  // Load settings
  const resp = await chrome.runtime.sendMessage({ type: 'get-settings' });
  if (resp && resp.settings) {
    serverUrl = resp.settings.serverUrl || serverUrl;
    document.getElementById('serverUrlInput').value = serverUrl;
  }

  // Check server status
  checkServer();

  // Load last result if available
  const lastResp = await chrome.runtime.sendMessage({ type: 'get-last-result' });
  if (lastResp && lastResp.result) {
    showResult(lastResp.result.result);
  }

  // Check if there is selected text from the page to pre-fill
  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (tab) {
      chrome.tabs.sendMessage(tab.id, { type: 'get-selection' }, (response) => {
        if (chrome.runtime.lastError) return;
        if (response && response.text && response.text.length > 5) {
          document.getElementById('msgInput').value = response.text;
        }
      });
    }
  } catch (e) {}

  // Wire up buttons
  document.getElementById('scanBtn').addEventListener('click', runScan);
  document.getElementById('settingsToggle').addEventListener('click', toggleSettings);
  document.getElementById('saveSettingsBtn').addEventListener('click', saveSettings);
  document.getElementById('openFullBtn').addEventListener('click', openFull);

  // Ctrl+Enter to scan
  document.getElementById('msgInput').addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') runScan();
  });
});

// ── Server check ──────────────────────────────────────────────────────────────

async function checkServer() {
  const dot = document.getElementById('statusDot');
  const text = document.getElementById('statusText');

  const resp = await chrome.runtime.sendMessage({ type: 'check-server' });
  if (resp && resp.online) {
    dot.className = 'status-dot online';
    text.textContent = `Connected · ${serverUrl.replace('http://', '')}`;
  } else {
    dot.className = 'status-dot offline';
    text.textContent = 'Server offline — start HumanTrace first';
  }
}

// ── Scan ──────────────────────────────────────────────────────────────────────

async function runScan() {
  const text = document.getElementById('msgInput').value.trim();
  if (!text) return;

  const contextHint = document.getElementById('contextSelect').value || null;
  const btn = document.getElementById('scanBtn');
  btn.disabled = true;
  btn.textContent = '...';

  showLoading();

  // Detect if input looks like a URL
  const isUrl = /^https?:\/\//i.test(text) || /^[a-zA-Z0-9][a-zA-Z0-9\-.]+\.[a-zA-Z]{2,}/.test(text);

  const msgType = isUrl ? 'scan-url' : 'scan-text';
  const payload = isUrl
    ? { type: msgType, url: text }
    : { type: msgType, text, contextHint };

  const resp = await chrome.runtime.sendMessage(payload);

  btn.disabled = false;
  btn.textContent = 'Scan';

  if (resp && resp.success) {
    showResult(resp.result);
  } else {
    showError(resp ? resp.error : 'Scan failed. Is HumanTrace running?');
  }
}

// ── Display ───────────────────────────────────────────────────────────────────

function showLoading() {
  const section = document.getElementById('resultSection');
  const loading = document.getElementById('loadingIndicator');
  const card = document.getElementById('resultCard');
  section.style.display = 'block';
  loading.style.display = 'flex';
  card.style.display = 'none';
}

function showResult(result) {
  const section = document.getElementById('resultSection');
  const loading = document.getElementById('loadingIndicator');
  const card = document.getElementById('resultCard');

  section.style.display = 'block';
  loading.style.display = 'none';
  card.style.display = 'block';

  const signal = result.signal || 'yellow';
  const confidence = Math.round((result.confidence || 0.5) * 100);

  card.className = `result-card ${signal}`;

  const icons = { red: '⚠', yellow: '◐', green: '✓' };
  const labels = {
    red: 'Low Human Presence',
    yellow: 'Signal Unclear',
    green: 'Human Present'
  };

  document.getElementById('resultIcon').textContent = icons[signal] || '◐';
  document.getElementById('resultLabel').textContent = labels[signal] || 'Unknown';
  document.getElementById('resultConf').textContent = `${confidence}%`;

  const plainEnglish = result.plain_english || result.plainEnglish || '';
  document.getElementById('resultText').textContent = plainEnglish;

  const action = result.recommended_action || result.recommendedAction || '';
  document.getElementById('resultAction').textContent = action;
}

function showError(message) {
  const section = document.getElementById('resultSection');
  const loading = document.getElementById('loadingIndicator');
  const card = document.getElementById('resultCard');

  section.style.display = 'block';
  loading.style.display = 'none';
  card.style.display = 'block';
  card.className = 'result-card yellow';

  document.getElementById('resultIcon').textContent = '⚠';
  document.getElementById('resultLabel').textContent = 'Error';
  document.getElementById('resultConf').textContent = '';
  document.getElementById('resultText').textContent = message || 'Scan failed.';
  document.getElementById('resultAction').textContent =
    'Make sure HumanTrace is running at ' + serverUrl;
}

// ── Settings ──────────────────────────────────────────────────────────────────

function toggleSettings() {
  const panel = document.getElementById('settingsPanel');
  panel.classList.toggle('visible');
}

async function saveSettings() {
  const newUrl = document.getElementById('serverUrlInput').value.trim();
  if (!newUrl) return;

  serverUrl = newUrl;
  await chrome.runtime.sendMessage({
    type: 'save-settings',
    settings: { serverUrl: newUrl }
  });

  document.getElementById('settingsPanel').classList.remove('visible');
  checkServer();
}

// ── Open full HumanTrace ──────────────────────────────────────────────────────

function openFull() {
  chrome.tabs.create({ url: serverUrl });
}
