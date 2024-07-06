# main.py
import pygame
import sys
import random
from config import WIDTH, HEIGHT, BLACK, agent, final
from grid import draw_grid
from maze import initialize_maze, run, show_path, value, visualize_grid

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid World")

pos = [(row, col) for row in range(8) for col in range(8)]
wall = random.sample(pos, 6)
pos = [(row, col) for (row, col) in pos if (row, col) not in wall]
danger = random.sample(pos, 3)
pos = [(row, col) for (row, col) in pos if (row, col) not in danger]
final.append(random.sample(pos, 1)[0])
pos = [(row, col) for (row, col) in pos if (row, col) != final[0]]
agent.append(random.sample(pos, 1)[0])
print(f"danger zones:{danger}, walls:{wall}, final destination:{final}")

def main():
    clock = pygame.time.Clock()
    screen.fill(BLACK)
    draw_grid(screen, wall, danger)
    initialize_maze(wall, danger)
    run()
    pygame.display.flip()
    clock.tick(0.25)
    print("VALUE MATRIX")
    a, b = final[0]
    value[a][b] = 100
    for i in range(8):
        for j in range(8):
            print(int(value[i][j]), end="   ")
        print()
    show_path(screen, value)
    visualize_grid(value)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
