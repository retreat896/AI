from collections import deque
import random
import pygame
import time

pygame.init()

# Set up constants
WIDTH, HEIGHT = 300, 300
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 2  # Frames per second to slow down the display of iterations

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (173, 216, 230)  # Light color for moved items


goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid Iterations")


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    blank_row, blank_col = find_blank(state)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    for dr, dc in moves:
        new_row, new_col = blank_row + dr, blank_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state] # Create a copy of the state
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            neighbors.append(new_state)
    return neighbors

def solve_8_puzzle_bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = {tuple(map(tuple, initial_state))}

    while queue:
        current_state, path = queue.popleft()
        #display_grid(current_state)
        if current_state == goal_state:
            return path

        for neighbor in get_neighbors(current_state):
            
            if tuple(map(tuple, neighbor)) not in visited:
                visited.add(tuple(map(tuple, neighbor)))
                queue.append((neighbor, path + [neighbor]))

        
    return None


def draw_grid(state, goal_state, moved_indices=None):
    screen.fill(WHITE)  # Fill the screen with white background
    
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            # Get position of the cell
            x, y = j * CELL_SIZE, i * CELL_SIZE
            
            # Check if the current tile is in the correct position
            if state[i][j] == goal_state[i][j]:
                color = GREEN  # Correct position
            elif state[i][j] == 0:
                color = LIGHT_BLUE  # Blank space
            elif moved_indices and (i, j) in moved_indices:
                color = RED  # Moved tile
            else:
                color = BLUE  # Incorrectly placed tile

            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))  # Draw cell
            # Draw the number in the center of the cell
            font = pygame.font.SysFont(None, 40)
            text = font.render(str(state[i][j]), True, (0, 0, 0))
            screen.blit(text, (x + CELL_SIZE // 3, y + CELL_SIZE // 3))

    pygame.display.update()

    
def show_iterations(iterations):
    prev_state = None  # Keep track of the previous state for coloring
    for iteration in iterations:
        moved_indices = []
        # Find moved elements compared to the previous state
        if prev_state:
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    if prev_state[i][j] != iteration[i][j]:
                        moved_indices.append((i, j))

        draw_grid(iteration, goal_state, moved_indices)
        prev_state = iteration
        time.sleep(1 / FPS)  # Control the speed of iteration change
        
        # Event handling (for closing the window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return



# Example usage:
def main():
    initial = random.sample(range(9), 9)
    initial_state = [initial[i * 3:(i + 1) * 3] for i in range(3)]
    

    solution_path = solve_8_puzzle_bfs(initial_state, goal_state)

    if solution_path:
        print("Solution found:")
        print(initial_state)
        show_iterations(solution_path)
    else:
        print("No solution found.")
        main()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
main()