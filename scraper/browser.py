from playwright.sync_api import sync_playwright


def fetch_html(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (X11; Linux x86_64)"
        )
        page = context.new_page()

        page.goto(url, timeout=60000)
        page.wait_for_selector("div.mb-srp__card")  # wait for listings

        html = page.content()
        browser.close()

        return html