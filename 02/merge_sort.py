import random
import time

def merge_sort(arr):
    # Se o array tem 1 ou 0 elementos, já está ordenado
    if len(arr) <= 1:
        return arr

    # Divide o array no meio
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Chama recursivamente o merge_sort para as duas metades
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Junta as duas metades ordenadas
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_arr = []
    left_index = right_index = 0

    # Intercala os elementos de left e right em ordem
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1

    # Adiciona o restante dos elementos de left e right
    sorted_arr.extend(left[left_index:])
    sorted_arr.extend(right[right_index:])

    return sorted_arr


lista = [random.randint(1, 1000000) for _ in range(5000000)]

inicio = time.time()

lista_ordenada = merge_sort(lista)

fim = time.time()

print(f"Tempo para ordenar 5 milhões de registros: {fim - inicio:.4f} segundos")
