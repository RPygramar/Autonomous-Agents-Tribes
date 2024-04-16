import math
import heapq

class Node:
    def __init__(self):
        self.heuristic = 0 # Heuristic
        self.parent_row = 0 # Parent node row index
        self.parent_col = 0 # Parent node column index
        self.start_cost = 0 # Cost from start to this node
        self.total_cost = float('inf') # Total cost of node ( start_cost + heuristic )

# GRID
ROW = 90
COL = 90

# Check if node is valid
def is_valid(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

def is_unblocked(grid, row, col):
    return grid[row][col] != -1

# Check if node is destination
def is_destination(row, col, destination):
    return row == destination[0] and col == destination[1]

# Calculate heuristic of each node (Euclidean distance)
def calculate_heuristic(row, col, destination):
    # return abs(row - destination[0]) + abs(col - destination[1])
    return ((row - destination[0]) ** 2 + (col - destination[1]) ** 2) ** 0.5

# Trace path from start to destination
def trace_path(node, destination):
    print('Path: ')
    path = []
    row = destination[0]
    col = destination[1]

    # Trace path from destination to start using parent cells
    while not (node[row][col].parent_row == row and node[row][col].parent_col == col):
        path.append((row, col))
        temp_row = node[row][col].parent_row
        temp_col = node[row][col].parent_col
        row = temp_row
        col = temp_col

    # Add start node to path
    path.append((row, col))

    # Reverse path from start to destination
    path.reverse()

    # Print path
    for i in path:
        print('->', i, end='')
    print()

    return path

# START ALGORITHM
def A_STAR(grid, start, destination):
    # Check if the source and destination are valid
    if not is_valid(start[0], start[1]) or not is_valid(destination[0], destination[1]):
        print('Start or destination is not valid ')
        return

    # Check if start and destination are unblocked
    if not is_unblocked(grid, start[0], start[1]) or not is_unblocked(grid, destination[0], destination[1]):
        print(start[0], start[1])
        print(destination[0], destination[1])
        print('Source or destination is blocked')
        return

    # Check if already at destination
    if is_destination(start[0], start[1], destination):
        print('Already at destination')
        if start == destination:
            return
        return destination

    # Initialize the closed list
    closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
    # Initialize the nodes
    nodes_list = [[Node() for _ in range(COL)] for _ in range(ROW)]

    # Initialize start node
    i = start[0]
    j = start[1]
    nodes_list[i][j].total_cost = 0
    nodes_list[i][j].start_cost = 0
    nodes_list[i][j].cost = 0
    nodes_list[i][j].parent_row = i
    nodes_list[i][j].parent_col = j

    # Initialize open list with start node
    open_list = []
    heapq.heappush(open_list, (0.0, i, j))

    # Flag if found destination
    found_destination = False

    while len(open_list) > 0:
        # Pop node with the smallest total cost from open list
        p = heapq.heappop(open_list)

        # Mark node as visited
        i = p[1]
        j = p[2]
        closed_list[i][j] = True

        # For each direction, check the successors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]

            if is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
                # If the successor is the destination
                if is_destination(new_i, new_j, destination):
                    # Set the parent of the destination node
                    nodes_list[new_i][new_j].parent_row = i
                    nodes_list[new_i][new_j].parent_col = j
                    print('Found destination')
                    # Trace and print the path from start to destination
                    
                    found_destination = True
                    return trace_path(nodes_list, destination)
                else:
                    # Calculate the new total_cost, start_cost and heuristic
                    start_new_cost = nodes_list[new_i][new_j].start_cost + 1
                    heuristic_new = calculate_heuristic(new_i, new_j, destination)
                    total_new_cost = start_new_cost + heuristic_new

                    # If node is not in open list or total_cost is smaller
                    if nodes_list[new_i][new_j].total_cost == float('inf') or nodes_list[new_i][new_j].total_cost > total_new_cost:
                        # Add the node to open list
                        heapq.heappush(open_list, (total_new_cost, new_i, new_j))
                        # Update node list
                        nodes_list[new_i][new_j].total_cost = total_new_cost
                        nodes_list[new_i][new_j].start_cost = start_new_cost
                        nodes_list[new_i][new_j].heuristic = heuristic_new
                        nodes_list[new_i][new_j].parent_row = i
                        nodes_list[new_i][new_j].parent_col = j

    if not found_destination:
        print('Failed to find destination node')

if __name__ == '__main__':
    # Define the grid (1 for unblocked, 0 for blocked)
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

    start = (1, 1)
    destination = (0, 0)

    A_STAR(grid, start, destination)