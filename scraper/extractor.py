from bs4 import BeautifulSoup
from scraper.cleaner import clean_price


def extract_properties(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")
    cards = soup.select("div.mb-srp__card")

    properties = []

    for card in cards:
        title_tag = card.select_one(".mb-srp__card--title")
        price_tag = card.select_one(".mb-srp__card__price")
        location_tag = card.select_one(".mb-srp__card--address")
        bhk = card.select_one(".mb-srp__card__bhk")
        bathroom = card.select_one(".mb-srp__card__bathroom")
        furnishing = card.select_one(".mb-srp__card__furnishing")

        title = title_tag.get_text(strip=True) if title_tag else None
        location = location_tag.get_text(strip=True) if location_tag else None
        raw_price = price_tag.get_text(strip=True) if price_tag else None

        price = clean_price(raw_price)

        if title and price:
            properties.append({
                "title": title,
                "price": price,
                "location": location
            })

    return properties

