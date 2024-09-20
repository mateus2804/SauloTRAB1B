import itertools
def todas_combinacoes(lista):
    combinacoes = []

    # Adicionar elementos individuais
    for item in lista:
        combinacoes.append(item)

    # Adicionar combinações de dois ou mais elementos como listas
    for i in range(2, len(lista) + 1):
        combinacoes.extend([list(comb) for comb in itertools.combinations(lista, i)])

    return combinacoes

# print(chr(ord('A') + 1))