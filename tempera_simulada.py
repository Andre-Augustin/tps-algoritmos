import math
import random

from funcoes_auxiliares import rota_aleatoria, trocar_cidades, custo

def tempera_simulada(cidades, temperatura_inicial, temperatura_minima, taxa_resfriamento, max_iter=500):
    solucao_atual = rota_aleatoria(cidades)
    solucao_melhor = solucao_atual
    temperatura = temperatura_inicial

    historico_custos = []  # lista para guardar os custos por iteração

    for _ in range(max_iter):  # roda exatamente max_iter vezes
        # Guarda o custo da solução atual
        historico_custos.append(custo(solucao_atual, cidades))
        
        solucao_nova = trocar_cidades(solucao_atual)
        delta = custo(solucao_nova, cidades) - custo(solucao_atual, cidades)

        if delta < 0:
            solucao_atual = solucao_nova
        else:
            probabilidade = math.exp(-delta / temperatura)
            if random.random() < probabilidade:
                solucao_atual = solucao_nova

        if custo(solucao_atual, cidades) < custo(solucao_melhor, cidades):
            solucao_melhor = solucao_atual

        # Resfriamento controlado
        temperatura = max(temperatura * taxa_resfriamento, temperatura_minima)

    return solucao_melhor, historico_custos
