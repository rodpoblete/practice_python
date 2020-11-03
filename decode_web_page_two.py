"""Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this
website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you
can read the full article without having to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution of
the exercise posted here.)

This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise
we will learn how to write this text to a .txt file. """
import requests
from bs4 import BeautifulSoup


def run():
    url = (
        "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
    )
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, "html.parser")
    article_container = soup.find_all("div", class_="article__body")

    for index in range(0, len(article_container) + 1):
        for content in range(0, len(article_container[index].contents)):
            print(article_container[index].contents[content].get_text())

    # for article_content in soup.find_all("div", class_="article__body"):
    #     if article_content.p:
    #         print(article_content.p.text)
    #     else:
    #         print(article_content.contents[0])  # Falta más anidamiento para llegar al contenido


if __name__ == "__main__":
    run()
