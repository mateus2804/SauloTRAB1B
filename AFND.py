from classes.Estado import Estado

class AFND:
    def __init__(self, inicial: Estado, finais, estados):
        self.Inicial = inicial
        self.Finais = finais
        self.Estados = estados
        self.Alfabeto = ['0', '1']
        self.Tabela = {}

    def CriarTabela(self):
        for simb, estado in self.Estados.items():
            var0 = [acao.simbDestino for acao in estado.Acoes if acao.caracter == self.Alfabeto[0]]
            var1 = [acao.simbDestino for acao in estado.Acoes if acao.caracter == self.Alfabeto[1]]
            var0.sort()
            var1.sort()
            letras = {self.Alfabeto[0]: tuple(var0),
                      self.Alfabeto[1]: tuple(var1)}
            self.Tabela[simb] = letras
