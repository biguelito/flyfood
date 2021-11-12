import random

class GeneticAlgoritm:
    def __init__(self, distances):
        self.distances = distances
        self.genes = list(self.distances.keys())
        self.chromossome_size = len(self.genes)-1
        return

    def calc_fitness(self, chromossome):
        fit = 0
        for i in range(1, len(chromossome)):
            fit += self.distances[chromossome[i-1]][chromossome[i]]
        fit += self.distances['R'][chromossome[0]] + self.distances['R'][chromossome[len(chromossome)-1]]
        
        return 1/fit

    def crossover(self, father1, father2, step=1):
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

    def stop_if(self):
        pass

    def search_min_way(self, population_size, generations):
        genes = list(self.distances.keys())
        genes.remove('R')
        population = []
        best_chro = [0, []]

        # Initial population
        for i in range(population_size):
            chromossome = random.sample(genes, len(genes))
            population.append(chromossome)
        print(population)
        
        for g in range(generations):

            fitness = []
            for chro in population:
                fit = self.calc_fitness(chro)
                fitness.append([fit, chro])
            best_chro = max(fitness, key=lambda x: x[0])
            
            # TODO: self.stop_if()

            for p in range(int(population_size/2)):
                population_set = list(range(population_size))
                population_set.remove(random.choice(population_set))
                print(population_set)

                # child1, child2 = self.crossover(population[0], population[1])                

        return 

