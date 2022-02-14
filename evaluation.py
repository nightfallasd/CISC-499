"""
My collection of fitness evaluation methods

Student number:20090405
Student name:Zijian Lu
"""

#imports


def fitness_8queen (individual): 
    """Compute fitness of an invidual for the 8-queen puzzle (maximization)"""    

    fitness = 0
    # student code begin
    
    #set a list for unfit queen position
    not_fit = []
    
    #loop through each position for the queen
    for i in range(len(individual)):
        location = individual[i]

        #if it have not been marked as unfit queen
        if (i,location) not in not_fit:
            fit = True

            #loop through all the queen positions behind the current on to check whether there is a conflict
            for j in range(i+1,len(individual)):
                if individual[j] == location or abs(i-j) == abs(location - individual[j]):
                    
                    not_fit.append((j,individual[j]))
                    fit = False

            #if there is no conflict with other queen        
            if fit:
                fitness += 1
    # student code end
    
    return fitness




