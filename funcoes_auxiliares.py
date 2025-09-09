
# FUNÇÕES AUXILIARES PARA OS 2 ALGORITMOS PRINCIPAIS (AG E TS).
# Além disso, neste arquivo, tem uma função para criar um grafo não direcional, conexo e completo.
# Esse grafo é representado por uma matriz de adjacência 

import random
import numpy as np

# Implementação rota_aletaroia
def rota_aleatoria(matriz):
    # descobrir a tamanho de uma dimensão da matriz
    # primeiro verificar se a matriz é quadrada:
    if not all(len(linha) == len(matriz) for linha in matriz):
        raise ValueError("Matriz não quadrada")
    tamanho = len(matriz)
    rota = list(range(tamanho))
    random.shuffle(rota)
    return rota

def trocar_cidades(solucao):
    tamanho = len(solucao)
    posicao_1, posicao_2 = random.sample(range(tamanho), 2) # garante que sejam diferentes
    solucao_nova = solucao[:]
    auxiliar = solucao[posicao_1]
    solucao_nova[posicao_1] = solucao_nova[posicao_2]
    solucao_nova[posicao_2] = auxiliar
    return solucao_nova

def custo(solucao, matriz):
    tamanho = len(matriz)
    custo_total = 0
    for i in range(tamanho - 1):
        custo_total = custo_total + matriz[solucao[i]][solucao[i+1]]
    custo_total = custo_total + matriz[solucao[-1]][solucao[0]]
    return custo_total

# Matriz de adjacência
def gera_matriz_distancias(n, min_dist=1, max_dist=100, seed=None):
    if seed is not None:
        np.random.seed(seed)
    matriz = np.random.randint(min_dist, max_dist+1, size=(n, n))
    matriz = (matriz + matriz.T) // 2 
    np.fill_diagonal(matriz, 0)
    return matriz
