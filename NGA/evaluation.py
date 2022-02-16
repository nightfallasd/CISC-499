"""
This file evaluates fitness according to some benchmark functions in GA
Modified by Yizhou Xiao
"""


def f2(vector):
    fitness = 0
    for value in vector:
        fitness += value ** 2
    return fitness


'''
The following function evaluates the fitness for a single vector
'''


def evaluate(vector):
    return f2(vector)


'''
The following function evaluates the fitness for a list of vectors
'''


def evaluate_lst(population):
    fitness = []
    for vector in population:
        fitness.append(f2(vector))
    return fitness
