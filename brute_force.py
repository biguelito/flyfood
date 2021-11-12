class BruteForce:
    def __init__(self, distances):
        self.vertices = list(distances.keys())
        self.distances = distances

        return

    def all_paths(self, vertices):
        """
        Metodo recursivo que retorna todas as permutacoes de uma .
        Segue a tecnica de dividir e conquistar, divindo a lista em listas menores
        e removendo um termo por vez, retornando recursivamente quando a quantidade 
        de termos é <= 1, constrindo todas as permutacoes
        Recebe:
            Uma lista contendo os vertices do grafo
        Retorna:
            Uma lista com sublistas, onde cada sublista é uma permutacao, exemplo:
            ['a', 'b', 'c'] resulta:
            [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a']]
        """
        if len(vertices) <= 1:
            return [vertices]

        path = []
        for i in range(len(vertices)):
            a = vertices[i]
            remain_vertices = vertices[:i] + vertices[i+1:]

            for poss in self.all_paths(remain_vertices):
                path.append([a] + poss)

        return path


    def shortest_path(self):
        """
        Metodo principal da classe, calcula o menor caminho do grafo, indo de R a R.
        Cria a lista de permutacoes com o metodo all_paths sem o ponto R, esse ponto 
        pode ser atribuido no final, reduzindo a pilha de recursao. Depois, calcula o
        custo de cada caminho e salva o menor custo e seu caminho.
        Recebe:
            Um dicionario, gerado pelo metodo get_distance
        Retorna:
            O menor caminho do grafo e seu custo
        """
        
        self.vertices.remove("R")
        sh_path = []
        sh_cost = float('inf')

        all_paths = self.all_paths(self.vertices)
        for path in all_paths:
            temp = 0

            for i in range(1, len(path)):
                temp += self.distances[path[i-1]][path[i]]
            temp += self.distances['R'][path[0]] + self.distances['R'][path[len(path)-1]]

            if temp < sh_cost:
                sh_cost = temp
                sh_path = path
        sh_path = ['R'] + sh_path + ['R']

        return sh_path, sh_cost

    
    