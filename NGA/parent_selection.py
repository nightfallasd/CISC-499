'''
This function use tournament to select a parent
'''
def tournament(size):
    # randomly find some individual to join the tournament
    parent = []
    Index = list(range(len(build.network)))
    parent_list = random.sample(Index, size)
    # use the best individual in the list as parent.
    parent_fit = float('inf')
    for i in parent_list:
        if build.network[i].fitness < parent_fit:
            parent_fit = build.network[i].fitness
            parent = build.network[i]

    return parent
