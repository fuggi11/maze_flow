# maze.py
import numpy as np
import pygame
import random
from config import ROWS, COLS, agent, final,PURPLE,CELL_SIZE
import matplotlib.pyplot as plt

maze = np.zeros((ROWS, COLS))
value = np.zeros((ROWS, COLS))

def initialize_maze(wall, danger):
    for i in range(ROWS):
        for j in range(COLS):
            if (i, j) in wall:
                maze[i][j] = -1
                value[i][j] = -1
            elif (i, j) in final:
                maze[i][j] = 100
                value[i][j] = -1
            elif (i, j) in danger:
                maze[i][j] = -1
                value[i][j] = -1
            else:
                maze[i][j] = 0
                value[i][j] = 0

def action():
    return random.randint(1, 4)

def state():
    while True:
        i = random.randint(0, 7)
        j = random.randint(0, 7)
        if value[i][j] != -1:
            return i, j

# 1: up  2: left   3: down   4: right
gamma = 0.9

def update(i, j, b):
    if b == 1 and (i - 1) >= 0:
        value[i][j] = max(maze[i - 1][j] + gamma * (value[i-1][j]), value[i][j])
    elif b == 2 and (j - 1) >= 0:
        value[i][j] = max(maze[i][j - 1] + gamma * (value[i][j-1]), value[i][j])
    elif b == 3 and (i + 1) < 8:
        value[i][j] = max(maze[i + 1][j] + gamma * (value[i+1][j]), value[i][j])
    elif b == 4 and (j + 1) < 8:
        value[i][j] = max(maze[i][j + 1] + gamma * (value[i][j+1]), value[i][j])

def run():
    epoch = 50000
    for _ in range(epoch):
        b = action()
        i, j = state()
        update(i, j, b)

def show_path(screen, value):
    i, j = agent[0]
    a, b = final[0]
    print(f"Starting position: {(i, j)}")
    print(f"Final position: {(a, b)}")
    while (i != a or j != b):
        m = max(value[i][j-1] if j-1 >= 0 else -1,
                value[i-1][j] if i-1 >= 0 else -1,
                value[i+1][j] if i+1 < 8 else -1,
                value[i][j+1] if j+1 < 8 else -1)

        if j - 1 >= 0 and value[i][j-1] == m:
            j = j - 1
        elif i + 1 < 8 and value[i+1][j] == m:
            i = i + 1
        elif i - 1 >= 0 and value[i-1][j] == m:
            i = i - 1
        elif j + 1 < 8 and value[i][j+1] == m:
            j = j + 1
        if (i == a) & (j == b):
            return
        rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, PURPLE, rect)
        pygame.display.flip()

def visualize_grid(values, title="Value Function"):
    plt.imshow(values, cmap='coolwarm', interpolation='nearest')
    plt.colorbar(label='Value')
    plt.title(title)
    plt.show()
