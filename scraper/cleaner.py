import re


def clean_price(price_text: str | None) -> int | None:
    if not price_text:
        return None

    price_text = price_text.lower().replace(",", "").strip()

    if "lac" in price_text:
        number = re.findall(r"\d+\.?\d*", price_text)
        if number:
            return int(float(number[0]) * 100000)

    if "cr" in price_text:
        number = re.findall(r"\d+\.?\d*", price_text)
        if number:
            return int(float(number[0]) * 10000000)

    number = re.findall(r"\d+", price_text)
    if number:
        return int(number[0])

    return None