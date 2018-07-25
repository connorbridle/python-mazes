import random


# Chooses the newest visited cell in the list
def choose_newest_visited_cell(cell_list_length):
    return cell_list_length-1


# Size will always be an even square
def make_maze(size):
    height = size
    width = size
    grid = []
    cells = []
    # Generate a maze filled with blocked passages
    for x in range(height):
        grid.append([])
        for j in range(width):
            grid[x].append('#')

    # Cho0sing a random cell and adding it to the list
    # x, y = random.randint(0, width-1), random.randint(0, height-1)
    x, y = 0, 0
    cells.append([x, y])
    grid[y][x] = ' '

    # Loop through the list until it is empty
    while len(cells) > 0:
        frontiers = []
        index = choose_newest_visited_cell(len(cells)) # Chooses the last visited cell in the cells list
        x, y = cells[index]
        # Looking for potential neighbours
        if (x + 2) < width and grid[y][x + 2] == '#':
            frontiers.append([y, x + 2])
        if (x - 2) >= 0 and grid[y][x - 2] == '#':
            frontiers.append([y, x - 2])
        if (y + 2) < height and grid[y + 2][x] == '#':
            frontiers.append([y + 2, x])
        if (y - 2) >= 0 and grid[y - 2][x] == '#':
            frontiers.append([y - 2, x])
        print("X: " + str(x) + " Y: " + str(y))
        print(frontiers)

        # If neighbours were found
        if len(frontiers) > 0:
            # If found then carve a passage between the
            randomIndex = random.randint(0, len(frontiers)-1)
            fronty, frontx = frontiers[randomIndex]
            # Changes the cell between the neighbour cell and current cell to ' ' (carves the wall)
            grid[int((y + fronty) / 2)][int((x + frontx) / 2)] = ' '
            grid[fronty][frontx] = ' '
            # Add the chosen neighbour to the list
            cells.append([frontx, fronty])
            index = None
        else:
            # If not found remove the current cell from list
            cells.pop(index)

    # Print out the final maze
    for i in range(size):
        print(grid[i])


make_maze(16)