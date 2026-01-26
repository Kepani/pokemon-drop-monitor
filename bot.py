import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from config import DISCORD_WEBHOOK_URL, PRODUCT_URL, CHECK_INTERVAL

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def send_discord_alert(message):
    payload = {"content": message}
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
    response.raise_for_status()

def is_in_stock():
    response = requests.get(PRODUCT_URL, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    page_text = soup.get_text().lower()

    return "out of stock" not in page_text

def main():
    last_status = is_in_stock()
    log("Pokemon Drop Monitor Started")

    try:
        while True:
            current_status = is_in_stock()
            log("Checked stock status")

            if current_status and not last_status:
                send_discord_alert(
                    f"🔥 **POKÉMON ETB RESTOCK DETECTED** 🔥\n{PRODUCT_URL}"
                )
                log("Restock detected - alert sent")

            last_status = current_status
            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        log("Bot stopped by user")

    except Exception as error:
        log(f"Unexpected error: {error}")

if __name__ == "__main__":
    main()