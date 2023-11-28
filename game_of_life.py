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
button_color = (50, 150, 50)  # Adjusted button color
button_text_color = (255, 255, 255)

# Set up the grid
rows, cols = 50, 50
grid_size = width // rows
grid = np.random.choice([0, 1], size=(rows, cols))

# Function to update the grid based on Conway's Game of Life rules
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

# Function to draw the start button
def draw_button():
    pygame.draw.rect(screen, button_color, (0, 0, width//2, 50))
    font = pygame.font.Font(None, 36)
    text = font.render("Start", True, button_text_color)
    screen.blit(text, (width // 4 - 30, 10))

# Main game loop
running = True
simulation_running = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 0 <= event.pos[0] <= width//2 and 0 <= event.pos[1] <= 50:
                simulation_running = not simulation_running
            elif not simulation_running:
                # If the simulation is not running, toggle the state of the clicked cell
                i, j = event.pos[1] // grid_size, event.pos[0] // grid_size
                grid[i, j] = 1 - grid[i, j]  # Toggle the cell state

    screen.fill(bg_color)

    # If the simulation is running, update and draw the grid
    if simulation_running:
        grid = update_grid(grid)

    for i in range(rows):
        for j in range(cols):
            color = cell_color if grid[i, j] == 1 else bg_color
            pygame.draw.rect(
                screen, color, (j * grid_size, i * grid_size, grid_size, grid_size)
            )

    # Draw the start button
    draw_button()
    pygame.display.flip()
    time.sleep(0.1)  # Adjust the speed of the animation

pygame.quit()
