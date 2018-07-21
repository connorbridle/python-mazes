import numpy as np
import random


def create_grid(mheight, mwidth):
    test = [[0 for x in range(mwidth)] for y in range(mheight)]
    for x in range(0, mheight):
        for i in range(0, mwidth):
            test[x][i] = 1
    print(np.matrix(test))
    return test


myGrid = create_grid(10, 10)
myGrid[0][1] = 5

# This algorithm is a randomized version of Prim's algorithm.
#
# Start with a grid full of walls. Y
# Pick a cell, mark it as part of the maze. Add the walls of the cell to the wall list.
# While there are walls in the list:
    # Pick a random wall from the list. If only one of the two cells that the wall divides is visited, then:
        # Make the wall a passage and mark the unvisited cell as part of the maze.
        # Add the neighboring walls of the cell to the wall list.
#    Remove the wall from the list.


def start_prims_algorithm(wallGrid):
    # Pass in a grid full of walls (1's) and this function will return a matrix after prims algorithm
    chosenCell = random.randint(0, len(wallGrid))
    print("Just testing some repo stuff")

