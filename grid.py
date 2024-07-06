# grid.py
import pygame
import random
from config import WIDTH, HEIGHT, ROWS, COLS, CELL_SIZE, WHITE, BLACK, RED, GREEN, BLUE, PURPLE, agent, final

def draw_grid(screen, wall, danger):
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if (row, col) in wall:
                pygame.draw.rect(screen, BLUE, rect)
            elif (row, col) in final:
                pygame.draw.rect(screen, GREEN, rect)
            elif (row, col) in agent:
                pygame.draw.rect(screen, WHITE, rect)
            elif (row, col) in danger:
                pygame.draw.rect(screen, RED, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect, 1)
