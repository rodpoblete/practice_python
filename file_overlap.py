"""Dados dos archivos .txt que tienen listas de números en ellos, encuentra los números que se superponen. Un archivo
.txt tiene una lista de todos los números primos por debajo de 1000, y el otro archivo .txt tiene una lista de
números felices hasta 1000.

(Si lo olvidaste, los números primos son números que no pueden ser divididos por ningún otro número. Y sí,
los números felices son verdaderos en las matemáticas, puedes buscarlo en Wikipedia"""


def run():
    """Lee 2 archivos txt y retorna un array con la lista de las similitudes entre ambos."""

    lista_primos = []
    lista_felices = []
    lista_solapados = []
    with open("primenumbers.txt", "r") as n_primos:
        with open("happynumbers.txt", "r") as n_felices:
            linea_primos = n_primos.readline()
            linea_felices = n_felices.readline()
            while linea_felices:
                lista_felices.append(linea_felices.strip())
                linea_felices = n_felices.readline()
        while linea_primos:
            lista_primos.append(linea_primos.strip())
            linea_primos = n_primos.readline()

    lista_comparacion = [
        primo for primo in lista_primos for feliz in lista_felices if primo == feliz
    ]

    for numero in lista_comparacion:
        if numero not in lista_solapados:
            lista_solapados.append(numero)

    print(lista_solapados)


if __name__ == "__main__":
    run()
