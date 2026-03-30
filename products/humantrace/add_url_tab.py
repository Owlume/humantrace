# add_url_tab.py
# Run this from owlume-engine root:
#   python add_url_tab.py
# Adds the URL/Link tab to humantrace_interface.html

import os

path = os.path.join("assets", "humantrace_interface.html")

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Check if already added
if "Link / URL" in content or "panelUrl" in content:
    print("URL tab already present. Nothing to do.")
    exit()

# Add URL tab button
old1 = """      <button class="method-tab" id="tabImage" onclick="switchMethod('image')">
        ⊞ Screenshot
      </button>
    </div>"""

new1 = """      <button class="method-tab" id="tabImage" onclick="switchMethod('image')">
        ⊞ Screenshot
      </button>
      <button class="method-tab" id="tabUrl" onclick="switchMethod('url')">
        ⛓ Link / URL
      </button>
    </div>"""

content = content.replace(old1, new1)
print("Tab button:", "✅" if "tabUrl" in content else "❌")

# Add URL input panel before input-footer
old2 = """    <div class="input-footer">
      <select class="context-select" id="contextSelect">"""

new2 = """    <!-- URL input panel -->
    <div class="method-panel" id="panelUrl">
      <label class="input-label">Paste a suspicious link or email address</label>
      <input
        type="text"
        id="urlInput"
        placeholder="https://suspicious-link.com or user@domain.com"
        style="width:100%;background:transparent;border:none;border-bottom:1px solid var(--border-hi);
               outline:none;color:var(--text);font-family:'DM Sans',sans-serif;font-size:14px;
               padding:10px 0;margin-bottom:16px;transition:border-color 0.2s;"
        onfocus="this.style.borderColor='var(--accent)'"
        onblur="this.style.borderColor='var(--border-hi)'"
      >
      <div style="font-size:12px;color:var(--text-dim);font-family:'DM Mono',monospace;line-height:1.6;">
        HumanTrace will analyse the domain for known fraud patterns.
        No need to paste the full message — just the link.
      </div>
    </div>

    <div class="input-footer">
      <select class="context-select" id="contextSelect">"""

content = content.replace(old2, new2)
print("URL panel:", "✅" if "panelUrl" in content else "❌")

# Update switchMethod to include URL tab
old3 = """function switchMethod(method) {
  _activeMethod = method;
  document.getElementById('tabText').classList.toggle('active', method === 'text');
  document.getElementById('tabImage').classList.toggle('active', method === 'image');
  document.getElementById('panelText').classList.toggle('active', method === 'text');
  document.getElementById('panelImage').classList.toggle('active', method === 'image');
}"""

new3 = """function switchMethod(method) {
  _activeMethod = method;
  document.getElementById('tabText').classList.toggle('active', method === 'text');
  document.getElementById('tabImage').classList.toggle('active', method === 'image');
  document.getElementById('tabUrl').classList.toggle('active', method === 'url');
  document.getElementById('panelText').classList.toggle('active', method === 'text');
  document.getElementById('panelImage').classList.toggle('active', method === 'image');
  document.getElementById('panelUrl').classList.toggle('active', method === 'url');
  document.getElementById('contextSelect').style.display = method === 'url' ? 'none' : '';
}"""

content = content.replace(old3, new3)
print("switchMethod:", "✅" if "panelUrl" in content else "❌")

# Add URL scan path to runScan
old4 = """  // Image scan path
  if (_activeMethod === 'image') {"""

new4 = """  // URL scan path
  if (_activeMethod === 'url') {
    const urlInput = document.getElementById('urlInput').value.trim();
    if (!urlInput) {
      alert('Please paste a URL or domain first.');
      return;
    }
    btn.disabled = true;
    btn.classList.add('loading');
    fetch('/scan-url', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url: urlInput })
    })
    .then(r => r.json())
    .then(result => {
      renderResults(result);
      btn.disabled = false;
      btn.classList.remove('loading');
    })
    .catch(err => {
      console.error('URL scan error:', err);
      alert('URL scan failed. Is the server running?');
      btn.disabled = false;
      btn.classList.remove('loading');
    });
    return;
  }

  // Image scan path
  if (_activeMethod === 'image') {"""

content = content.replace(old4, new4)
print("runScan URL:", "✅" if "scan-url" in content else "❌")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\nDone. File size: {os.path.getsize(path)} bytes")
print("Refresh http://localhost:8000 to see the URL tab.")
