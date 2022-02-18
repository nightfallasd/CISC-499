"""
This file builds the BA network
Written by Yizhou Xiao
"""

import evaluation
import random

# This global variable represents the id of the last individual added into the network
id = 0
# This global variable represents the network
network = []
# This global variable represents the connection situations of all individuals
connection = []
# This global variable represents the sum of fitness of all individuals
sum_fitness = 0
# Modify the following variables to change the configure of the network
m = 4
m0 = 4

'''
The following function builds the initial network, with m0 individuals in the network
This m0 individuals are fully connected
val and fitness are the value and fitness of this m0 individuals
'''


def init_net(upper_range, lower_range, D):
    global sum_fitness
    # Get the value of the initial individuals
    val = []
    for i in range(m0):
        val.append([])
        for j in range(D):
            val[i].append(random.uniform(upper_range, lower_range))
    indlst = []
    for i in range(m0):
        indlst.append(i)
    # Calculate the fitness
    fitness = evaluation.evaluate_lst(val)
    # Add m0 individuals to the network
    for j in range(m0):
        # Find its neighbour
        neighbour_j = indlst.copy()
        neighbour_j.remove(j)
        sum_fitness += fitness[j]
        # Append it to the network
        network.append(Ind(val[j], neighbour_j, fitness[j]))
        # Record it to the connection situation
        for k in neighbour_j:
            if k > j:
                connection.append((j, k))


'''
The following function adds a new individual into the network
The parameter val is a vector while neighbour represents its neighbour
'''


def add(val):
    global sum_fitness
    # Decides its neighbour
    neighbour = []
    choose = network.copy()
    sum_fitness_lst = sum_fitness
    for i in range(m):
        rand_n = random.uniform(0, sum_fitness_lst)
        # Decide the area of which individual it falls
        for j in choose:
            rand_n -= j.fitness
            if rand_n <= 0:
                # It falls in this individual. Record it
                neighbour_choose = j
                # Append it to neighbour
                neighbour.append(j.id)
                j.neighbour.append(id)
                break
        # Remove the chosen neighbour from the list
        choose.remove(neighbour_choose)
        sum_fitness_lst -= neighbour_choose.fitness
    # Calculate its fitness
    fitness_val = evaluation.evaluate(val)
    # Append it to the network
    network.append(Ind(val, neighbour, fitness_val))
    # Update the sum of fitness
    sum_fitness += fitness_val
    # Record it to the connection situation
    for j in neighbour:
        connection.append((id - 1, j))


'''
The following function removes an individual from the network
The parameter r_id represents the id of that individual
'''


def remove(r_id):
    global sum_fitness
    # Initialize
    remove_i = -1

    for i in network:
        # Update neighbour of each individuals
        for k in i.neighbour:
            if k == r_id:
                i.neighbour.remove(k)
        if i.id == r_id:
            # Record this individual
            remove_i = i
    # Update the sum of fitness

    sum_fitness -= remove_i.fitness
    # Remove this individual
    network.remove(remove_i)
    # Update the connection situation
    remove_j = []
    for j in connection:
        if (j[0] == r_id) or (j[1] == r_id):
            remove_j.append(j)
    for q in remove_j:
        # Remove the lines
        connection.remove(q)


'''
The following class defines each individual
val represents the value of this vector
neighbour represents the other individual which are connected with this individuals
degree represents the degree of this individual
fitness represents the fitness of this individual
'''


class Ind:
    def __init__(self, val, neighbour, fitness):
        global id
        # Assign this id to this individual
        self.id = id
        # Add 1 to the global id
        id += 1
        self.val = val
        self.neighbour = neighbour
        self.fitness = fitness


# Test
if __name__ == '__main__':
    # Test init_net
    print("Test init_net")
    init_net(10, -10, 10)
    for n in network:
        print("id:", n.id, ", val:", n.val, ", neighbour:", n.neighbour, ", fitness:", n.fitness)
    print("Total connection situation: ", connection)
    print("Sum of fitness: ", sum_fitness)

    # Test add
    print("Test add")
    add([5, 6])
    for n in network:
        print("id:", n.id, ", val:", n.val, ", neighbour:", n.neighbour, ", fitness:", n.fitness)
    print("Total connection situation: ", connection)
    print("Sum of fitness: ", sum_fitness)

    # Test remove
    print("Test remove")
    remove(4)
    for n in network:
        print("id:", n.id, ", val:", n.val, ", neighbour:", n.neighbour, ", fitness:", n.fitness)
    print("Total connection situation: ", connection)
    print("Sum of fitness: ", sum_fitness)

    print("Test remove")
    remove(1)
    for n in network:
        print("id:", n.id, ", val:", n.val, ", neighbour:", n.neighbour, ", fitness:", n.fitness)
    print("Total connection situation: ", connection)
    print("Sum of fitness: ", sum_fitness)
