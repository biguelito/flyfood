import pandas as pd

class Graphic:
    def __init__(self, dict_ag, forca_bruta) -> None:
        self.ag = dict_ag
        # self.data_ag = {}
        self.data_ag_resume = {}
        self.indexes = []
        self.fb = forca_bruta

        return

    def treat_data_resume(self):
        self.data_ag_resume['melhor custo'] = []
        self.data_ag_resume['media de pesos'] = []
        self.data_ag_resume['prob. menor custo'] = []
        self.data_ag_resume['media de tempo'] = []

        for k,v in self.ag.items():
            self.data_ag_resume['media de pesos'].append(sum(custo for a, custo, b in v)/len(v))
            
            menor_custo = min(v, key=lambda x: x[1])[1]
            self.data_ag_resume['melhor custo'].append(menor_custo)
            
            ocorrencia_menor = sum(1 for a, custo, b in v if custo == self.fb[1])
            self.data_ag_resume['prob. menor custo'].append((ocorrencia_menor/len(v))*100)
            
            self.data_ag_resume['media de tempo'].append(sum(tempo for tempo, a, b in v)/len(v))
            
            self.indexes.append(k) 

        return

    def show_resume(self):
        print(f'Forca Bruta:\nTempo: {self.fb[0]} Peso: {self.fb[1]}\n')
        
        self.treat_data_resume()
        df = pd.DataFrame(self.data_ag_resume, index=self.indexes)
        print('Algoritmo Genetico:')
        print(df)

        return