import main
import importlib
import build

"""
This file runs the algorithm for several times, then find the average
"""

repeat = 50
totalSum = 0
best_result = 99999999

for i in range(repeat):
    result = main.runNGA()
    totalSum += result
    if result < best_result:
        best_result = result
    print("\nThe result in the ", i + 1, " run is: ", result, "\n")
    print("\nThe best result in the ", i + 1, " run is: ", best_result, "\n")
    importlib.reload(build)

print("The average result for ", repeat, " runs is: ", totalSum / repeat)
print("The best result for ", repeat, " runs is: ", best_result)
