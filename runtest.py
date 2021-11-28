import timeit
from brute_force import BruteForce as BF
from algoritmo_genetico import GeneticAlgoritm as GA
from utils import Utils
from graphic import Graphic

class RunTest:
    
    def __init__(self, grafo) -> None:
        self.distancias = Utils.get_distances(grafo) 
        self.total_cga = {}
        self.total_cbf = []
        self.graphic = Graphic()
        return

    def brute_force(self):
        start = timeit.default_timer()
        bf = BF(self.distancias)
        m_caminho, m_custo = bf.shortest_path()
        custo_forca_bruta = timeit.default_timer() - start
        
        self.total_cbf = [custo_forca_bruta, m_custo, m_caminho]
        return 

    def test_genetic_algoritm(self, quant_populacao, geracoes, prob_mutacao):
        start = timeit.default_timer()
        ga = GA(self.distancias)
        m_caminho, m_custo = ga.search_min_way(quant_populacao, geracoes, prob_mutacao)
        custo_algoritmo_genetico = timeit.default_timer() - start
        
        return custo_algoritmo_genetico, m_custo, m_caminho

    def genetic_algoritm(self, testes_totais, testes_por_valores, tamanho_populacao, geracoes, probabilidade_mutacao, cres_populacao, cres_geracao):
        
        total_cga = {}
        for i in range(testes_totais):
            cga = []
            for j in range(testes_por_valores):
                custo_ga, m_custo_ga, m_caminho_ga = self.test_genetic_algoritm(tamanho_populacao, geracoes, probabilidade_mutacao)
                cga.append((custo_ga, m_custo_ga, m_caminho_ga))
            
            total_cga[(tamanho_populacao, geracoes)] = cga
            tamanho_populacao += cres_populacao
            geracoes += cres_geracao
        
        self.total_cga = total_cga
        return 

    def resume_brute_force(self):
        self.graphic.show_brute_force(self.total_cbf)

    def resume_genetic_algoritm(self):
        self.graphic.show_genetic_algoritm(self.total_cga)
