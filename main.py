from scraper.browser import fetch_html
from scraper.extractor import extract_properties
from database.db import init_db, insert_data
from analysis.analysis import analyze


URL = "https://www.magicbricks.com/property-for-rent/residential-real-estate?cityName=Chennai"


def main():
    print("Scraping started...")
    html = fetch_html(URL)

    properties = extract_properties(html)
    print("Total properties extracted:", len(properties))

    print("Initializing database...")
    init_db()

    print("Inserting data...")
    insert_data(properties)

    print("Running analysis...")
    analyze()

    print("Done.")


if __name__ == "__main__":
    main()