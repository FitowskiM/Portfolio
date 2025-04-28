import requests
from bs4 import BeautifulSoup


def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("span", class_="text")

        for quote in quotes:
            print(quote.get_text())
    else:
        print(f"[!] Failed to fetch page. Status code: {response.status_code}")


# Example usage
scrape_quotes()