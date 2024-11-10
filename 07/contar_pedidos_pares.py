def contar_pedidos_pares(pilha_pedidos):
    # Inicializa o contador de pedidos com número par
    contador_pares = 0

    while pilha_pedidos:
        # Retira o último pedido da pilha
        pedido = pilha_pedidos.pop()

        # Verifica se o número do pedido é par
        if pedido % 2 == 0:
            contador_pares += 1

    return contador_pares


pilha_pedidos = [101, 202, 303, 404, 505]
quantidade_pares = contar_pedidos_pares(pilha_pedidos.copy())

print("Quantidade de pedidos com número de identificação par:", quantidade_pares)
