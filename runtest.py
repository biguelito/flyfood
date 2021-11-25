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

    # def testar(self, tamanho_populacao, geracoes, probabilidade_mutacao):   
    #     custo_fb, m_custo_fb, m_caminho_fb = self.testar_forca_bruta()
    #     custo_ag, m_custo_ag, m_caminho_ag = self.testar_algoritmo_genetico(tamanho_populacao, geracoes, probabilidade_mutacao)
        
    #     print(f'{custo_fb=}\n{custo_ag=}')
    #     if custo_fb < custo_ag:
    #         print(f'forca bruta foi mais rapido por {custo_ag-custo_fb}\n')
    #     else:
    #         print(f'algoritmo genetico foi mais rapido por {custo_fb-custo_ag}\n')
        
    #     return custo_ag, custo_ag

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
        
        custo_fb, m_custo_fb, m_caminho_fb = self.testar_forca_bruta()
        cfb = (custo_fb, m_custo_fb, m_caminho_fb)
        return cfb, total_cag

        return [0, 0,['a']], total_cag

    def run(self, 
            testes_totais, 
            testes_por_valores, 
            tamanho_populacao, 
            geracoes, 
            probabilidade_mutacao,
            cres_populacao, 
            cres_geracao
        ):
        
        self.custo_forca_bruta, self.custos_algoritmo_genetico = self.roda_de_teste(testes_totais, testes_por_valores, tamanho_populacao, geracoes, probabilidade_mutacao, cres_populacao, cres_geracao)
            
        self.graphic = Graphic(self.custos_algoritmo_genetico, self.custo_forca_bruta)

        return

    def resume(self):
        self.graphic.show_resume()