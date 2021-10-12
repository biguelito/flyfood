class BruteForce:
    def getDistances(self, file):
        dictDistance = {}
        matrix = []
        m, n = map(int, file.readline().split())
        for i in range(m):
            x = list(file.readline().split())

            for j in range(n):
                if x[j] != '0':
                    matrix.append((x[j], i, j))

        for touple in matrix:
            p, px, py = touple
            dictDistance[p] = {}

            for near in matrix:
                if touple == near:
                    continue

                p2, px2, py2 = near
                # |px - px2| + |py - py2|
                dictDistance[p][p2] = (abs(px - px2) + abs(py - py2))

        return dictDistance

    def possibilites(self, v):
        if len(v) <=1:
            yield v
        else:
            for perm in self.possibilites(v[1:]):
                for i in range(len(v)):
                    yield perm[:i] + v[0:1] + perm[i:]

    def shortestpath(self, distance_matrix):
        vertices = list(distance_matrix.keys())
        vertices.remove("R")
        sh_path = []
        sh_cost = float('inf')

        allpaths = self.possibilites(vertices)
        # print(allpaths)
        for n in allpaths:
            temp = 0

            for i in range(1, len(n)):
                temp += distance_matrix[n[i-1]][n[i]]
            temp += distance_matrix['R'][n[0]] + distance_matrix['R'][n[len(n)-1]]

            if temp < sh_cost:
                sh_cost = temp
                sh_path = n
        sh_path = ['R'] + sh_path + ['R']

        return sh_path, sh_cost

    
    