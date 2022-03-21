import random
import build

'''
This function would do single point crossover
'''


def crossover(parent1):
    # get the index of all the neighbour of parent1
    parent2_list = parent1.neighbour
    # select one neighbour as parent2
    parent2_id = random.choice(parent2_list)
    for i in build.network:
        if i.id == parent2_id:
            parent2 = i
    # do the single point crossover
    dimension = len(parent1.val)
    crossover_point = random.randint(0, dimension)
    offspring1_val = parent1.val[0:crossover_point] + parent2.val[crossover_point:dimension]
    offspring2_val = parent2.val[0:crossover_point] + parent1.val[crossover_point:dimension]

    return offspring1_val, offspring2_val


'''
This function do the single point mutation to the offspring
'''


def mutation(offspring, upper_range, lower_range, mutation_rate):
    if mutation_rate > random.random():
        index = random.randint(0, len(offspring) - 1)
        offspring[index] = random.uniform(upper_range, lower_range)
    return offspring
