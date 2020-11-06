"""Este ejercicio es la parte 1 de 4 de la serie de ejercicios Tic Tac Toe. Los otros ejercicios son: Parte 2,
Parte 3 y Parte 4. ¡Es hora de algunos gráficos falsos! Digamos que queremos dibujar tableros de juego que se vean así:
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---

Este es 3x3 (como en el tic tic toe). Obviamente, vienen en muchos otros tamaños (8x8 para el ajedrez,
19x19 para el Go, y muchos más). Pregunte al usuario qué tamaño de tablero de juego quiere dibujar, y dibújelo en la
pantalla usando la declaración impresa de Python. Recuerde que en Python 3, la impresión en la pantalla se realiza
mediante:
  print("Thing to show on screen")"""


def run():
    """Retorna un tablero de ajedrez de las medidas que el usuario indique."""
    medida = int(input("Ingresa la medida del tablero: "))
    print(" ---" * medida)
    for borde in range(medida):
        print("|   " * (medida + 1))
        print(" ---" * medida)


if __name__ == "__main__":
    run()
