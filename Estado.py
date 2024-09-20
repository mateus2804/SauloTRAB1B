from classes.Acao import Acao


class Estado:
    def __init__(self):
        self.Acoes = []
        self.isFinal = False
        self.isInicial = False

    def InserirAcao(self, simbolo, caracter, destino):
        self.Acoes.append(Acao(simbolo, caracter, destino))