import random

"""
This function do the single point crossover
"""


def crossover(parent1, parent2):
    offspring1 = []
    offspring2 = []
    #choose a point to cross
    crossover_point = random.randint(0, len(parent1))
    #generate offspring
    offspring1 = parent1[0:crossover_point] + parent2[crossover_point:len(parent2)]
    offspring2 = parent2[0:crossover_point] + parent1[crossover_point:len(parent2)]

    return offspring1, offspring2

"""
This function would do single point mutation
"""
def mutation(offspring, upper_range, lower_range, mutation_rate):
    if random.random() <= mutation_rate:
        index = random.randint(0, len(offspring) - 1)
        offspring[index] = random.uniform(upper_range, lower_range)
    return offspring
