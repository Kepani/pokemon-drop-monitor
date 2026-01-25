# A Pokemon TCG Drop Monitor

A Python automated tool that monitors Pokemon TCG product pages and sends real-time Discord alerts when inventory stauts changes.

## Key Features
- Monitors product availability (in stock / out of stock)
- Sends Discord webhook alerts on restock
- Configurable check interval
- Simple, readable codebase

## How It Works
1. Periodically sends an HTTP GET request to a product page
2. Parses the page content to detect stock status
3. Triggers a Discord alert when a restock is detrected

## Tech stack
- Python
- Requests
- BeautifulSoup
- Discord Webhooks

## Setup
1. Clone Repo
2. Install dependencies:
pip install -r requirments.txt
3. Configure your Discord webhook and product URL in 'config.py'
4. Run the bot:
python bot.py

## Disclaimer
This product is for educational and monitoring purposes only.
No automated purchasing or ToS circumvention is performed.

## Future Improvements
- Support for multiple URLs
- Discord embeded-style alerts
- Async requests for improved performance
- Dockerized deployment