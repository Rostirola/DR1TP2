from collections import deque

def inverter_fila(fila):
    # Converte a lista em deque para simular uma fila
    fila_deque = deque(fila)

    # Inverte a ordem da fila
    fila_invertida = deque(reversed(fila_deque))

    # Converte novamente para lista antes de retornar
    return list(fila_invertida)


fila_original = ['Paciente1', 'Paciente2', 'Paciente3', 'Paciente4']
fila_invertida = inverter_fila(fila_original)
print(fila_invertida)
