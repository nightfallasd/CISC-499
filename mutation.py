"""
My colleciton of mutation methods

Student number:20090405
Student name:Zijian Lu
"""

# imports
import random

def permutation_swap (individual):
    """Mutate a permutation"""

    mutant = individual.copy()
    
    # student code starts
    #randomly choose to position for exchange
    change_position = random.sample(range(0,len(individual)),2)
    position1 = change_position[0]
    position2 = change_position[1]

    #swap the elements in the two position
    mutant[position1] = individual[position2]
    mutant[position2] = individual[position1]

   
    # student code ends
    
    return mutant


