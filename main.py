from sites import pokemon_center
from alert import send_discord_alert

seen = set()

def main():
    listings = pokemon_center.check()

    for item in listings:
        key = f"{item['site']}_{item['url']}"

        if item["in_stock"] and key not in seen:
            seen.add(key)
            send_discord_alert(item)
            print("ALERT SENT!")
        else:
            print("No restock:", item["site"])

if __name__ == "__main__":
    main()