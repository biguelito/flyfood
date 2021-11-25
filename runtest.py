import timeit
from brute_force import BruteForce as BF
from algoritmo_genetico import GeneticAlgoritm as GA
from utils import Utils
from graphic import Graphic

class RunTest:
    
    def __init__(self, grafo) -> None:
        self.distancias = Utils.get_distances(grafo) 

        return

    def testar_forca_bruta(self):
        start = timeit.default_timer()
        bf = BF(self.distancias)
        m_caminho, m_custo = bf.shortest_path()
        custo_forca_bruta = timeit.default_timer() - start
        
        return custo_forca_bruta, m_custo, m_caminho

    def testar_algoritmo_genetico(self, quant_populacao, geracoes, prob_mutacao):
        start = timeit.default_timer()
        ag = GA(self.distancias)
        m_caminho, m_custo = ag.search_min_way(quant_populacao, geracoes, prob_mutacao)
        custo_algoritmo_genetico = timeit.default_timer() - start
        
        return custo_algoritmo_genetico, m_custo, m_caminho

    def testar(self, tamanho_populacao, geracoes, probabilidade_mutacao):   
        custo_fb, m_custo_fb, m_caminho_fb = self.testar_forca_bruta()
        custo_ag, m_custo_ag, m_caminho_ag = self.testar_algoritmo_genetico(tamanho_populacao, geracoes, probabilidade_mutacao)
        
        print(f'{custo_fb=}\n{custo_ag=}')
        if custo_fb < custo_ag:
            print(f'forca bruta foi mais rapido por {custo_ag-custo_fb}\n')
        else:
            print(f'algoritmo genetico foi mais rapido por {custo_fb-custo_ag}\n')
        
        return custo_ag, custo_ag

    def roda_de_teste(self, testes_totais, testes_por_valores, tamanho_populacao, geracoes, probabilidade_mutacao, cres_populacao, cres_geracao):
        
        total_cag = {}
        for i in range(testes_totais):
            cag = []
            for j in range(testes_por_valores):
                custo_ag, m_custo_ag, m_caminho_ag = self.testar_algoritmo_genetico(tamanho_populacao, geracoes, probabilidade_mutacao)
                cag.append((custo_ag, m_custo_ag, m_caminho_ag))
            
            total_cag[(tamanho_populacao, geracoes)] = cag
            tamanho_populacao += cres_populacao
            geracoes += cres_geracao
        
        # custo_fb, m_custo_fb, m_caminho_fb = testar_forca_bruta(self.distancias)
        # cfb = (custo_fb, m_custo_fb, m_caminho_fb)
        # return cfb, total_cag

        return [0, 0,['a']], total_cag

    def run(self):
        testes_totais = 2
        testes_por_valores = 5
        tamanho_populacao = 50
        geracoes = 280
        probabilidade_mutacao = 0.05
        cres_populacao = 4
        cres_geracao = 10
        custo_forca_bruta, custos_algoritmo_genetico = self.roda_de_teste(testes_totais, testes_por_valores, tamanho_populacao, geracoes, probabilidade_mutacao, cres_populacao, cres_geracao)
            
        print(f'Forca Bruta encontrou o caminho: {"-".join(custo_forca_bruta[2])} de peso {custo_forca_bruta[1]} em {custo_forca_bruta[0]}\n')
        print('Algoritmo genetico encontrou os caminhos:')

        # for k,v in custos_algoritmo_genetico.items():
        #     media_custo_caminho = sum(custo for a, custo, b in v)/len(v)
        #     media_custo_tempo = sum(tempo for tempo, a, b in v)/len(v)
        #     print(k, ':', media_custo_caminho, media_custo_tempo)
        #     print('')

        graphic = Graphic(custos_algoritmo_genetico)
        graphic.show()
