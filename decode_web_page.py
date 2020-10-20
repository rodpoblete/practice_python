"""Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York
Times homepage. """
import requests
from bs4 import BeautifulSoup


def run():
    """Print out list of all the article titles on the New York Times homepage."""
    url = "https://www.nytimes.com/"
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, "html.parser")
    list_articles = []

    for article in soup.find_all("h2"):
        list_articles.append(article.get_text())

    return print(list_articles)


if __name__ == "__main__":
    run()
