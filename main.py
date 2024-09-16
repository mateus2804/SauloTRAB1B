from classes.Estado import Estado
from classes.AFND import AFND

# declarando dicionário de estados
estados = {}

# abrindo o file apenas para pegar o conteudo da primeira linha
file = open('file.txt', 'r')
readEstados = file.readline().strip().split(' ')
file.close()

# salvando os estados no dicionario
for estado in readEstados:
    estados[estado] = Estado()

# salvando o estado inicial
file = open('file.txt', 'r')
file.readline()
readInicial = file.readline().strip()
file.close()

# salvando os estados finais
file = open('file.txt', 'r')
file.readline()
file.readline()
readFinais = file.readline().strip().split(' ')
file.close()

# salvando as possiveis movimentações em cada estado
file = open('file.txt', 'r')

# pulando as 3 primeiras linhas
file.readline()
file.readline()
file.readline()

# lendo as movimentaçoes
for line in file:
    seq = line.strip().split(' ')
    estados[seq[0]].InserirAcao(seq[0], seq[1], seq[2])



automatoND = AFND(estados[readInicial], [estados[simb] for simb in readFinais], estados)

print(automatoND.TestarPalavra('01010'))

