import initialization
import evaluation
import parent_selection

import offspring_selection
import reproduce

population_size = 100
dimension = 30
Range = [-100, 100]
tournament_size = 4
generation = 2000
parents_number = 20
mutation_rate = 0.9

"""
This function return the next generation of the population
"""
def next_generation(population, fitness):
    offspring_list = []
    offspring_fitness_list = []
    for i in range(parents_number):
        #choose the selection method

        parent1, parent2 = parent_selection.tournament(population, fitness, tournament_size)
        #parent1 = parent_selection.roulette(population, fitness)
        #parent2 = parent_selection.roulette(population, fitness)

        #do the crossover and mutation
        offspring1, offspring2 = reproduce.crossover(parent1, parent2)
        offspring1 = reproduce.mutation(offspring1, Range[0], Range[1],mutation_rate)
        offspring2 = reproduce.mutation(offspring2, Range[0], Range[1],mutation_rate)
        #evaluate new offspring
        offspring = [offspring1, offspring2]
        offspring_fitness = evaluation.evaluate(offspring)
        offspring_list = offspring_list + offspring
        offspring_fitness_list = offspring_fitness_list + offspring_fitness
    population, fitness = offspring_selection.mu_plus_lambda(population, fitness, offspring_list,
                                                             offspring_fitness_list)
    return population, fitness


def main():
    #generate population and fitness
    population = initialization.initialization(dimension, Range[0], Range[1], population_size)
    fitness = evaluation.evaluate(population)
    current_generation = 0
    
    for i in range(generation):
        current_generation += 1
        population, fitness = next_generation(population, fitness)
        if current_generation%500 == 0:
            best_fitness = 0
            best = []
            for k in range(len(fitness)):
                if fitness[k] >= best_fitness:
                    best_vector = population[k]
                    best_fitness = fitness[k]
                    best = population[k]
                    print(best)
                    print(1/best_fitness)


main()

