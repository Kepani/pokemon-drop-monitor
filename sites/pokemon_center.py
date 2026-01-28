import requests
from bs4 import BeautifulSoup
import re

# URL is defined here for test
URL = "https://www.pokemoncenter.com/category/elite-trainer-box?srsltid=AfmBOoqOEeB7teZpL3G4ExmRyiIPpnYvKZo7DCysnTWPbscx9sGofEnI"

def check():
    try:
        resp = requests.get(
            URL, # fetch URL
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )
        resp.raise_for_status()
    except Exception as e:
        print("Pokemon Center request failed:", e)
        return[]

    soup = BeautifulSoup(resp.text, "html.parser")

    # This detects if stock is avail by string text
    page_text = soup.get_text().lower()
    in_stock = not("sold out" in page_text or "out of stock" in page_text or "unavailable" in page_text)

    # PKMN Center disables the add to cart button if out of stock, so this is how we will determine out of stock logic
    add_to_cart_btn = soup.find("button", {"data-test": "add-to-cart"})

    if add_to_cart_btn and not add_to_cart_btn.has_attr("disabled"):
        in_stock = True
    else:
        in_stock = False

    # Title
    title_tag = soup.find("title")
    title = title_tag.text.strip() if title_tag else "Pokemon Center Elite Trainer Box"

    # Price
    price = None

    # Pokemon Center usually embeds price as $XX.XX in text
    price_match = re.search(r"\$\d+.\d{2}", soup.get_text())
    if price_match:
        price = float(price_match.group().replace("$", ""))

    return [{
        "site": "Pokemon Center",
        "title": title,
        "in_stock": in_stock,
        "price": price,
        "url": URL # returns URL
    }]

