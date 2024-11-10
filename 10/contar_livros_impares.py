from collections import deque

def contar_livros_impares(fila_livros):
    contador_impares = 0

    for id_livro in fila_livros:
        # Verifica se o número é ímpar
        if id_livro % 2 != 0:
            contador_impares += 1

    # Retorna o total de livros com identificações ímpares
    return contador_impares


fila_livros = deque([101, 202, 303, 404, 505])
print(contar_livros_impares(fila_livros))
