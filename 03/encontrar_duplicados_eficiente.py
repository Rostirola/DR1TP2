def encontrar_duplicados_eficiente(lista):
    vistos = set()
    duplicados = set()
    for numero in lista:
        if numero in vistos:
            duplicados.add(numero)
        else:
            vistos.add(numero)
    return list(duplicados)


lista = [1, 2, 3, 4, 5, 1, 6, 2, 7, 8, 9, 5]

duplicados_eficiente = encontrar_duplicados_eficiente(lista)
print("Duplicados (Eficiente):", duplicados_eficiente)
