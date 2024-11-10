def ordenar_pilha(pilha):
    pilha_auxiliar = []

    while pilha:
        # Retira o topo da pilha original
        temp = pilha.pop()

        # Move os elementos da pilha auxiliar para a pilha original até achar o lugar certo para temp
        while pilha_auxiliar and pilha_auxiliar[-1] > temp:
            pilha.append(pilha_auxiliar.pop())

        # Coloca o elemento atual na pilha auxiliar
        pilha_auxiliar.append(temp)

    # Transfere elementos de volta para a pilha original em ordem crescente
    while pilha_auxiliar:
        pilha.append(pilha_auxiliar.pop())

    return pilha

pilha_notas = [70, 85, 60, 90, 75]
print("Pilha original:", pilha_notas)
pilha_ordenada = ordenar_pilha(pilha_notas)
print("Pilha ordenada:", pilha_ordenada)
