import pandas as pd

class Graphic:
    def __init__(self) -> None:
        self.data_ga_resume = {}
        self.indexes = []

        return

    def treat_data_resume(self, data_ga):
        self.data_ga_resume['melhor custo'] = []
        self.data_ga_resume['media de pesos'] = []
        self.data_ga_resume['prob. menor custo'] = []
        self.data_ga_resume['media de tempo'] = []

        for k,v in data_ga.items():
            self.data_ga_resume['media de pesos'].append(sum(custo for a, custo, b in v)/len(v))
            
            menor_custo = min(v, key=lambda x: x[1])[1]
            self.data_ga_resume['melhor custo'].append(menor_custo)
            
            ocorrencia_menor = sum(1 for a, custo, b in v if custo == menor_custo)
            self.data_ga_resume['prob. menor custo'].append((ocorrencia_menor/len(v))*100)
            
            self.data_ga_resume['media de tempo'].append(sum(tempo for tempo, a, b in v)/len(v))
            
            self.indexes.append(k) 

        return

    def show_genetic_algoritm(self, data_ga):
        self.treat_data_resume(data_ga)
        df = pd.DataFrame(self.data_ga_resume, index=self.indexes)
        print('Algoritmo Genetico:')
        print(df)

        return

    def show_brute_force(self, fb):
        print(f'\nForca Bruta:\nTempo: {fb[0]} Peso: {fb[1]}')
