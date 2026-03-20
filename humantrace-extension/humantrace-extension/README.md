# HumanTrace Browser Extension
## Installation Guide

### What this extension does

- **Right-click any text** on any webpage → "Scan with HumanTrace"
- **Right-click any link** → "Check this link with HumanTrace"  
- **Click the toolbar icon** → Paste and scan any message instantly
- Results appear as an overlay on the page — no tab switching needed

### Requirements

HumanTrace must be running on your ThinkPad:
```
python -m uvicorn humantrace_api:app --reload --host 0.0.0.0 --port 8000
```

### Installation in Edge or Chrome

1. Open Edge and go to: `edge://extensions`  
   (or Chrome: `chrome://extensions`)

2. Turn on **Developer mode** — toggle in the top right corner

3. Click **"Load unpacked"**

4. Select the `humantrace-extension` folder

5. The HumanTrace extension appears in your toolbar

### Usage

**Method 1 — Right-click on selected text:**
1. Select any suspicious text on a webpage
2. Right-click → "🔍 Scan with HumanTrace"
3. Result appears as overlay on the page

**Method 2 — Right-click on a link:**
1. Right-click any suspicious link
2. Click "🔗 Check this link with HumanTrace"
3. Domain reputation result appears on page

**Method 3 — Toolbar popup:**
1. Click the HumanTrace icon in your browser toolbar
2. Paste any message or URL
3. Click Scan
4. Result appears in the popup

### Settings

Click the ⚙ gear icon in the popup to change the server URL.

Default: `http://localhost:8000`

When HumanTrace is deployed to cloud, update this to `https://humantrace.au`
