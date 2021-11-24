import timeit
from brute_force import BruteForce as BF
from algoritmo_genetico import GeneticAlgoritm as GA
from utils import Utils

def testar_forca_bruta(distancias):
    start = timeit.default_timer()
    bf = BF(distancias)
    m_caminho, m_custo = bf.shortest_path()
    custo_forca_bruta = timeit.default_timer() - start
    
    return custo_forca_bruta, m_custo, m_caminho

def testar_algoritmo_genetico(distancias, quant_populacao, geracoes, prob_mutacao):
    start = timeit.default_timer()
    ag = GA(distancias)
    m_caminho, m_custo = ag.search_min_way(quant_populacao, geracoes, prob_mutacao)
    custo_algoritmo_genetico = timeit.default_timer() - start
    
    return custo_algoritmo_genetico, m_custo, m_caminho

def testar(grafo, tamanho_populacao, geracoes, probabilidade_mutacao):
    distancias = Utils.get_distances(grafo)    
    custo_fb, m_custo_fb, m_caminho_fb = testar_forca_bruta(distancias)
    custo_ag, m_custo_ag, m_caminho_ag = testar_algoritmo_genetico(distancias, tamanho_populacao, geracoes, probabilidade_mutacao)
    
    print(f'{custo_fb=}\n{custo_ag=}')
    if custo_fb < custo_ag:
        print(f'forca bruta foi mais rapido por {custo_ag-custo_fb}\n')
    else:
        print(f'algoritmo genetico foi mais rapido por {custo_fb-custo_ag}\n')
    
    return custo_ag, custo_ag

def testar_grafos():
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

    return

def roda_de_teste(testes_totais, testes_por_valores, grafo, tamanho_populacao, geracoes, probabilidade_mutacao, cres_populacao, cres_geracao):
    distancias = Utils.get_distances(grafo) 
    
    total_cag = {}
    for i in range(testes_totais):
        cag = []
        for j in range(testes_por_valores):
            custo_ag, m_custo_ag, m_caminho_ag = testar_algoritmo_genetico(distancias, tamanho_populacao, geracoes, probabilidade_mutacao)
            cag.append((custo_ag, m_custo_ag, m_caminho_ag))
        
        total_cag[(tamanho_populacao, geracoes)] = cag
        tamanho_populacao += cres_populacao
        geracoes += cres_geracao
    
    # custo_fb, m_custo_fb, m_caminho_fb = testar_forca_bruta(distancias)
    # cfb = (custo_fb, m_custo_fb, m_caminho_fb)
    # return cfb, total_cag

    return [0, 0,['a']], total_cag

def main():
    grafo = open("input10x10-11.txt", "r")
    testes_totais = 5
    testes_por_valores = 10
    tamanho_populacao = 60
    geracoes = 270
    probabilidade_mutacao = 0.05
    cres_populacao = 6
    cres_geracao = 20
    custo_forca_bruta, custos_algoritmo_genetico = roda_de_teste(testes_totais, testes_por_valores, grafo, tamanho_populacao, geracoes, probabilidade_mutacao, cres_populacao, cres_geracao)
        
    grafo.close()

    print(f'Forca Bruta encontrou o caminho: {"-".join(custo_forca_bruta[2])} de peso {custo_forca_bruta[1]} em {custo_forca_bruta[0]}\n')
    print('Algoritmo genetico encontrou os caminhos:')

    for k,v in custos_algoritmo_genetico.items():
        for r in v:
            print(k, ':', r)
        print('')

if __name__ == "__main__":
    main()