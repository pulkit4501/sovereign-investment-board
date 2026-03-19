import os
import sys
import json
import urllib.request
import urllib.error

# CONFIGURATION
# In a real deployment, these would be loaded from environment variables
# or a secure config file.
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID_HERE")

def send_alert(message):
    """
    Sends a message to the Chairman's Telegram channel.
    """
    if TELEGRAM_BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("MOCK ALERT (Telegram not configured):")
        print(f"--------------------------------------------------")
        print(message)
        print(f"--------------------------------------------------")
        return

    
    # Check if message is a file path (PDF)
    if message.endswith(".pdf") and os.path.exists(message):
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument"
        # For sending files, we need multipart/form-data. 
        # Using a simpler approach with `curl` for reliability if python requests is not available,
        # but since we are refactoring, let's use standard library with multipart.
        # Actually, to keep it simple and robust without 'requests' (if user env is strict),
        # let's try a direct POST with boundary.
        
        # SIMPLIFICATION: If we have 'requests' installed (which we likely do or can use), use it.
        # If not, we fall back to a subprocess curl for file (easiest for "no-dep" constraints).
        try:
            import requests # Attempt import again since we might have installed it or it exists
            with open(message, 'rb') as f:
                files = {'document': f}
                data = {'chat_id': TELEGRAM_CHAT_ID}
                response = requests.post(url, data=data, files=files)
            
            if response.status_code == 200:
                print("✓ PDF Report sent successfully.")
            else:
                print(f"⚠ FAILED to send PDF. HTTP {response.status_code}: {response.text}")
                # Fallback to text message if PDF fails
                url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
                payload = {
                    "chat_id": TELEGRAM_CHAT_ID,
                    "text": f"⚠ Could not attach PDF report (Error {response.status_code}).\n\nPlease check logs.",
                    "parse_mode": "HTML"
                }
                urllib.request.urlopen(urllib.request.Request(url, json.dumps(payload).encode('utf-8'), {'Content-Type': 'application/json'}))

            return
        except ImportError:
            # Fallback to CURL if requests is missing
            cmd = f'curl -v -F chat_id="{TELEGRAM_CHAT_ID}" -F document=@"{message}" {url}'
            os.system(cmd)
            return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    
    try:
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            print("✓ Executive Brief sent successfully.")
    except urllib.error.HTTPError as e:
        print(f"⚠ FAILED to send alert: {e}")
        print(f"Response: {e.read().decode('utf-8')}")
    except urllib.error.URLError as e:
        print(f"⚠ Connection failed: {e}")
    except Exception as e:
        print(f"⚠ An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python telegram_ping.py 'Your message here'")
        sys.exit(1)
        
    message = sys.argv[1]
    
    if message.endswith(".pdf") and os.path.exists(message):
        send_alert(message)
    else:
        # FORMATTING THE EXECUTIVE BRIEF
        header = "🚨 **SOVEREIGN BOARDROOM: EXECUTIVE BRIEF** 🚨\n\n"
        full_message = header + message
        send_alert(full_message)
