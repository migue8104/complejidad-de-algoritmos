def Torres_hanoi(n, origen, destino, auxiliar):
    if n >= 1:
        Torres_hanoi(n - 1, origen, auxiliar, destino)
        print("mover dico",origen,"a",destino)
        Torres_hanoi(n - 1, auxiliar, destino, origen)


