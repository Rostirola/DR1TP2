class FilaAtendimento:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, nome):
        # Adiciona o cliente ao final da fila
        self.fila.append(nome)
        print(f"Cliente {nome} adicionado à fila.")

    def atender_cliente(self):
        # Verifica se a fila está vazia antes de tentar atender
        if self.fila:
            # Remove o cliente do início da fila
            cliente = self.fila.pop(0)
            print(f"Atendendo o cliente: {cliente}")
        else:
            print("Não há clientes na fila para atender.")

    def tamanho_fila(self):
        # Retorna o número de clientes na fila
        return len(self.fila)


fila = FilaAtendimento()

fila.adicionar_cliente("João")
fila.adicionar_cliente("Maria")
fila.adicionar_cliente("Carlos")

print(f"Tamanho da fila: {fila.tamanho_fila()}")

fila.atender_cliente()
print(f"Tamanho da fila: {fila.tamanho_fila()}")

fila.atender_cliente()
fila.atender_cliente()
fila.atender_cliente()
