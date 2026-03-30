// background.js
// HumanTrace Browser Extension — Background Service Worker
// Powered by Owlume
//
// Handles:
// - Context menu registration
// - Scan requests from context menu and popup
// - Communication with HumanTrace server
// - Result storage for popup display

// ── Default settings ──────────────────────────────────────────────────────────

const DEFAULT_SETTINGS = {
  serverUrl: 'http://localhost:8000',
  lastScanResult: null,
  lastScanTime: null,
};

// ── Initialise ────────────────────────────────────────────────────────────────

chrome.runtime.onInstalled.addListener(() => {
  // Set default settings
  chrome.storage.local.get('settings', (data) => {
    if (!data.settings) {
      chrome.storage.local.set({ settings: DEFAULT_SETTINGS });
    }
  });

  // Register context menu
  chrome.contextMenus.create({
    id: 'humantrace-scan-text',
    title: '🔍 Scan with HumanTrace',
    contexts: ['selection'],
  });

  chrome.contextMenus.create({
    id: 'humantrace-scan-link',
    title: '🔗 Check this link with HumanTrace',
    contexts: ['link'],
  });
});

// ── Context menu handler ──────────────────────────────────────────────────────

chrome.contextMenus.onClicked.addListener(async (info, tab) => {
  const settings = await getSettings();
  const serverUrl = settings.serverUrl || DEFAULT_SETTINGS.serverUrl;

  if (info.menuItemId === 'humantrace-scan-text') {
    const text = info.selectionText || '';
    if (!text.trim()) return;

    // Show scanning notification in page
    await notifyTab(tab.id, { type: 'scanning', text: text.substring(0, 50) + '...' });

    try {
      const result = await scanText(serverUrl, text);
      await storeResult(result, text, 'text');
      await notifyTab(tab.id, { type: 'result', result });
    } catch (err) {
      await notifyTab(tab.id, { type: 'error', message: err.message });
    }
  }

  if (info.menuItemId === 'humantrace-scan-link') {
    const url = info.linkUrl || info.srcUrl || '';
    if (!url.trim()) return;

    await notifyTab(tab.id, { type: 'scanning', text: url.substring(0, 50) + '...' });

    try {
      const result = await scanUrl(serverUrl, url);
      await storeResult(result, url, 'url');
      await notifyTab(tab.id, { type: 'result', result });
    } catch (err) {
      await notifyTab(tab.id, { type: 'error', message: err.message });
    }
  }
});

// ── Message handler (from popup and content script) ───────────────────────────

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  handleMessage(message, sender, sendResponse);
  return true; // Keep channel open for async response
});

async function handleMessage(message, sender, sendResponse) {
  const settings = await getSettings();
  const serverUrl = settings.serverUrl || DEFAULT_SETTINGS.serverUrl;

  if (message.type === 'scan-text') {
    try {
      const result = await scanText(serverUrl, message.text, message.contextHint);
      await storeResult(result, message.text, 'text');
      sendResponse({ success: true, result });
    } catch (err) {
      sendResponse({ success: false, error: err.message });
    }
    return;
  }

  if (message.type === 'scan-url') {
    try {
      const result = await scanUrl(serverUrl, message.url);
      await storeResult(result, message.url, 'url');
      sendResponse({ success: true, result });
    } catch (err) {
      sendResponse({ success: false, error: err.message });
    }
    return;
  }

  if (message.type === 'get-last-result') {
    const data = await chrome.storage.local.get('lastResult');
    sendResponse({ result: data.lastResult || null });
    return;
  }

  if (message.type === 'save-settings') {
    await chrome.storage.local.set({ settings: message.settings });
    sendResponse({ success: true });
    return;
  }

  if (message.type === 'get-settings') {
    sendResponse({ settings });
    return;
  }

  if (message.type === 'check-server') {
    try {
      const resp = await fetch(`${serverUrl}/health`, { method: 'GET' });
      const data = await resp.json();
      sendResponse({ online: true, data });
    } catch (err) {
      sendResponse({ online: false, error: err.message });
    }
    return;
  }
}

// ── Scan functions ────────────────────────────────────────────────────────────

async function scanText(serverUrl, text, contextHint = null) {
  const resp = await fetch(`${serverUrl}/scan`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: text, context_hint: contextHint }),
  });
  if (!resp.ok) throw new Error(`Server error: ${resp.status}`);
  return await resp.json();
}

async function scanUrl(serverUrl, url) {
  const resp = await fetch(`${serverUrl}/scan-url`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ url }),
  });
  if (!resp.ok) throw new Error(`Server error: ${resp.status}`);
  return await resp.json();
}

// ── Storage helpers ───────────────────────────────────────────────────────────

async function getSettings() {
  const data = await chrome.storage.local.get('settings');
  return data.settings || DEFAULT_SETTINGS;
}

async function storeResult(result, input, inputType) {
  await chrome.storage.local.set({
    lastResult: {
      result,
      input: input.substring(0, 100),
      inputType,
      timestamp: new Date().toISOString(),
    }
  });
  // Update extension badge
  updateBadge(result.signal);
}

function updateBadge(signal) {
  const colors = {
    red: '#ff4458',
    yellow: '#f0b429',
    green: '#2ecc71',
  };
  const labels = { red: '⚠', yellow: '?', green: '✓' };
  chrome.action.setBadgeText({ text: labels[signal] || '?' });
  chrome.action.setBadgeBackgroundColor({ color: colors[signal] || '#6c757d' });
}

// ── Tab notification ──────────────────────────────────────────────────────────

async function notifyTab(tabId, message) {
  try {
    await chrome.tabs.sendMessage(tabId, message);
  } catch (err) {
    // Tab may not have content script — open popup instead
    chrome.action.openPopup();
  }
}
