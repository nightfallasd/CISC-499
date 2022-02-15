'''
Use a vector as input and return the result calucalte by function2
'''
def f2(vector):
    fitness = 0
    for value in vector:
        fitness += value ** 2
    return fitness



'''
Use population as input and return the fitness list that record the fitness of each individual
'''
def evaluate(population):
    fitness = []
    for vector in population:
        fitness.append(f2(vector))
    return fitness



