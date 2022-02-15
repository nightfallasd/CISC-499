'''
return second value of a list.
'''
def get_second(fit_info):
    return fit_info[1]

'''
use mu_plus_lambda to complete the offspring selection. 
input: population and fitness of population, offspring and fitness of offspring
'''
def mu_plus_lambda(population, population_fitness, offspring, offspring_fitness):
    
    #combine the offspring and population
    population_offspring = population + offspring
    population_offspring_fitness = population_fitness + offspring_fitness
    
    #combine the whole population and its fitness
    PopWithFit = []
    for i in range(len(population_offspring)):
        PopWithFit.append([population_offspring[i], population_offspring_fitness[i]])
    
    #sort them and remove the individuals with worst fitness
    PopWithFit.sort(key=get_second)
    NewPopWithFit = PopWithFit[0:len(population)]

    new_population = []
    new_fitness = []
    
    #return the new populationa and fitness list
    for individual in NewPopWithFit:
        new_population.append(individual[0])
        new_fitness.append(individual[1])

    return new_population, new_fitness
