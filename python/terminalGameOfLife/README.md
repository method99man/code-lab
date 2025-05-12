## Conway's Game of Life – Terminal Version
A simple terminal-based implementation of Conway's Game of Life, written in Python.
The simulation displays cells evolving over time according to basic rules of life and death, with live cells shown as "■" and dead cells as spaces.

# 🧬 What Is It?
Conway's Game of Life is a cellular automaton devised by mathematician John Conway.
Each cell on a grid lives or dies depending on the state of its 8 neighbors.

# 📜 Rules
1. Any live cell with 2 or 3 live neighbors survives.
2. Any dead cell with exactly 3 live neighbors becomes a live cell.
3. All other live cells die in the next generation, and dead cells stay dead.

# 💻 How to Run
Requirements
Python 3.x

Run the Program
"""bash
python game_of_life.py
"""
The simulation runs in the terminal.
Press Ctrl + C to stop the program at any time.

# ⚙️ Features
- Grid size: 20x20 (modifiable via WIDTH and HEIGHT)
- Random initial grid
- No wrapping at edges (border cells have fewer neighbors)
- Terminal clearing for smooth animation
- Easy-to-modify code

# 🧩 Customize
- Cell symbols: Change CELLSTATE = ["■", " "] to use other characters.
- Grid size: Modify WIDTH and HEIGHT at the top of the script.
- Frame delay: Change time.sleep(1) to speed up or slow down the animation.
- Initial pattern: Replace gridInit() with a custom starter layout.

