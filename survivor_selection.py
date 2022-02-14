"""
My collection of survivor selection methods

Student number:20090405
Student name:Zijian Lu
"""

#imports
import random

#This function would retunrn the second value
def get_second(fit_info):
    return fit_info[1]

def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    """mu+lambda selection"""
    population = []
    fitness = []

    # student code starts
    pop = []
    #combine all the current population and offspring
    pop = current_pop.copy() + offspring.copy()
    fit = []
    #combine all the current population fitness and offspring fitness,then add an index
    for i in range(len(current_fitness)+ len(offspring)):
        if i < len(current_fitness):
            fit.append((i,current_fitness[i]))
        else:
            fit.append((i,offspring_fitness[i-len(current_fitness)]))

    #eliminate to proper size by sorting them and removing the relatively unsatisfactory members
    fit.sort(key=get_second,reverse=True)
    fit_update = fit[0:len(current_fitness)]

    #append them to the population list and fitness list
    for j in fit_update:
        population.append(pop[j[0]])
        fitness.append(j[1])
        
    # student code ends
    
    return population, fitness


def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    """replacement selection"""

    population = []
    fitness = []

    # student code starts
    fit= []

    #add the index for curret fitness
    for i in range(len(current_fitness)):
        if i < len(current_fitness):
            fit.append((i,current_fitness[i]))

    #remove the wrost n current populations, n is the number of offspring
    fit.sort(key=get_second,reverse=True)
    fit_update = fit[0:len(current_fitness)-len(offspring_fitness)]

    #append them to the population list and fitness list
    for j in fit_update:
        population.append(current_pop[j[0]])
        fitness.append(j[1])

    #combine with the offspring and its fitness
    population = population + offspring 
    fitness = fitness + offspring_fitness
    # student code ends
    
    return population, fitness


def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    """random uniform selection"""
    population = []
    fitness = []

    # student code starts
    pop = []
    #combine all the current population and offspring
    pop = current_pop.copy() + offspring.copy()
    fit = []
    #combine all the current population fitness and offspring fitness,then add an index
    for i in range(len(current_fitness)+ len(offspring)):
        if i < len(current_fitness):
            fit.append((i,current_fitness[i]))
        else:
            fit.append((i,offspring_fitness[i-len(current_fitness)]))
            
    #randomly pick the population from pop
    random_index = random.sample(range(0,len(current_fitness)+len(offspring_fitness)),len(current_fitness))

    #append them into the popualtion list and fitness list
    for i in random_index:
        population.append(pop[i])
        fitness.append(fit[i][1])
    # student code ends
    
    return population, fitness



