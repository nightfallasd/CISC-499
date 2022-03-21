import random
import build

'''
This function use tournament to select a parent
'''


def tournament(size):
    # randomly find some individual to join the tournament
    parent = []
    Index = list(range(len(build.network)))
    parent_list = random.sample(Index, size)
    # use the best individual in the list as parent.
    parent_fit = float('inf')
    for i in parent_list:
        if build.network[i].fitness < parent_fit:
            parent_fit = build.network[i].fitness
            parent = build.network[i]

    return parent

"""
This function use roulette wheel to select parents
"""
def roulette():
    # generate a cumulative probability distribution fitness list
    cum_fitness = [0]
    for i in range(len(build.network)):
        fitness = build.network[i].fitness
        cum_fitness.append(fitness / build.sum_fitness + cum_fitness[-1])
    cum_fitness.pop(0)

    # select parents according to cumulative probability distribution fitness list
    selector = random.random()
    j = 0
    while cum_fitness[j] <= selector:
        j = j + 1
    return build.network[j]
