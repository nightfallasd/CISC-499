import main
import importlib
import build

"""
This file runs the algorithm for several times, then find the average
"""

repeat = 50
bestSum = 0

for i in range(repeat):
    result = main.runNGA()
    bestSum += result
    print("\nThe best result in the ", i + 1, " run is: ", result, "\n")
    importlib.reload(build)

print("The average result for ", repeat, " runs is: ", bestSum / repeat)
