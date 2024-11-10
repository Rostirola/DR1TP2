def ordenar_lista(lista):
    n = len(lista)

    for i in range(n):
        # Aloca os últimos i elementos no lugar correto a cada iteração
        for j in range(0, n - i - 1):
            # Troca os elementos se o atual for maior que o próximo
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista_numeros = [5, 3, 8, 4, 2]
lista_ordenada = ordenar_lista(lista_numeros)
print("Lista ordenada:", lista_ordenada)
