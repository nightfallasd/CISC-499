
import initialization
import evaluation
import parent_selection
import build

import offspring_selection
import reproduce

population_size = 125
dimension = 30
Range = [-32, 32]
tournament_size = 5
generation = 2000
parent_number = 20
mutation_rate = 0.9
m = 4
m0 = 4


def next_generation(size):
    # do the parent selection
    offspring_list = []
    for i in range(parent_number):
        #parent = parent_selection.tournament(size)
        parent = parent_selection.roulette()
        offspring1, offspring2 = reproduce.crossover(parent)

    # mutate two offsprings and add them into network
        offspring1 = reproduce.mutation(offspring1, Range[0], Range[1], mutation_rate)
        offspring2 = reproduce.mutation(offspring2, Range[0], Range[1], mutation_rate)
        offspring_list.append(offspring1)
        offspring_list.append(offspring2)
    for offspring in offspring_list:
        build.add(offspring)

    # do the offspring selection
    offspring_selection.remove_worst(parent_number*2)


def runNGA():
    population = initialization.initialization(dimension, Range[0], Range[1], population_size)
    # let the population loop through generation
    generation_number = 0
    for i in range(generation):
        generation_number += 1
        next_generation(tournament_size)
        if generation_number % 400 == 0:
            print("After", generation_number, "generations:")
            net = build.network.copy()
            duplicate = []

            # count how many individuals are the same in the population
            for j in range(population_size):
                count = 0
                for m in range(population_size):
                    if net[j].val == net[m].val:
                        count = count + 1
                duplicate.append(count)
                if count > population_size / 2:
                    break
            print(max(duplicate), "individuals in the population are the same")

            # print the best individual
            net.sort(key=lambda x: x.fitness, reverse=True)
            print("After", generation_number, "generation:")
            print("The best individual is:", net[0].id, ", val:", net[0].val)
            print("The result is:", 1 / net[0].fitness)
            print()
    return 1 / net[0].fitness
