def get_second(fit_info):
    return fit_info[1]


def mu_plus_lambda(population, population_fitness, offspring, offspring_fitness):
    population_offspring = population + offspring
    population_offspring_fitness = population_fitness + offspring_fitness
    PopWithFit = []
    for i in range(len(population_offspring)):
        PopWithFit.append([population_offspring[i], population_offspring_fitness[i]])

    PopWithFit.sort(key=get_second)
    NewPopWithFit = PopWithFit[0:len(population)]

    new_population = []
    new_fitness = []

    for individual in NewPopWithFit:
        new_population.append(individual[0])
        new_fitness.append(individual[1])

    return new_population, new_fitness
