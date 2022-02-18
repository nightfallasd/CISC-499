import initialization
import evaluation
import parent_selection
import build

import offspring_selection
import reproduce

population_size = 100
dimension = 30
Range = [-100, 100]
tournament_size = 4
generation = 1000
m = 4
m0 = 4


def next_generation(size):
    # do the parent selection
    parent = parent_selection.tournament(size)

    offspring1, offspring2 = reproduce.crossover(parent)

    # mutate two offsprings and add them into network
    offspring1 = reproduce.mutation(offspring1, Range[0], Range[1])
    offspring2 = reproduce.mutation(offspring2, Range[0], Range[1])
    build.add(offspring1)
    build.add(offspring2)

    # do the offspring selection
    offspring_selection.remove_worst()


def main():
    population = initialization.initialization(dimension, Range[0], Range[1], population_size)
    # let the population loop through generation
    for i in range(generation):
        next_generation(tournament_size)

    # print the best individual
    net = build.network.copy()
    net.sort(key=lambda x: x.fitness, reverse=True)
    print("The best individual is:", net[0].id, ", val:", net[0].val)
    print("The result is:", 1 / net[0].fitness)


main()
