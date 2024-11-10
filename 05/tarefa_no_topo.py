def tarefa_no_topo(pilha_de_tarefas):
    if not pilha_de_tarefas:
        return None
    return pilha_de_tarefas[-1]

pilha_de_tarefas = ["Tarefa 1", "Tarefa 2", "Tarefa 3"]
print(tarefa_no_topo(pilha_de_tarefas))
