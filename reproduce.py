import random


def crossover(parent1, parent2):
    offspring1 = []
    offspring2 = []

    crossover_point = random.randint(0, len(parent1))

    offspring1 = parent1[0:crossover_point] + parent2[crossover_point:len(parent2)]
    offspring2 = parent2[0:crossover_point] + parent1[crossover_point:len(parent2)]

    return offspring1, offspring2


def mutation(offspring, upper_range, lower_range):
    index = random.randint(0, len(offspring) - 1)
    offspring[index] = random.uniform(upper_range, lower_range)
    return offspring
