"""
https://structy.net/problems/island-count
Write a function, island_count, that takes in a grid containing Ws and Ls.
W represents water and L represents land. 
The function should return the number of islands on the grid. 
An island is a vertically or horizontally connected region of land.
"""


def island_count(grid):
    visited_land = set()
    number_of_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L':
                current_coordinate = (i, j)
                if(explore(grid, current_coordinate, visited_land)):
                    number_of_islands += 1

    return number_of_islands


def explore(grid, current, visited):
    i, j = current
    coordinate = f"{i},{j}"
    if (coordinate in visited):
        return False

    visited.add(coordinate)

    for neighbor in my_neigbours(grid, i, j):
        explore(grid, neighbor, visited)

    return True


def my_neigbours(grid, i, j):
    neighbours = []
    if i > 0:
        top_neighbour = grid[i-1][j]
        if top_neighbour == 'L':
            neighbours.append((i-1, j))

    if i+1 < len(grid):
        bottom_neighbour = grid[i+1][j]
        if bottom_neighbour == 'L':
            neighbours.append((i+1, j))

    if j > 0:
        left_neighbour = grid[i][j-1]
        if left_neighbour == 'L':
            neighbours.append((i, j-1))

    if j+1 < len(grid[0]):
        right_neighbour = grid[i][j+1]
        if right_neighbour == 'L':
            neighbours.append((i, j+1))

    return neighbours


grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]
