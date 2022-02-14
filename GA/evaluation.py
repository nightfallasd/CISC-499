def f2(vector):
    fitness = 0
    for value in vector:
        fitness += value ** 2
    return fitness




def evaluate(population):
    fitness = []
    for vector in population:
        fitness.append(f2(vector))
    return fitness



