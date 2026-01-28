import requests
from config import DISCORD_WEBHOOK_URL

def send_discord_alert(listing):
    payload = {
        "content": (
            " **POKÉMON RESTOCK ALERT** \n"
            f"**Site:** {listing['site']}\n"
            f"**Item:** {listing['title']}\n"
            f"**Price:** {listing['price']}\n"
            f"{listing['url']}"
        )
    }

    requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=10)
