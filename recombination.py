"""
My collection of recombination methods

Student number:20090405
Student name:Zijian Lu
"""

#imports
import random

def permutation_cut_and_crossfill (parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""

    offspring1 = []
    offspring2 = []
    
    # student code begin
    #randomly select a crossover point
    crossover_point = random.randint(0,len(parent1))

    #generate an offspring by get the part before the crossover point from parent1 and get the part after the crossover point from parent2
    offspring1 = parent1[0:crossover_point]+parent2[crossover_point:len(parent2)]
    #generate another offspring by get the part before the crossover point from parent2 and get the part after the crossover point from parent1
    offspring2 = parent2[0:crossover_point]+parent1[crossover_point:len(parent2)]
                
    # student code end
    
    return offspring1, offspring2


