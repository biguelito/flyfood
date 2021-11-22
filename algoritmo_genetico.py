import random

class GeneticAlgoritm:
    def __init__(self, distances):
        self.distances = distances
        self.genes = list(self.distances.keys())
        self.genes.remove('R')
        self.chromossome_size = len(self.genes) # Removing initial city
        self.best_chro = []
        self.best_fit = float('inf')
        
        return

    def calc_fitness(self, chromossome):
        """
        Metodo que calcula o fitnees de um chromossomo da populacao
        Recebe um chromossomo como argumento
        Retorna seu fit, nesse caso, o custo desse caminho no grafo
        """
        fit = 0
        for i in range(1, len(chromossome)):
            fit += self.distances[chromossome[i-1]][chromossome[i]]
        fit += self.distances['R'][chromossome[0]] + self.distances['R'][chromossome[len(chromossome)-1]]
        
        return fit

    def crossover(self, father1, father2, step=1):
        """
        Metodo que realiza o crossover entre 2 chromossomos
        Divide-se os chromossos em 3 partes, nos mesmos pontos, e mantem a parte do meio
        de cada pai no seu filho. Depois tentamos inserir os genes do pai1 no filho2 e vice-versa
        a partir do 2 ponto de corte do pai no 2 ponto de corte no filho
        Recebe 2 chromossomos 
        Retorna 2 chromossomos
        """
        child1 = [0 for i in range(self.chromossome_size)]
        child2 = [0 for i in range(self.chromossome_size)]
        
        p1 = random.randrange(0,self.chromossome_size-1, step)
        p2 = random.randrange(p1+1,self.chromossome_size, step)

        child1[p1:p2] = father1[p1:p2]
        child2[p1:p2] = father2[p1:p2]
        child1pos, child2pos = p2,p2 

        for i in range(self.chromossome_size):
            pos = (p2+i) % self.chromossome_size
            
            if father1[pos] not in child2:
                child2[child2pos] = father1[pos]         
                child2pos = (child2pos + 1) % self.chromossome_size

            if father2[pos] not in child1:
                child1[child1pos] = father2[pos]         
                child1pos = (child1pos + 1) % self.chromossome_size

        return child1, child2

    def mutation(self, chromossome):
        """
        Metodo que realiza a mutacao em um chromossomo
        Divide o chromosso em 3 partes e inverte-se a parte do meio colocando
        ela no mesmo lugar
        Recebe 1 chromossomo
        Retorna 1 chromossomo
        """
        p1 = random.randrange(0,self.chromossome_size-1)
        p2 = random.randrange(p1,self.chromossome_size)

        mut = chromossome[p1:p2]
        mut.reverse()
        muted_chromossome = chromossome[:p1] + mut + chromossome[p2:]

        return muted_chromossome
        
    def elitism(self, population):
        """
        Metodo que realiza o elitismo
        Procura na populacao o pior chromossomo e substitui ele pelo
        melhor chromossomo da populacao anterior
        Recebe as listas de populacao e fitness
        Retorna uma populacao 
        """
        worst_fit = -1
        for i, chro in enumerate(population):
            fit = self.calc_fitness(chro)
            if fit > worst_fit:
                worst_fit = fit 
                worst_index = i
        
        population[worst_index] = self.best_chro

        return population

    def search_min_way(self, population_size, generations, mutation_p):
        """
        *OBS: UM NUMERO IMPAR DE {population_size} PODE INFLUENCIAR NEGATIVAMENTE O RESULTADO*
        Metodo que roda o algoritmo genetico
        Cria a 1 populacao aleatoriamente e inicia a evolucao das populacoes
        Calcula o fitness dos individuos atuais e inicia a renovacao da populacao
        Escolhe de dois em dois individuos, realiza o crossover entre eles e
        geram-se 2 novos individuos para todo par de pais
        Verifica a possibilidade de ocorrer uma mutacao em qualquer um desses 2
        novos individuos
        Apos renovar toda a populacao, é aplicado o elitismo
        Depois de um numero {generations} de geracoes, o metodo encerra
        Recebe o numero de individuos por populacao, a quantidade de geracoes e a porcentagem de mutacao
        Retorna o melhor chromossomo e seu melhor fit
        """
        population = []
        fitness = []

        # Initial population
        while len(population) != population_size:
            chromossome = random.sample(self.genes, len(self.genes))
            if chromossome not in population:
                population.append(chromossome)

        for g in range(generations):

            # Calculating fitness
            new_population = []
            fitness = []
            for chro in population:
                fit = self.calc_fitness(chro)
                fitness.append(fit)
                if fit < self.best_fit:
                    self.best_fit = fit
                    self.best_chro = chro

            # Crossover
            weight = fitness[:]
            for p in range(int(population_size/2)):
                population_set = list(range(len(population))) 

                # Chosing 2 fathers
                index_father1 = random.choices(population_set, weights=weight, k=1)[0]
                index_father2 = random.choices(population_set, weights=weight, k=1)[0]
                while index_father2 == index_father1:
                    index_father2 = random.choices(population_set, weights=weight, k=1)[0]
                father1, father2 = population[index_father1], population[index_father2]
                fit1, fit2 = weight[index_father1], weight[index_father2]
                
                child1, child2 = self.crossover(father1, father2)

                # Removing selected fathers
                population_set.remove(index_father1)
                population_set.remove(index_father2)
                population.remove(father1)
                population.remove(father2)
                weight.remove(fit1)
                weight.remove(fit2)

                # mutation
                if random.random() < mutation_p:
                    child1 = self.mutation(child1)
                if random.random() < mutation_p:
                    child2 = self.mutation(child2)

                new_population.append(child1)
                new_population.append(child2)

            population = self.elitism(new_population)

        self.best_chro = ['R'] + self.best_chro + ['R'] 

        return self.best_chro, self.best_fit
