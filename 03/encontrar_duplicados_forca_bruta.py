def encontrar_duplicados_forca_bruta(lista):
    duplicados = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados


lista = [1, 2, 3, 4, 5, 1, 6, 2, 7, 8, 9, 5]

duplicados_forca_bruta = encontrar_duplicados_forca_bruta(lista)
print("Duplicados (Força Bruta):", duplicados_forca_bruta)
