"""Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to
largest) and another number. The function decides whether or not the given number is inside the list and returns (
then prints) an appropriate boolean.

Extras:

    Use binary search.
"""
from time import time


def busqueda_normal(numero_a_buscar, lista_elementos):
    """Función que toma un número ingresado por el usuario y lo busca en una lista ordenada de elementos."""
    busqueda = [num for num in lista_elementos if num == numero_a_buscar]
    if busqueda:
        return print(f"{numero_a_buscar} si esta en la lista")
    else:
        return print(f"{numero_a_buscar} no esta en la lista")


def busqueda_binaria(numero_a_buscar, lista_elementos):
    """Función que busca un número ingresado en una lista ordenada a través de búsqueda binaria con un ciclo."""
    izquierda, derecha = (
        0,
        len(lista_elementos) - 1,
    )  # Establecemos los indices para cada lado del arreglo.
    while izquierda <= derecha:
        indice_del_elemento_del_medio = (izquierda + derecha) // 2
        elemento_medio = lista_elementos[indice_del_elemento_del_medio]
        if elemento_medio == numero_a_buscar:
            return print(
                f"El número {numero_a_buscar} se encuentra en la lista en el índice: {indice_del_elemento_del_medio}"
            )
        if numero_a_buscar < elemento_medio:
            derecha = indice_del_elemento_del_medio - 1
        else:
            izquierda = indice_del_elemento_del_medio + 1
    # Si se sale del ciclo, significa que no existe el valor
    return print(f"{numero_a_buscar} no esta en la lista")


if __name__ == "__main__":
    numero = int(input("Ingrese número a buscar en la lista: "))
    lista = [1, 2, 3, 10, 30, 50, 77, 90, 100]

    start_time = time()
    busqueda_normal(numero, lista)
    elapsed_time = time() - start_time
    print("Tiempo transcurrido búsqueda normal: %.10f segundos\n" % elapsed_time)

    start_time = time()
    busqueda_binaria(numero, lista)
    elapsed_time = time() - start_time
    print("Tiempo transcurrido búsqueda binaria: %.10f segundos" % elapsed_time)