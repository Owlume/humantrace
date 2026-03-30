# HumanTrace — Deployment Guide
## From localhost to humantrace.au on DigitalOcean
*Written for someone not fully confident on the Linux command line.*
*Every command is written out exactly. Copy and paste each one.*

---

## Overview of what we're doing

1. Create a DigitalOcean account and server
2. Point your domains (humantrace.au + humantrace.com.au) at the server
3. Connect to the server from your ThinkPad
4. Install the software the server needs
5. Copy your HumanTrace code onto the server
6. Start HumanTrace running
7. Set up Nginx (the web gateway) and HTTPS
8. Confirm everything works at https://humantrace.au

Estimated time: 1.5 to 2 hours, most of which is waiting for things to install.

---

## PART 1 — Create your DigitalOcean Droplet

### Step 1.1 — Sign up
Go to https://digitalocean.com and create an account.
Use a credit card. The $6/month Droplet will be all you need to start.

### Step 1.2 — Create a Droplet
Once logged in:
- Click **Create** → **Droplets**
- **Region**: Sydney (syd1)
- **OS**: Ubuntu 24.04 LTS
- **Size**: Basic → Regular → $6/month (1GB RAM / 1 CPU / 25GB SSD)
- **Authentication**: choose **Password** (simpler for now)
  - Set a strong root password and write it down
- **Hostname**: humantrace
- Click **Create Droplet**

Wait about 60 seconds. You'll see an IP address appear — something like `123.456.78.90`.
**Write this IP address down. You'll need it repeatedly.**

---

## PART 2 — Point your domains at the server

Do this in Crazy Domains (where you bought the domains).

### Step 2.1 — Log into Crazy Domains
Go to https://www.crazydomains.com.au and log in.

### Step 2.2 — Update DNS for humantrace.au
- Go to **My Domains** → click **humantrace.au** → **Manage**
- Find **DNS Settings** or **A Records**
- You need to set (or update) the **A record** for `@` (the root domain):
  - **Type**: A
  - **Name**: @ (or leave blank — means the root domain)
  - **Value**: your DigitalOcean IP address (e.g. 123.456.78.90)
  - **TTL**: 3600 (or whatever default is offered)
- Also add an A record for `www`:
  - **Type**: A
  - **Name**: www
  - **Value**: same IP address
- Save.

### Step 2.3 — Repeat for humantrace.com.au
Do the exact same thing for humantrace.com.au — same IP address, same A records.

### Step 2.4 — Wait for DNS to propagate
DNS changes take 15 minutes to 2 hours to take effect worldwide.
You can check progress at https://dnschecker.org — type in humantrace.au
and wait until it shows your IP address in green.

You can proceed with the server setup while waiting.

---

## PART 3 — Connect to your server from your ThinkPad

### Step 3.1 — Open PowerShell on your ThinkPad
Press **Windows key**, type **PowerShell**, press Enter.

### Step 3.2 — SSH into the server
Type this command, replacing the IP with your actual DigitalOcean IP:

```powershell
ssh root@123.456.78.90
```

It will ask: "Are you sure you want to continue connecting?" — type `yes` and press Enter.
Then it will ask for your password — type the root password you set in Step 1.2.

You are now inside your server. The prompt will change to something like:
```
root@humantrace:~#
```

Everything you type from here runs on the server, not your ThinkPad.

---

## PART 4 — Set up the server

Copy and paste each command block exactly. Press Enter after each one.
Wait for each command to finish before running the next.

### Step 4.1 — Update the server
```bash
apt update && apt upgrade -y
```
This may take 2–3 minutes.

### Step 4.2 — Install Python, pip, git, and nginx
```bash
apt install -y python3 python3-pip python3-venv git nginx certbot python3-certbot-nginx
```
This may take 2–3 minutes.

### Step 4.3 — Install Tesseract OCR (same as your ThinkPad)
```bash
apt install -y tesseract-ocr
```

### Step 4.4 — Create a non-root user to run HumanTrace
Running as root is a security risk. Create a dedicated user:
```bash
useradd -m -s /bin/bash humantrace
```

### Step 4.5 — Create the application directory
```bash
mkdir -p /var/www/humantrace
chown humantrace:humantrace /var/www/humantrace
```

---

## PART 5 — Copy your code to the server

You have two options. **Option A is easier if your code is on GitHub.**

### Option A — Clone from GitHub (recommended)
Still in your SSH session, run:

```bash
cd /var/www/humantrace
sudo -u humantrace git clone https://github.com/Owlume/owlume-engine.git .
```

If your GitHub repo is private, you'll need to authenticate.
The simplest way: create a GitHub Personal Access Token at
https://github.com/settings/tokens (classic token, repo scope),
then use it as the password when prompted.

### Option B — Copy files from your ThinkPad using SCP
Open a **second** PowerShell window on your ThinkPad (keep the SSH session open).
Run this from your ThinkPad, replacing the IP:

```powershell
scp -r C:\dev\owlume-engine\* root@123.456.78.90:/var/www/humantrace/
```

This copies everything. May take a minute or two.

---

## PART 6 — Install Python dependencies on the server

Back in your SSH session:

### Step 6.1 — Switch to the humantrace user
```bash
su - humantrace
cd /var/www/humantrace
```

### Step 6.2 — Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
Your prompt will now show `(.venv)` at the start.

### Step 6.3 — Install dependencies
```bash
pip install fastapi uvicorn python-docx pdfminer.six pytesseract pillow pdf2image
```

