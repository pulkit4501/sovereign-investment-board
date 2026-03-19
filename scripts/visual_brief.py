import sys
import json
import matplotlib.pyplot as plt
import os
import urllib.request
import urllib.parse

# Import configuration from existing script if possible, else hardcode for reliability in this task
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID_HERE")

def send_image(image_path, caption=""):
    """Sends an image to Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    cmd = f'curl -s -F chat_id="{TELEGRAM_CHAT_ID}" -F photo=@"{image_path}" -F caption="{caption}" {url} > /dev/null'
    os.system(cmd)

def send_text(message):
    """Sends a text message."""
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
            pass
    except Exception as e:
        print(f"Error sending text: {e}")

def create_dashboard(data, filename="dashboard.png"):
    """Creates a visual summary dashboard."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis('off')

    # Background
    fig.patch.set_facecolor('#f0f0f0')

    # Title
    plt.text(0.05, 0.9, f"{data['ticker']} SNAPSHOT", fontsize=18, fontweight='bold', color='#003366')
    plt.text(0.05, 0.8, f"Price: {data['technical_analysis'].split('. ')[0]}", fontsize=14, color='#333333')

    # RSI Gauge
    rsi = data.get('rsi', 50)
    color = 'green' if 30 <= rsi <= 70 else 'red'
    plt.text(0.05, 0.6, "Momentum (RSI)", fontsize=10, fontweight='bold', color='#555555')
    
    # Draw simple bar for RSI
    rect = plt.Rectangle((0.05, 0.5), 0.4, 0.05, color='#dddddd')
    ax.add_patch(rect)
    rect_fill = plt.Rectangle((0.05, 0.5), 0.4 * (rsi/100), 0.05, color=color)
    ax.add_patch(rect_fill)
    plt.text(0.05 + 0.4 * (rsi/100), 0.57, str(rsi), fontsize=8, ha='center')

    # P/E or Key Metric
    pe = data.get('pe_ratio', 0)
    pe_text = f"{pe}x" if pe > 0 else "N/A"
    plt.text(0.55, 0.6, "Valuation (P/E)", fontsize=10, fontweight='bold', color='#555555')
    plt.text(0.55, 0.5, pe_text, fontsize=20, fontweight='bold', color='#003366')

    # Bottom Line
    verdict = data.get('verdict', 'N/A')
    v_color = 'green' if 'BUY' in verdict else 'red'
    plt.text(0.05, 0.2, "VERDICT:", fontsize=12, fontweight='bold', color='#333333')
    plt.text(0.25, 0.2, verdict, fontsize=14, fontweight='bold', color=v_color)

    plt.tight_layout()
    plt.savefig(filename, dpi=100, bbox_inches='tight')
    plt.close()

def format_report(data):
    return f"""
<b>🚨 SOVEREIGN BOARDROOM: EXECUTIVE BRIEF</b>
<b>TARGET: {data['ticker']}</b>

<b>⭐ THE BOTTOM LINE</b>
{data['bottom_line']}

<b>👶 THE "ELI5" (WHY IT MATTERS)</b>
{data['eli5']}

<b>📊 TECHNICAL ANALYST REPORT</b>
{data['technical_analysis']}

<b>🏦 FUNDAMENTAL ANALYST REPORT</b>
{data['fundamental_analysis']}

<b>🌏 MACRO STRATEGIST REPORT</b>
{data['macro_analysis']}

<i>— The Chairman</i>
"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python visual_brief.py '<json_data>'")
        sys.exit(1)
    
    # Sanitize currency again just in case
    raw_data = sys.argv[1].replace("₹", "Rs. ")
    data = json.loads(raw_data)
    
    # 1. Generate Image
    img_filename = f"chart_{data['ticker'].replace('.', '_')}.png"
    create_dashboard(data, img_filename)
    
    # 2. Send Image
    send_image(img_filename, caption=f"Visual Snapshot: {data['ticker']}")
    
    # 3. Send Text
    report_text = format_report(data)
    send_text(report_text)
    
    # Cleanup
    if os.path.exists(img_filename):
        os.remove(img_filename)

    print("✓ Visual Brief sent successfully.")
