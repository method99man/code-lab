# === Import required libraries === #
import pygame           # Library for graphics and window control
import numpy as np      # Library for efficient arrays
import time             # Time control (for sleep, delay)

# === Random number generator instance === #
rng = np.random.default_rng()   # Better/faster RNG than Python's built-in random

# === Constants === #
COLOR_BG = (10, 10, 10)                 # Background color (dark gray/black)
COLOR_ALIVE = (255, 255, 255)           # Alive cell color (white)
COLOR_ABOUT_TO_DIE = (177, 177, 240)    # Cell die in next cycle (violet)

ROWS = 40                               # Number of rows (grid height in cells)
COLS = 60                               # Number of columns (grid width in cells)
CELL_SIZE = 10                          # Size of each cell

# === Initialize grid with random 0s (dead) and 1s (alive) === #
def init():
    matrix = rng.integers(2, size=(ROWS,COLS))      # Create 2D array of shape (ROWS x COLS) with random 0s or 1s
    return matrix    

# === Function to create an empty (all-dead) grid of same shape === #
def emptyArray(cells):
    return np.zeros((cells.shape[0], cells.shape[1]), dtype=int)    # Same shape, filled with 0s

# === Draw cells to the screen === #
def update(screen, cells, size):
    updateCells = emptyArray(cells)     # Create new empty grid for next generation

    # Loop over every cell in the grid using NumPy's efficient indexing
    for row, col in np.ndindex(cells.shape):
            # Count neighbors in a 3x3 area centered on current cell, subtract current cell itself
            cellNeighbours = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row][col]
            color = COLOR_BG    # Default: cell is dead, so background color

            # Game of Life rules
            if(cells[row][col] == 1):   # If cell is alive
                if cellNeighbours == 2 or cellNeighbours == 3:
                    updateCells[row][col] = 1       # Cell survives
                    color = COLOR_ALIVE             # Color as alive
                else:
                    color = COLOR_ABOUT_TO_DIE      # Dying color for visual feedback
            else:   # If cell is dead
                if cellNeighbours == 3:
                    updateCells[row][col] = 1       # Cell becomes alive
                    color = COLOR_ALIVE             # Color as alive

            # Draw the current cell as a rectangle on the screen
            pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))
    return updateCells      # Return updated grid for the next frame

# === Main application logic === #
def main():
    pygame.init()   # Initialize all pygame modules
    screen = pygame.display.set_mode((COLS * CELL_SIZE, ROWS * CELL_SIZE))  # Set window size
    pygame.display.set_caption("John Conway's Game of Life")    # Window title
    running = True  # State of simulation (paused or running)

    random_matrix = init()  # First generation: random alive/dead grid

    # === Main loop === #
    while True:
        # === Handle events === #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Handle window close
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                 # SPACE toggles simulation running/paused
                    running = not running
                    update(screen,random_matrix,CELL_SIZE)      # Redraw immediately
                    pygame.display.update()
                if event.key == pygame.K_BACKSPACE:             # BACKSPACE clears grid
                    random_matrix = emptyArray(random_matrix)   # Clear all cells
                    update(screen,random_matrix,CELL_SIZE)      # Redraw
                    pygame.display.update()

            # === Mouse interaction: left click to place live cell === #
            
            if pygame.mouse.get_pressed()[0]:                   # Left mouse button pressed
                pygame.event.set_grab(True)                     # Lock the mouse inside the Pygame window
                pygame.mouse.set_visible(False)                 # Hide the mouse cursor
                pos = pygame.mouse.get_pos()                    # Get mouse position in pixels
                col = pos[0] // CELL_SIZE                       # Convert X coordinate from pixels to cell column index
                row = pos[1] // CELL_SIZE                       # Convert Y coordinate from pixels to cell row index
                
                # Ensure the calculated row and col are within grid bounds
                if 0 <= row < ROWS and 0 <= col < COLS:
                    random_matrix[row,col] = 1                      # Convert to grid coords and set to alive
                    update(screen,random_matrix,CELL_SIZE)          # Redraw
                    pygame.display.update()
                pygame.event.set_grab(False)                        # Release mouse lock after click
            else:
                pygame.event.set_grab(False)                        # Ensure mouse is not locked if not pressing
                pygame.mouse.set_visible(True)                      # Make the mouse cursor visible again
                
        screen.fill(COLOR_BG)   # Clear entire screen before drawing next frame

        # === Main update: apply rules and draw === #
        if running:
            random_matrix = update(screen,random_matrix,CELL_SIZE)  # Update grid & draw
            pygame.display.update()                                 # Refresh the window
        
        time.sleep(0.01)                                            # Short delay to reduce CPU usage

# === Run main function if script is executed === #
if __name__ == '__main__':
    main()