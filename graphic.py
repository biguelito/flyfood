import pandas as pd

class Graphic:
    def __init__(self, dict_ag) -> None:
        self.ag = dict_ag

    def treat_data(self):
        pass

    def show(self):
        pddata = pd.DataFrame(self.ag)
        pddata.head().describe()
