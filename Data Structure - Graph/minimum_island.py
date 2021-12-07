def minimum_island(grid):
    visited_land = set()
    lowest = float("inf")
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'L':
                current_coordinate = (i, j)
                land_count = explore(grid, current_coordinate, visited_land)
                if land_count > 0 and land_count < lowest:
                    lowest = land_count

    return lowest


def explore(grid, current, visited):
    i, j = current
    coordinate = f"{i},{j}"
    if (coordinate in visited):
        return 0

    visited.add(coordinate)

    count = 1
    for neighbor in my_neigbours(grid, i, j):
        count += explore(grid, neighbor, visited)

    return count


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
