def contar_pedidos_impares(pilha_pedidos):
    # Inicializa o contador de pedidos com número ímpar
    contador_impares = 0

    while pilha_pedidos:
        # Retira o último pedido da pilha
        pedido = pilha_pedidos.pop()

        # Verifica se o número do pedido é ímpar
        if pedido % 2 != 0:
            contador_impares += 1

    return contador_impares


pilha_pedidos = [101, 202, 303, 404, 505]
quantidade_impares = contar_pedidos_impares(pilha_pedidos)

print("Quantidade de pedidos com número de identificação ímpar:", quantidade_impares)
