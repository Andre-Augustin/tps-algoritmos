# Comparação de Algoritmos para o Problema do Caixeiro Viajante

Este projeto implementa e compara dois algoritmos para resolver o **Problema do Caixeiro Viajante (TSP)**: o **Algoritmo Genético (AG)** e a **Têmpera Simulada (TS)**. O objetivo é encontrar rotas entre um conjunto de cidades que minimizem a distância total percorrida.

O projeto está organizado em três arquivos principais de código. O arquivo `funcoes_auxiliares.py` contém funções para: gerar uma rota aleatória, trocar cidades, calcular o custo de um caminho e criar uma matriz de distâncias simétrica. Tais funções são usadas na main, para criar o grafo e principalmente pela TS. O arquivo `algoritmo_genetico.py` implementa o Algoritmo Genético, incluindo a criação da população, cálculo de fitness, seleção por torneio, crossover e mutação. Já o arquivo `tempera_simulada.py` implementa o algoritmo de Têmpera Simulada, controlando a aceitação de soluções piores e o resfriamento da temperatura.

O script `main.py` é responsável por executar os dois algoritmos, gerar uma matriz de distâncias para as cidades, acompanhar os custos e exibir gráficos comparativos. Ele mostra o custo médio e o melhor custo do Algoritmo Genético, assim como o custo por iteração e a melhor solução encontrada pela Têmpera Simulada. Além disso, imprime no console os melhores caminhos e seus respectivos custos.

É possível ajustar parâmetros como o número de cidades, número de gerações ou iterações, tamanho da população, probabilidade de crossover e mutação, temperatura inicial e taxa de resfriamento. Isso permite testar diferentes cenários e observar como cada algoritmo se comporta.
