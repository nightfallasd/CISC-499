import main
import importlib
import build

"""
This file runs the algorithm for several times, then find the average
"""

repeat = 20
totalSum = 0
best_result = 99999999
convergence = []
average_convergence = []

for i in range(repeat):
    result, dominance = main.runNGA()
    convergence.append(dominance)
    totalSum += result
    if result < best_result:
        best_result = result
    print("\nThe result in the ", i + 1, " run is: ", result, "\n")
    print("\nThe best result in the ", i + 1, " run is: ", best_result, "\n")
    importlib.reload(build)
for j in range(len(convergence[0])):
    total = 0
    for k in range(len(convergence)):
        total += convergence[k][j]
    average_convergence.append(total/repeat)

print("The average result for ", repeat, " runs is: ", totalSum / repeat)
print("The best result for ", repeat, " runs is: ", best_result)
print("The diversity of population as generation grow:", average_convergence)