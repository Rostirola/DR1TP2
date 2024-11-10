class TabelaHash:
    # Construtor que aceita um tamanho inicial para a tabela hash.
    def __init__(self, tamanho=10):
        # Cria tabela como uma lista de listas
        self.tabela = [[] for _ in range(tamanho)]
        self.tamanho = tamanho

    # Função de hash simples para calcular o índice da tabela com base na chave.
    def _hash(self, chave):
        return hash(chave) % self.tamanho

    # Insere uma chave e seu valor na tabela hash.
    def inserir(self, chave, valor):
        indice = self._hash(chave)

        for i, (ch, val) in enumerate(self.tabela[indice]):
            if ch == chave:
                self.tabela[indice][i] = (chave, valor)
                return
        # Caso a chave não exista, adiciona uma nova entrada
        self.tabela[indice].append((chave, valor))

    # Insere uma chave e seu valor na tabela hash.
    def buscar(self, chave):
        indice = self._hash(chave)
        for ch, val in self.tabela[indice]:
            if ch == chave:
                return val
        # Retorna None se a chave não for encontrada
        return None

    # Remove uma chave e seu valor da tabela hash.
    def remover(self, chave):
        indice = self._hash(chave)
        for i, (ch, val) in enumerate(self.tabela[indice]):
            if ch == chave:
                del self.tabela[indice][i]  # Remove a entrada
                return True
        # Retorna False se a chave não for encontrada
        return False


tabela = TabelaHash(10)
tabela.inserir("nome", "João")
tabela.inserir("idade", 30)

print(tabela.buscar("nome"))
print(tabela.buscar("idade"))

tabela.remover("idade")
print(tabela.buscar("idade"))
