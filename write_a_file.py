"""Take the code from the How To Decode A Website exercise (if you didnt do it
or just want to play with some different code, use the code from the solution),
and instead of printing the  results to a screen, write the results to a txt
file. In your code, just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved."""
import requests
from bs4 import BeautifulSoup


def run():
    """Toma el texto extraído de un sitio web y lo pasa a un archivo de texto
    plano. Opcionalmente el usuario puede nombrar el archivo.
    """
    url = "https://www.nytimes.com/"
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, "html.parser")
    list_articles = []

    for article in soup.find_all("h2"):
        list_articles.append(article.get_text())

    listToStr = "".join(
        [str(elem) for elem in list_articles]
    )  # Parsea la lista a un string

    name_file = input("Enter a name of file: ")
    with open(f"{name_file}.txt", "w") as open_file:
        open_file.write(listToStr)


if __name__ == "__main__":
    run()
