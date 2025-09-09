import matplotlib.pyplot as plt
import random
import math
from algoritmo_genetico import algoritmoGenetico
from tempera_simulada import tempera_simulada
from funcoes_auxiliares import gera_matriz_distancias, custo, rota_aleatoria

if __name__ == "__main__":
    # --------- Parâmetros ---------
    n_cidades = 100
    n_iteracoes = 500  # número de gerações/iterações fixo para AG e TS
    
    # --------- Gera matriz de distâncias ---------
    distanciaCidades = gera_matriz_distancias(n_cidades)
    
    # --------- Algoritmo Genético ---------
    melhor_caminho_ag, melhor_custo_ag, historico_ag, custos_populacao_ag = algoritmoGenetico(distanciaCidades)
    
    # Custo médio e menor custo por geração do AG
    media_ag = [sum(custos)/len(custos) for custos in custos_populacao_ag]
    menor_ag = [min(custos) for custos in custos_populacao_ag]

    # --------- Têmpera Simulada ---------
    temperatura_inicial = 1000
    temperatura_minima = 1
    taxa_resfriamento = 0.95

    melhor_solucao_ts, historico_ts = tempera_simulada(
        distanciaCidades, 
        temperatura_inicial, 
        temperatura_minima, 
        taxa_resfriamento, 
        max_iter=n_iteracoes
    )
    
    # Custo por iteração no TS
    media_ts = historico_ts
    menor_ts = [min(historico_ts[:i+1]) for i in range(len(historico_ts))]

    # --------- Gráfico comparativo ---------
    plt.figure(figsize=(12,6))
    
    plt.plot(media_ag, label='Custo médio AG', color='blue')
    plt.plot(menor_ag, label='Menor custo AG', color='cyan')
    plt.plot(media_ts, label='Custo TS', color='red')
    plt.plot(menor_ts, label='Melhor custo TS', color='orange')

    plt.xlabel('Iterações / Gerações')
    plt.ylabel('Custo')
    plt.title('Comparação AG x TS')
    plt.legend()
    plt.grid(True)
    plt.show()

    # --------- Impressão dos melhores resultados ---------
    print("AG - Melhor caminho:", melhor_caminho_ag)
    print("AG - Custo do melhor caminho:", melhor_custo_ag)
    print("TS - Melhor solução:", melhor_solucao_ts)
    print("TS - Custo do melhor caminho:", menor_ts[-1])
    