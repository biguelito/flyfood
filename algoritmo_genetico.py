import random

class GeneticAlgoritm:
    def __init__(self, distances):
        self.distances = distances
        self.genes = list(self.distances.keys())
        self.chromossome_size = len(self.genes)-1 # Removing initial city
        self.best_chro = []
        self.best_fit = float('inf')
        
        return

    def calc_fitness(self, chromossome):
        fit = 0
        for i in range(1, len(chromossome)):
            fit += self.distances[chromossome[i-1]][chromossome[i]]
        fit += self.distances['R'][chromossome[0]] + self.distances['R'][chromossome[len(chromossome)-1]]
        
        return fit

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

    def mutation(self, chromossome):
        p1 = random.randrange(0,self.chromossome_size-1)
        p2 = random.randrange(p1,self.chromossome_size)

        mut = chromossome[p1:p2]
        mut.reverse()
        muted_chromossome = chromossome[:p1] + mut + chromossome[p2:]

        return muted_chromossome

    def stop_if(self):
        pass

    def elitism(self, population, fitness):
        worst_fit = max(fitness)
        worst_index = fitness.index(worst_fit)

        fitness[worst_index] = self.best_fit
        population[worst_index] = self.best_chro

        return population

    def search_min_way(self, population_size, generations, mutation_p, d=False):
        genes = list(self.distances.keys())
        genes.remove('R')
        population = []
        fitness = []

        # Initial population
        while len(population) != population_size:
            chromossome = random.sample(genes, len(genes))
            if chromossome not in population:
                population.append(chromossome)

        for g in range(generations):
            # print('generation', g)

            # Calculating fitness
            new_population = []
            fitness = []
            for chro in population:
                fit = self.calc_fitness(chro)
                fitness.append(fit)
                if fit < self.best_fit:
                    self.best_fit = fit
                    self.best_chro = chro

            # print(f'{fitness=}\n{best_chro}')

            # Crossover
            weight = fitness[:]
            for p in range(int(population_size/2)):
                population_set = list(range(len(population))) 

                index_father1 = random.choices(population_set, weights=weight, k=1)[0]
                index_father2 = random.choices(population_set, weights=weight, k=1)[0]
                while index_father2 == index_father1:
                    index_father2 = random.choices(population_set, weights=weight, k=1)[0]
                father1, father2 = population[index_father1], population[index_father2]
                fit1, fit2 = weight[index_father1], weight[index_father2]
                
                child1, child2 = self.crossover(father1, father2)
                new_population.append(child1)
                new_population.append(child2)

                population_set.remove(index_father1)
                population_set.remove(index_father2)
                population.remove(father1)
                population.remove(father2)
                weight.remove(fit1)
                weight.remove(fit2)

                if random.random() < mutation_p:
                    self.mutation(child1)

                if random.random() < mutation_p:
                    self.mutation(child2)

                # TODO: aplicar mutacao

            #     print(f'{father1=} {child1=}\n{father2=} {child2=}\n')
    
            # print(f"best chromossome={best_chro}\ncost={1/best_chro[0]}")
            
            population = self.elitism(new_population, fitness)

        self.best_chro = ['R'] + self.best_chro + ['R'] 

        return self.best_chro, self.best_fit
