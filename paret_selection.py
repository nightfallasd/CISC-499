import random


def tournament(population,fitness,size):
    Index = list(range(len(population)))
    parent1_list = random.sample(Index,size)
    parent1_fit = float('inf')
    for i in parent1_list:
        if fitness[i] < parent1_fit:
            parent1_fit = fitness[i]
            parent1 = population[i]

    same_parent = True
    while same_parent:
        parent2_list = random.sample(Index,size)
        parent2_fit = float('inf')

        for j in parent2_list:
            if fitness[j] < parent2_fit:
                parent2_fit = fitness[j]
                parent2 = population[j]
        if parent1 != parent2:
            same_parent = False

    return parent1,parent2