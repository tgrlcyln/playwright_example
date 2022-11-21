from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def main():
    url = 'https://onedio.com'
    with sync_playwright() as p:
        browser = p.webkit.launch(
            # proxy={"server": "172.217.160:142"}
        )
        page = browser.new_page()
        page.goto(url)
        html = page.content()
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.get_text())

if __name__ == '__main__':
    main()