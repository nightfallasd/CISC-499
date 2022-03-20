import random

'''
input: D: dimension of the vector, upper_range and lower_range : range of the vevtor, size: population size
output: population with certain vectors and each vector contains D dimension
'''


def initialization(D, upper_range, lower_range, size):
    population = []
    for i in range(size):
        population.append([])
        for j in range(D):
            population[i].append(random.uniform(upper_range, lower_range))
    return population

