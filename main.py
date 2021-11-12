import timeit
from brute_force import BruteForce as BF
from algoritmo_genetico import GeneticAlgoritm as GA
from utils import Utils

def forca_bruta(distancias):
    bf = BF(distancias)
    
    short_path, short_cost = bf.shortest_path()
    print(short_path, short_cost)

    return

def algoritmo_genetico(distances, quant_populacao, geracoes):
    ag = GA(distances)
    ag.search_min_way(quant_populacao, geracoes)
    

def sum(a,b):
    return a+b

def main():
    grafo = open("input.txt", "r")

    distancias = Utils.get_distances(grafo)    

    # start = timeit.default_timer()
    # forca_bruta(distancias)
    # print('custo forca bruta: ', timeit.default_timer() - start)

    start = timeit.default_timer()
    algoritmo_genetico(distancias, 4, 1)
    print('custo algoritmo genetico: ', timeit.default_timer() - start)

    grafo.close()

if __name__ == "__main__":
    main()