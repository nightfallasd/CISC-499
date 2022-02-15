import random

'''
use population, fitness and tournament size to do the parent selection
'''
def tournament(population,fitness,size):
    
    #randomly choose some individuals to join the tournament
    Index = list(range(len(population)))
    parent1_list = random.sample(Index,size)
    parent1_fit = float('inf')
    
    #find the best one in the tournament as parent 1
    for i in parent1_list:
        if fitness[i] < parent1_fit:
            parent1_fit = fitness[i]
            parent1 = population[i]
    
    #make sure parent 1 and parent2 are not the same or can not find new individuals 
    same_parent = True
    count = 0
    while same_parent:
        parent2_list = random.sample(Index,size)
        parent2_fit = float('inf')
        
        #find the best one as parent 2
        for j in parent2_list:
            if fitness[j] < parent2_fit:
                parent2_fit = fitness[j]
                parent2 = population[j]
        if parent1 != parent2:
            same_parent = False
        elif count >= 50:
            same_parent = False
        count += 1

    return parent1,parent2
