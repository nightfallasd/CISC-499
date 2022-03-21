import random

'''
This function use tournament to select parents
'''
def tournament(population, fitness, size):
    # randomly choose some individuals to join the tournament
    Index = list(range(len(population)))
    parent1_list = random.sample(Index, size)
    parent1_fit = 0

    # find the best one in the tournament as parent 1
    for i in parent1_list:
        if fitness[i] > parent1_fit:
            parent1_fit = fitness[i]
            parent1 = population[i]

    # make sure parent 1 and parent2 are not the same or can not find new individuals
    same_parent = True
    count = 0
    while same_parent:
        parent2_list = random.sample(Index, size)
        parent2_fit = 0

        # find the best one as parent 2
        for j in parent2_list:
            if fitness[j] > parent2_fit:
                parent2_fit = fitness[j]
                parent2 = population[j]
        if parent1 != parent2:
            same_parent = False
        elif count >= 50:
            same_parent = False
        count += 1

    return parent1, parent2

'''
This function use roulette wheel to select parents
'''
def roulette(population, fitness):
    #generate a cumulative probability distribution fitness list
    cum_fitness = [0]
    total = sum(fitness)
    for i in fitness:
        cum_fitness.append( i/total + cum_fitness[-1])
    cum_fitness.pop(0)

    #select parents according to cumulative probability distribution fitness list
    selector = random.random()
    j = 0
    while cum_fitness[j] < selector:
        j = j + 1
    #return the target indvidual
    return population[j]
