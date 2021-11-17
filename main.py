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

def comparar_custo(cfb,cag):
    print(f'\n\n{cfb=}\n{cag=}')
    if cfb < cag:
        print(f'forca bruta foi mais rapido por {cag-cfb}')
    else:
        print(f'algoritmo genetico foi mais rapido por {cfb-cag}')

    return

def main():
    grafo = open("input.txt", "r")

    distancias = Utils.get_distances(grafo)    

    start = timeit.default_timer()
    forca_bruta(distancias)
    custo_forca_bruta = timeit.default_timer() - start

    tamanho_populacao = 50
    geracoes = 100
    probabilidade_mutacao = 0.05
    start = timeit.default_timer()
    algoritmo_genetico(distancias, tamanho_populacao, geracoes, probabilidade_mutacao)
    custo_algoritmo_genetico = timeit.default_timer() - start

    comparar_custo(custo_forca_bruta, custo_algoritmo_genetico)

    grafo.close()

if __name__ == "__main__":
    main()