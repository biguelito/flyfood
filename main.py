import timeit
from brute_force import BruteForce as BF

def forca_bruta(grafo):
    bf = BF()
    distance_dict = bf.get_distances(grafo)
    
    for k, v in distance_dict.items():
        print(k, ' = ', v)
    print('')

    short_path, short_cost = bf.shortest_path(distance_dict)
    print(short_path, short_cost)

    return


def main():
    grafo = open("input.txt", "r")

    start = timeit.default_timer()
    forca_bruta(grafo)
    print('custo forca bruta: ', timeit.default_timer() - start)



    grafo.close()
    return

if __name__ == "__main__":
    main()