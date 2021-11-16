import random

class GeneticAlgoritm:
    def __init__(self, distances):
        self.distances = distances
        self.genes = list(self.distances.keys())
        self.chromossome_size = len(self.genes)-1 # Removing initial city
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

    def adjust_fitness(self, fitness):
        t = 0
        r = []
        for f in fitness:
            t += f
            r.append(t)

        return r

    def search_min_way(self, population_size, generations, mutation_p, d=False):
        genes = list(self.distances.keys())
        genes.remove('R')
        population = []
        best_chro = [0, []]

        # Initial population
        while len(population) != population_size:
            chromossome = random.sample(genes, len(genes))
            if chromossome not in population:
                population.append(chromossome)
        
        for g in range(generations):
            new_population = []
            # print('generation', g)

            # Calculating fitness
            fitness = []
            best_fit = float('inf')
            best_chro = []
            for chro in population:
                fit = self.calc_fitness(chro)
                fitness.append(fit)
                if fit < best_fit:
                    best_fit = fit
                    best_chro = chro

            # print(f'{fitness=}\n{best_chro}')

            # Crossover
            for p in range(int(population_size/2)):
                population_set = list(range(len(population))) 
                # f1 = random.choice(population_set)
                # population_set.remove(f1)
                # f2 = random.choice(population_set)
                # population_set.remove(f2)

                # father1 = population[f1]
                # father2 = population[f2]
                # child1, child2 = self.crossover(father1, father2)                
                # population[f1] = child1
                # population[f2] = child2

                index_father1 = random.choices(population_set, weights=fitness, k=1)[0]
                population_set.remove(index_father1)
                fitness.pop(index_father1)

                index_father2 = random.choices(population_set, weights=fitness, k=1)[0]
                population_set.remove(index_father2)
                fitness.pop(index_father2)

                print(index_father1, index_father2, population_set)
                
                father1 = population.pop(index_father1)
                father2 = population.pop(index_father2)
                
                
                
                child1, child2 = self.crossover(father1, father2)
                new_population.append(child1)
                new_population.append(child2)
                

                # TODO: aplicar mutacao e desenvolver selecao

            #     print(f'{father1=} {child1=}\n{father2=} {child2=}\n')
    
            # print(f"best chromossome={best_chro}\ncost={1/best_chro[0]}")
        
            population = new_population[:]

        # TODO: implementar elitismo
        best_chro = ['R'] + best_chro + ['R'] 

        return best_chro, best_fit

