"""
My collection of initialization methods for different representations

Student number:20090405
Student name:Zijian Lu
"""

#imports
import random

def permutation (pop_size, chrom_length):
    """initialize a population of permutation"""

    population = []
    # student code begin
    
    #set current size to zero
    current_size = 0

    #add random solution till reach the pop size
    while current_size < pop_size:
        random_solution = []
        #append random number in the range of chess board to get a random solution
        for i in range(chrom_length):
            random_solution.append(random.randint(0,chrom_length-1))
        #add random solution into the population
        population.append(random_solution)
        current_size += 1
        
    #student code end
    
    return population



