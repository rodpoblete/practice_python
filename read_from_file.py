"""Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
and print out the results to the screen. I have a .txt file for you, if you want to use it!

Extra:

    Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file,
    and count how many of each “category” of each image there are. This text file is actually a list of files
    corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the
    images. Once you take a look at the first line or two of the file, it will be clear which part represents the
    scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a
    little bit about it in this post."""
import collections


def run():
    """Toma un .txt lo lee y extrae la categoría del path del archivo retornando las repeticiones."""

    categorias = []
    with open("training.txt", "r") as open_file:
        linea = open_file.readline()  # Lee el contenido del archivo línea por línea
        while linea:
            line_split = linea.split("/") 
            categorias.append(line_split[2])
            linea = open_file.readline()

    contador_categorias = collections.Counter(categorias)  # Con en módulo Counter, se obtiene las repeticiones.
    for clave, valor in contador_categorias.items():
        print(clave, ":", valor)

    print(
        f"Las categorías que más se repiten son: {contador_categorias.most_common(3)}"
    )


if __name__ == "__main__":
    run()
