import pandas as pd

class Graphic:
    def __init__(self, dict_ag, forca_bruta) -> None:
        self.ag = dict_ag
        self.data_ag = {}
        self.data_ag_resume = {}
        self.indexes = []
        self.fb = forca_bruta

        return

    def treat_data_resume(self):
        self.data_ag_resume['media custo caminho'] = []
        self.data_ag_resume['media custo tempo'] = []

        for k,v in self.ag.items():
            self.data_ag_resume['media custo caminho'].append(sum(custo for a, custo, b in v)/len(v))
            self.data_ag_resume['media custo tempo'].append(sum(tempo for tempo, a, b in v)/len(v))
            self.indexes.append(k) 

        return

    def show_resume(self):
        print(f'Forca Bruta:\nTempo: {self.fb[0]} Peso: {self.fb[1]}\n')
        
        self.treat_data_resume()
        df = pd.DataFrame(self.data_ag_resume, index=self.indexes)
        print(df)

        return