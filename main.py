import initialization
import evaluation
import paret_selection

import offspring_selection
import reproduce

population_size = 100
dimension = 10
Range = [-100, 100]
tournament_size = 4
generation = 50


def next_generation(population, fitness):
    parent1, parent2 = paret_selection.tournament(population, fitness, tournament_size)
    #print(parent1, parent2)
    offspring1, offspring2 = reproduce.crossover(parent1, parent2)
    #print(offspring1, offspring2)
    offspring1 = reproduce.mutation(offspring1, Range[0], Range[1])
    offspring2 = reproduce.mutation(offspring2, Range[0], Range[1])
    #print(offspring1, offspring2)
    offspring = [offspring1, offspring2]
    offspring_fitness = evaluation.evaluate(offspring)
    population, fitness = offspring_selection.mu_plus_lambda(population, fitness, offspring, offspring_fitness)
    return population, fitness


def main():
    population = initialization.initializtion(dimension, Range[0], Range[1], population_size)
    #print(population)
    fitness = evaluation.evaluate(population)
    print(fitness)
    for i in range(generation):
        population, fitness = next_generation(population, fitness)
    #print(population)
    print(fitness)
    best_vector = []
    best_fitness = float('inf')
    for k in range(len(fitness)):
        if fitness[k] <= best_fitness:
            best_vector = population[k]
            best_fitness = fitness[k]
    print(best_fitness)
main()


