"""
This file initialize the BA network
"""

import random
import build

m0 = 4


def initialization(D, upper_range, lower_range, size):
    # Build the initial network
    build.init_net(upper_range, lower_range, D)
    # Add an element each time to the network
    for i in range(size - m0):
        ind = []
        # Get the value of the vector
        for j in range(D):
            ind.append(random.uniform(upper_range, lower_range))
        # Add this individual to the network
        build.add(ind)


# Test
if __name__ == '__main__':
    # Test initialization
    print("Test initialization")
    initialization(10, 100, -100, 100)
    for n in build.network:
        print("id:", n.id, ", neighbour:", n.neighbour, ", fitness:", n.fitness)
