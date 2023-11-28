import pygame
import numpy as np
import time

# Initialize pygame
pygame.init()

# Set up the display
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")

# Set up the colors
bg_color = (255, 255, 255)
cell_color = (0, 0, 0)

# Set up the grid
rows, cols = 50, 50
grid_size = width // rows
grid = np.random.choice([0, 1], size=(rows, cols))

def update_grid(grid):
    new_grid = grid.copy()
    for i in range(rows):
        for j in range(cols):
            neighbors = (
                grid[i - 1:i + 2, j - 1:j + 2].sum() - grid[i, j]
            )  # Exclude the cell itself
            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0
            elif neighbors == 3:
                new_grid[i, j] = 1
    return new_grid

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(bg_color)

    # Update and draw the grid
    grid = update_grid(grid)
    for i in range(rows):
        for j in range(cols):
            color = cell_color if grid[i, j] == 1 else bg_color
            pygame.draw.rect(
                screen, color, (j * grid_size, i * grid_size, grid_size, grid_size)
            )

    pygame.display.flip()
    time.sleep(0.1)  # Adjust the speed of the animation

pygame.quit()
