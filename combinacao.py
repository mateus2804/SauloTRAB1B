import itertools

def todas_combinacoes(lista):
    combinacoes = []

    # Adicionar elementos individuais como tuplas
    for item in lista:
        combinacoes.append((item,))

    # Adicionar combinações de dois ou mais elementos como tuplas
    for i in range(2, len(lista) + 1):
        combinacoes.extend([tuple(comb) for comb in itertools.combinations(lista, i)])

    return combinacoes
