import time
import requests
from bs4 import BeautifulSoup
from config import DISCORD_WEBHOOK_URL, PRODUCT_URL, CHECK_INTERVAL

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

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
    last_status = False

    while True:
        try:
            current_status = is_in_stock()

            if current_status and not last_status:
                send_discord_alert(
                    f"🔥 **POKÉMON ETB RESTOCK DETECTED** 🔥\n{PRODUCT_URL}"
                )

            last_status = current_status
            time.sleep(CHECK_INTERVAL)

        except Exception as error:
            print("Error:", error)
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
