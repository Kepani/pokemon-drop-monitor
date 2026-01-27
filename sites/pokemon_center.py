import requests
from bs4 import BeautifulSoup

# URL is defined here for test
URL = "https://www.pokemoncenter.com/product/10-10372-109/pokemon-tcg-mega-evolution-perfect-order-pokemon-center-elite-trainer-box"

def check():
    return[{
        "site": "Pokemon Center",
        "title": "Mega-Evolution Perfect Order Pokemon Center ETB",
        "in_stock": False,
        "price": None,
        "url": "https://www.pokemoncenter.com/product/10-10372-109/pokemon-tcg-mega-evolution-perfect-order-pokemon-center-elite-trainer-box"
    }]

    soup = BeautifulSoup(resp.text, "html.parser")

    # Detect out of stock
    page_text = soup.get_text().lower()
    in_stock = not("sold out" in page_text or "out of stock" in page_text)

    title_tag = soup.find("title")
    title = title_tag.text.strip() if title_tag else "Mega Evolution Perfect Order"

    return [{
        "site": "Pokemon Center",
        "title": title,
        "in_stock": in_stock,
        "price": None,
        "url": URL # Fetches the defined URL
    }]

