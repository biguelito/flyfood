class Utils:

    def __init__(self):
        pass

    def get_distances(file):
        """
        Metodo que calcula a distancia entre os pontos do grafo.
        Calcula a distancia entre os pontos como se fossem um plano cartesiano,
        subtraindo as coordenadas x e y dos pontos e somando sua diferenca.
        Dependendo da posicao dos termos o resultado pode sair negativo,
        basta pegar o valor absoluto para resolver isso
        > |px - px2| + |py - py2|
        Recebe:
            o conteudo do arquivo, onde está o grafo
        Retorna:
            Um dicionario contendo a distancia de um ponto para todos os outros, exemplo de item
            'D': {'A': 4, 'C': 2, 'R': 7, 'B': 5}
        """
        dictDistance = {}
        matrix = []
        vertices = []
        m, n = map(int, file.readline().split())
        for i in range(m):
            x = list(file.readline().split())

            for j in range(n):
                vertice = x[j]
                if vertice != '0':
                    matrix.append((vertice, i, j))
                    vertices.append(vertice)

        for touple in matrix:
            p, px, py = touple
            dictDistance[p] = {}

            for near in matrix:
                if touple == near:
                    continue

                p2, px2, py2 = near
                # |px - px2| + |py - py2|
                dictDistance[p][p2] = abs(px - px2) + abs(py - py2) 
        
        return dictDistance