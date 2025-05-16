# Conway's Game of Life — Pygame Implementation

This is a Python implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), a cellular automaton devised by mathematician John Conway.

The simulation runs in a graphical window using **Pygame**, with randomly initialized cells and interactive controls for pausing, clearing, and editing the grid.

---

## 🧬 Rules of the Game

Each cell in a 2D grid is either **alive** or **dead**. For each generation:

1. A **live** cell with 2 or 3 neighbors survives.
2. A **dead** cell with exactly 3 neighbors becomes **alive**.
3. All other cells **die** or remain **dead**.

---

## 🖥️ Features

- Grid size: 60 x 40 cells
- Random initialization
- Toggle simulation with keyboard
- Add live cells with the mouse
- Custom cell colors for dying and living states

---

## 🎮 Controls

| Action             | Key / Mouse        |
|--------------------|--------------------|
| Pause / Resume     | `Space`            |
| Clear grid         | `Backspace`        |
| Add live cell      | Left-click         |
| Quit               | Close window       |

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.7+
- [Pygame](https://www.pygame.org/)
- [Numpy](https://numpy.org/)

Install dependencies:

```bash
pip install pygame numpy

## ▶️ Run the simulation
```bash
python main.py