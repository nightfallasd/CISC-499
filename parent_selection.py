"""
My collection of parent selection methods

Student number:20090405
Student name:Zijian Lu
"""

# imports
import random



def MPS(fitness, mating_pool_size):
    """Multi-pointer selection (MPS)"""

    selected_to_mate = []

    # student code starts
    cumulative_fitness = []
    cumulative_sum = 0

    #get the sum of fitness
    fitness_sum = sum(fitness)

    #calculate the cumulative fitness for each item
    for i in range(len(fitness)):
        cumulative_sum += fitness[i]
        cumulative_fitness.append(cumulative_sum/fitness_sum)
    
    current_member = i = 0

    #set a pointer
    pointer = random.uniform(0,1/mating_pool_size)

    #add the parents until reach the size of math pool
    while current_member < mating_pool_size:

        #select the parents according to the pointer
        while pointer < cumulative_fitness[i]:
            selected_to_mate.append(i)
            pointer = pointer + 1/mating_pool_size
            current_member = current_member + 1
        i = i + 1

    # student code ends
    
    return selected_to_mate


def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement"""

    selected_to_mate = []

    # student code starts
    current_member = 0

    #loop until there is enough member in mate pool
    while current_member < mating_pool_size:

        #get the index of the tournament
        tournament_index = random.sample(range(0, len(fitness)),tournament_size)
        tournament_fitness = []

        #get the fitness of the value in tournamnet index
        for i in tournament_index:
            tournament_fitness.append(fitness[i])

        #find the best one and add it into mate pool
        best_fitness = max(tournament_fitness)
        best_index = tournament_fitness.index(best_fitness)
        selected_to_mate.append(tournament_index[best_index])
        current_member += 1
    # student code ends
    
    return selected_to_mate


def random_uniform (population_size, mating_pool_size):
    """Random uniform selection"""

    selected_to_mate = []

    # student code starts
    #randomly select some parents from the population
    selected_to_mate = random.sample(range(0, population_size), mating_pool_size)

    # student code ends
    
    return selected_to_mate



