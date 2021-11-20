import timeit
from brute_force import BruteForce as BF
from algoritmo_genetico import GeneticAlgoritm as GA
from utils import Utils

def forca_bruta(distancias):
    bf = BF(distancias)
    
    menor_caminho, menor_custo = bf.shortest_path()
    print('forca bruta: ', menor_caminho, menor_custo)

    return

def algoritmo_genetico(distances, quant_populacao, geracoes, prob_mutacao):
    ag = GA(distances)
    menor_caminho, menor_custo = ag.search_min_way(quant_populacao, geracoes, prob_mutacao)
    print('algoritmo genetico: ', menor_caminho, menor_custo)
    
    return

def testar(grafo, tamanho_populacao, geracoes, probabilidade_mutacao):
    distancias = Utils.get_distances(grafo)    

    start = timeit.default_timer()
    algoritmo_genetico(distancias, tamanho_populacao, geracoes, probabilidade_mutacao)
    custo_algoritmo_genetico = timeit.default_timer() - start

    start = timeit.default_timer()
    forca_bruta(distancias)
    custo_forca_bruta = timeit.default_timer() - start

    print(f'{custo_forca_bruta=}\n{custo_algoritmo_genetico=}')
    if custo_forca_bruta < custo_algoritmo_genetico:
        print(f'forca bruta foi mais rapido por {custo_algoritmo_genetico-custo_forca_bruta}\n')
    else:
        print(f'algoritmo genetico foi mais rapido por {custo_forca_bruta-custo_algoritmo_genetico}\n')
    return 

def main():
    grafo = open("input.txt", "r")
    print('testando com o grafo original')
    tamanho_populacao = 4
    geracoes = 7
    probabilidade_mutacao = 0.05
    testar(grafo, tamanho_populacao, geracoes, probabilidade_mutacao)
    grafo.close()

    grafo = open("input7x7-8.txt", "r")
    print('testando com grafo 7x7 com 8 cidades')
    tamanho_populacao = 20
    geracoes = 60
    probabilidade_mutacao = 0.05
    testar(grafo, tamanho_populacao, geracoes, probabilidade_mutacao)
    grafo.close()

    grafo = open("input10x10-11.txt", "r")
    print('testando com grafo 10x10 com 11 cidades')
    tamanho_populacao = 60
    geracoes = 300
    probabilidade_mutacao = 0.05
    testar(grafo, tamanho_populacao, geracoes, probabilidade_mutacao)
    grafo.close()

    # grafo = open("input10x10-13.txt", "r")
    # print('testando com grafo 10x10 com 13 cidades')
    # tamanho_populacao = 80
    # geracoes = 350
    # probabilidade_mutacao = 0.05
    # testar(grafo, tamanho_populacao, geracoes, probabilidade_mutacao)
    # grafo.close()


if __name__ == "__main__":
    main()