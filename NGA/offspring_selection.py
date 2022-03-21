
import build


def remove_worst(remove_number):
    # sort the net
    net = build.network.copy()
    net.sort(key=lambda x: x.fitness)
    # remove the ones with the worst fitness
    while remove_number != 0:
        build.remove(net[0].id)
        net.pop(0)
        remove_number -= 1

    # find all the vector have no neighbour
    no_neighbour = []
    for vector in build.network:
        if len(vector.neighbour) == 0:
            no_neighbour.append(vector)
    # relink them into the net
    while len(no_neighbour) != 0:
        build.remove(no_neighbour[0].id)
        build.add(no_neighbour[0].val)
        no_neighbour.pop(0)
