from classes.AFD import AFD
from classes.Estado import Estado
from classes.AFND import AFND
from combinacao import todas_combinacoes

# declarando dicionário de estados
estados = {}

# abrindo o file apenas para pegar o conteudo da primeira linha
file = open('AFND.txt', 'r')
readEstados = file.readline().strip().split(' ')
file.close()

# salvando os estados no dicionario
for estado in readEstados:
    estados[estado] = Estado()

# salvando o estado inicial
file = open('AFND.txt', 'r')
file.readline()
readInicial = file.readline().strip()
estados[readInicial].isInicial = True
file.close()

# salvando os estados finais
file = open('AFND.txt', 'r')
file.readline()
file.readline()
readFinais = file.readline().strip().split(' ')
for e in readFinais:
    estados[e].isFinal = True
file.close()

# salvando as possiveis movimentações em cada estado
file = open('AFND.txt', 'r')

# pulando as 3 primeiras linhas
file.readline()
file.readline()
file.readline()

# lendo as movimentaçoes
for line in file:
    seq = line.strip().split(' ')
    estados[seq[0]].InserirAcao(seq[0], seq[1], seq[2])
file.close()

automatoND = AFND(estados[readInicial], [estados[simb] for simb in readFinais], estados)
automatoND.CriarTabela()

automatoD = AFD(automatoND)