If you have a requirements.txt in your repo:
```bash
pip install -r requirements.txt
pip install fastapi uvicorn python-docx pdfminer.six pytesseract pillow pdf2image
```
(The second line ensures the new institutional dependencies are included
even if they're not in requirements.txt yet.)

### Step 6.4 — Test that the server starts
```bash
python -m uvicorn humantrace_api:app --host 0.0.0.0 --port 8000
```

You should see:
```
INFO:     Started server process
INFO:     Waiting for application startup.
[HumanTrace] Institutional dependencies: all present.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

Press **Ctrl+C** to stop it. We'll set it up to run permanently in the next step.

### Step 6.5 — Exit back to root
```bash
exit
```

---

## PART 7 — Set up systemd (keeps HumanTrace running permanently)

This makes HumanTrace start automatically when the server boots and
restart automatically if it ever crashes.

### Step 7.1 — Create the service file
```bash
nano /etc/systemd/system/humantrace.service
```

This opens a text editor. Copy and paste exactly this content:

```
[Unit]
Description=HumanTrace API
After=network.target

[Service]
Type=simple
User=humantrace
WorkingDirectory=/var/www/humantrace
Environment="PATH=/var/www/humantrace/.venv/bin"
ExecStart=/var/www/humantrace/.venv/bin/uvicorn humantrace_api:app --host 127.0.0.1 --port 8000
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

To save: press **Ctrl+X**, then **Y**, then **Enter**.

### Step 7.2 — Enable and start the service
```bash
systemctl daemon-reload
systemctl enable humantrace
systemctl start humantrace
```

### Step 7.3 — Check it's running
```bash
systemctl status humantrace
```

You should see `Active: active (running)` in green.
If you see an error, run `journalctl -u humantrace -n 50` to see what went wrong.

---

## PART 8 — Set up Nginx (web gateway + HTTPS)

Nginx sits in front of FastAPI. It handles HTTPS and forwards
requests to your app running on port 8000.

### Step 8.1 — Create the Nginx config
```bash
nano /etc/nginx/sites-available/humantrace
```

Paste exactly this content:

```nginx
server {
    listen 80;
    server_name humantrace.au www.humantrace.au humantrace.com.au www.humantrace.com.au;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # File upload size limit — increase for large documents
        client_max_body_size 20M;
    }
}
```

Save: **Ctrl+X**, **Y**, **Enter**.

### Step 8.2 — Enable the site
```bash
ln -s /etc/nginx/sites-available/humantrace /etc/nginx/sites-enabled/
nginx -t
```

`nginx -t` should say `syntax is ok` and `test is successful`.
If it does, run:
```bash
systemctl restart nginx
```

### Step 8.3 — Test before HTTPS
At this point, if DNS has propagated, you should be able to visit:
```
http://humantrace.au
```
in your browser and see the HumanTrace interface over HTTP (not HTTPS yet).

---

## PART 9 — Enable HTTPS with Let's Encrypt

### Step 9.1 — Run Certbot
```bash
certbot --nginx -d humantrace.au -d www.humantrace.au -d humantrace.com.au -d www.humantrace.com.au
```

Certbot will:
- Ask for your email address (for renewal reminders)
- Ask you to agree to terms — type `Y`
- Automatically obtain certificates and update your Nginx config

### Step 9.2 — Confirm HTTPS works
Visit https://humantrace.au in your browser.
You should see the padlock icon and the HumanTrace consumer interface.
Visit https://humantrace.au/institutional — you should see the institutional interface.

### Step 9.3 — Auto-renewal
Certbot sets up automatic renewal by default. Confirm it's active:
```bash
certbot renew --dry-run
```
Should say "Congratulations, all simulated renewals succeeded."

---

## PART 10 — Confirm everything works

Run through this checklist:

| Check | URL | Expected |
|-------|-----|----------|
| Consumer interface | https://humantrace.au | HumanTrace interface loads |
| Institutional interface | https://humantrace.au/institutional | Institutional UI loads |
| Health endpoint | https://humantrace.au/health | JSON with status: running |
| iPhone | Open humantrace.au in Safari on iPhone | Interface loads, mobile-friendly |
| www redirect | https://www.humantrace.au | Redirects or loads correctly |
| .com.au | https://humantrace.com.au | Same as .au |

---

## PART 11 — Keeping the server updated

When you make changes to your code on your ThinkPad and push to GitHub:

```bash
# SSH into the server
ssh root@123.456.78.90

# Pull the latest code
cd /var/www/humantrace
sudo -u humantrace git pull

# Restart HumanTrace
systemctl restart humantrace

# Check it restarted cleanly
systemctl status humantrace
```

That's the full deployment cycle. Three commands to ship an update.

---

## Troubleshooting

**HumanTrace not starting:**
```bash
journalctl -u humantrace -n 100
```
Shows the last 100 lines of logs. Look for the error message.

**Nginx not working:**
```bash
nginx -t
journalctl -u nginx -n 50
```

**Can't reach the site:**
1. Check DNS has propagated: https://dnschecker.org
2. Check the firewall allows HTTP/HTTPS:
   ```bash
   ufw allow 80
   ufw allow 443
   ufw allow 22
   ufw enable
   ```
3. Check HumanTrace is running: `systemctl status humantrace`

**Certificate error:**
```bash
certbot renew
systemctl restart nginx
```

---

## Summary — what you'll have when done

- https://humantrace.au → Consumer interface
- https://humantrace.au/institutional → Institutional interface
- https://humantrace.com.au → Same (both domains point to same server)
- https://www.humantrace.au → Same
- Automatic HTTPS renewal
- HumanTrace restarts automatically after server reboots or crashes
- Deploy updates in 3 commands from your ThinkPad

**Monthly cost: $6 USD (~$9 AUD)**

---

*When you're ready to start, go to https://digitalocean.com and work through Part 1.*
*Come back to this guide at each step. Take your time — there's no rush.*