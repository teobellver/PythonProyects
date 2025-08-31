import time
lista = input("introduce la lista de números separados por espacios: ")
listaordenada = sorted(
    int(num)for num in lista
    )
print("La lista ordenada es:", listaordenada)
time.sleep(100)