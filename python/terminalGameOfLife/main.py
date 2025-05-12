import random, time, sys, os

# Grid dimensions
WIDTH = 20
HEIGHT = 20

# Representation of cell states: alive ("■") and dead (" ")
CELLSTATE = ["■", " "]

def gridInit():
    """
    Initializes the grid with random alive and dead cells.
    """
    return [[random.choice(CELLSTATE) for x in range(WIDTH)] for y in range(HEIGHT)]

def newBlankGrid():
    """
    Creates a blank grid filled with dead cells.
    """
    return [[CELLSTATE[1] for _ in range(WIDTH)] for _ in range(HEIGHT)]

def checkNeighbors(grid,x,y):
    """
    Counts the number of alive neighbors around the cell at (x, y).
    Does not wrap around the grid edges.
    """
    count = 0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx == 0 and dy == 0:
                continue    # Skip the cell itself
            nx = (x + dx) 
            ny = (y + dy) 

            # Check that neighbor coordinates are within the grid bounds
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
                if grid[ny][nx] == '■':     # Neighbor is alive
                    count += 1
    return count

def checkRules(grid, nextGrid, x, y, neighbors):
    """
    Applies Conway's Game of Life rules to determine the next state of a cell.
    """
    if grid[y][x] == "■" and neighbors in (2, 3):
        # Alive cell with 2 or 3 neighbors stays alive
        nextGrid[y][x] = CELLSTATE[0]
    elif grid[y][x] ==  CELLSTATE[1] and neighbors == 3:
        # Dead cell with exactly 3 neighbors becomes alive
        nextGrid[y][x] = CELLSTATE[0]
    else:
        # In all other cases, the cell dies or stays dead
        nextGrid[y][x] = CELLSTATE[1]

def drawGrid(grid):
    """
    Clears the terminal screen and prints the current grid state.
    """
    os.system('cls' if os.name == "nt" else 'clear')    # clear screen
    for row in grid:
        print(''.join(row))     # Print each row of the grid

# Main loop
grid = gridInit()   # Create initial random grid
while True:
    drawGrid(grid)      # Display the current generation
    nextGrid = newBlankGrid()     # Prepare an empty grid for the next generation

    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = checkNeighbors(grid, x, y)          # Count living neighbors
            checkRules(grid, nextGrid, x, y, neighbors)     # Apply the game rules

    grid = nextGrid
    try:
        time.sleep(1)       # Pause between frames
    except KeyboardInterrupt:
        print("Conway's Game of Life")      # Handle Ctrl+C gracefully
        sys.exit()
