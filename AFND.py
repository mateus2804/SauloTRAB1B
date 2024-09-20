from classes.Estado import Estado

class AFND:
    def __init__(self, inicial: Estado, finais, estados):
        self.Inicial = inicial
        self.Finais = finais
        self.Estados = estados
        self.Alfabeto = ['0', '1']
        self.Tabela = {}

    # def TestarPalavra(self, palavra: str):
    #     estadoAtual = self.Inicial
    #     for letra in range(len(palavra)):
    #         acao = None
    #         for mov in estadoAtual.Acoes:
    #             if mov.caracter == palavra[letra]:
    #                 acao = mov
    #                 break
    #         if acao is None:
    #             return False
    #         self.palavra += palavra[letra]
    #         estadoAtual = self.Estados[acao.simbDestino]
    #
    #     if estadoAtual in self.Finais:
    #         return True
    #     return False

    def CriarTabela(self):
        for simb, estado in self.Estados.items():
            var0 = [acao.simbDestino for acao in estado.Acoes if acao.caracter == self.Alfabeto[0]]
            var1 = [acao.simbDestino for acao in estado.Acoes if acao.caracter == self.Alfabeto[1]]
            var0.sort()
            var1.sort()
            letras = {self.Alfabeto[0]: var0,
                      self.Alfabeto[1]: var1}
            self.Tabela[simb] = letras