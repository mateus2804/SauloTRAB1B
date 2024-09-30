from classes.Acao import Acao
from classes.Estado import Estado
from classes.AFND import AFND
from combinacao import todas_combinacoes

class AFD:
    def __init__(self, AFND: AFND):
        self.Inicial = None
        self.Finais = []
        self.Estados = {}
        self.Alfabeto = ['0', '1']
        self.Tabela = {}
        self.Traducao = {}
        self.AFND = AFND
        self.CriarTabela()
        self.CriarArquivoSaida()

    def CriarTabela(self):
        comb = todas_combinacoes([simb for simb in self.AFND.Tabela.keys()])
        for simb in comb:
            if len(simb) == 1:
                var0 = self.AFND.Tabela[simb[0]][self.Alfabeto[0]]
                var1 = self.AFND.Tabela[simb[0]][self.Alfabeto[1]]
                self.Tabela[simb] = {
                    self.Alfabeto[0]: var0,
                    self.Alfabeto[1]: var1
                }
            else:
                var0 = set()
                var1 = set()
                for element in simb:
                    temp0 = self.AFND.Tabela[element][self.Alfabeto[0]]
                    temp1 = self.AFND.Tabela[element][self.Alfabeto[1]]
                    var0 = var0 | set(temp0)
                    var1 = var1 | set(temp1)

                toList0 = list(var0)
                toList1 = list(var1)
                toList0.sort()
                toList1.sort()

                self.Tabela[simb] = {
                    self.Alfabeto[0]: tuple(toList0),
                    self.Alfabeto[1]: tuple(toList1)
                }
        self.CriarTraducao()
        self.CriarEstados()
        self.EliminarImp()


    def CriarTraducao(self):
        counter = 0
        start = 'Q0'
        for n in self.Tabela.keys():
            self.Traducao[n] = start
            counter += 1
            start = f'Q{counter}'

    def CriarEstados(self):
        for simb in self.Tabela.keys():
            estado = Estado()

            if len(simb) == 1 and self.AFND.Estados[simb[0]].isInicial == True:
                estado.isInicial = True
                self.Inicial = self.Traducao[simb]

            for letra in simb:
                if self.AFND.Estados[letra].isFinal == True:
                    estado.isFinal = True
                    self.Finais.append(self.Traducao[simb])
                    break

            if len(self.Tabela[simb]['0']) != 0:
                estado.Acoes.append(Acao(self.Traducao[simb], '0', self.Traducao[self.Tabela[simb]['0']]))
            if len(self.Tabela[simb]['1']) != 0:
                estado.Acoes.append(Acao(self.Traducao[simb], '1', self.Traducao[self.Tabela[simb]['1']]))

            self.Estados[self.Traducao[simb]] = estado
    def EliminarImp(self):
        toEliminar = []
        for (simb, estado) in self.Estados.items():
            isImp = True
            for (simb1, estado1) in self.Estados.items():
                if len([x.simbDestino for x in estado1.Acoes if x.simbDestino == simb]) > 0:
                    isImp = False
                    break
            if isImp:
                toEliminar.append(simb)
        for n in toEliminar:
            self.Estados.pop(n)
        self.AttFinais()

    def AttFinais(self):
        for n in self.Finais:
            if n not in self.Estados.keys():
                self.Finais.remove(n)
    def TestarPalavra(self, palavra):
        estadoAtual = self.Estados[self.Inicial]
        for letra in range(len(palavra)):
            acao = None
            for mov in estadoAtual.Acoes:
                if mov.caracter == palavra[letra]:
                    acao = mov
                    break
            if acao is None:
                return False
            estadoAtual = self.Estados[acao.simbDestino]
        return estadoAtual.isFinal

    def CriarArquivoSaida(self):
        with open('AFD.txt', 'w') as file:
            estados = ""
            for (key, value) in self.Estados.items():
                estados += f'{key} '
            file.write(estados)
            file.write('\n')
            file.write(self.Inicial)
            file.write('\n')
            finais = ""
            for estado in self.Finais:
                finais += f'{estado} '
            file.write(finais)
            file.write('\n')
            for (key, value) in self.Estados.items():
                for acao in value.Acoes:
                    file.write(f'{acao.simbOrigem} {acao.caracter} {acao.simbDestino}')
                    file.write('\n')
    def Parte2(self, path):
        with open(path, 'r') as file:
            writeFile = open('resposta2.txt', 'w')
            for line in file:
                line = line.strip()
                if self.TestarPalavra(line) == True:
                    writeFile.write(f'{line} aceito')
                    writeFile.write('\n')
                else:
                    writeFile.write(f'{line} nao aceito')
                    writeFile.write('\n')
            writeFile.close()





