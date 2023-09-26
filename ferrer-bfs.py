from collections import deque


# Helper function to check if a position is within the grid boundaries
def is_valid_position(x_coord, y_coord):
    return 0 <= x_coord < r and 0 <= y_coord < c


# Helper functions for each direction
def move_up(x_coord, y_coord):
    return x_coord - 1, y_coord


def move_left(x_coord, y_coord):
    return x_coord, y_coord - 1


def move_right(x_coord, y_coord):
    return x_coord, y_coord + 1


def move_down(x_coord, y_coord):
    return x_coord + 1, y_coord


# Get the initial and target positions
pacman_r, pacman_c = map(int, input().split())
food_r, food_c = map(int, input().split())

# Get the grid dimensions
r, c = map(int, input().split())

grid = []  # Initialize the grid

# Populate the grid
for _ in range(r):
    grid.append(list(input()))

queue = deque()  # Initialize the queue for BFS
nodes = []
explored_nodes = None

# Initialize the queue with the starting position and an empty route
queue.append([pacman_r, pacman_c, []])

while queue:
    current_x, current_y, route = queue.popleft()
    routes = route.copy()
    routes.append([current_x, current_y])

    nodes.append([current_x, current_y])

    if current_x == food_r and current_y == food_c:
        if explored_nodes is None:
            explored_nodes = routes
            break

    # Use helper functions to move in each direction
    for move_func in [move_up, move_left, move_right, move_down]:
        next_x, next_y = move_func(current_x, current_y)
        if is_valid_position(next_x, next_y) and grid[next_x][next_y] in ["-", "."]:
            grid[next_x][next_y] = '='
            queue.append([next_x, next_y, routes])

# Output the number of nodes
print(len(nodes))
for point in nodes:
    print(f"{point[0]} {point[1]}")

# Output the length of the answer route and the route itself
print(len(explored_nodes) - 1)
for point in explored_nodes:
    print(f"{point[0]} {point[1]}")
