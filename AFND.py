from classes.Estado import Estado

class AFND:
    def __init__(self, inicial: Estado, finais, estados):
        self.palavra = ""
        self.Inicial = inicial
        self.Finais = finais
        self.Estados = estados

    def TestarPalavra(self, palavra: str):
        estadoAtual = self.Inicial
        for letra in range(len(palavra)):
            acao = None
            for mov in estadoAtual.Acoes:
                if mov.caracter == palavra[letra]:
                    acao = mov
                    break
            if acao is None:
                return False
            self.palavra += palavra[letra]
            estadoAtual = self.Estados[acao.simbDestino]

        if estadoAtual in self.Finais:
            return True
        return False