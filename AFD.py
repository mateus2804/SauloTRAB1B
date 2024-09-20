from classes.Estado import Estado
from classes.AFND import AFND
from combinacao import todas_combinacoes

class AFD:
    def __init__(self, AFND: AFND):
        self.Inicial = None
        self.Finais = []
        self.Estados = {}
        self.EstadosTrad = {}
        self.Alfabeto = ['0', '1']
        self.Tabela = {}
        self.AFND = AFND
        self.CriarEstadosTraducao()

    def CriarEstadosTraducao(self):
        simb = 'A'
        comb = todas_combinacoes([simb for simb in self.AFND.Tabela.keys()])
        for n in range(len(comb)):
            self.EstadosTrad[simb] = comb[n]
            simb = chr(ord(simb) + 1)

