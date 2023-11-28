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
start_button_color = (50, 150, 50)
randomise_button_color = (150, 50, 150)
button_text_color = (255, 255, 255)

# Set up the grid
rows, cols = 50, 50
grid_size = width // rows
grid = np.zeros((rows, cols), dtype=int)

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

# Function to randomize the grid
def randomize_grid():
    return np.random.choice([0, 1], size=(rows, cols))

# Function to draw a button
def draw_button(x, text, color):
    pygame.draw.rect(screen, color, (x, 0, width // 2, 50))
    font = pygame.font.Font(None, 36)
    text_render = font.render(text, True, button_text_color)
    screen.blit(text_render, (x + width // 4 - 30, 10))

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

            if width // 2 <= event.pos[0] <= width and 0 <= event.pos[1] <= 50:
                # If the click is on the right half, randomize the grid
                grid = randomize_grid()

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

    # Draw the Start button
    draw_button(0, "Start", start_button_color)

    # Draw the Randomize button
    draw_button(width // 2, "Randomize", randomise_button_color)

    pygame.display.flip()
    time.sleep(0.1)  # Adjust the speed of the animation

pygame.quit()
