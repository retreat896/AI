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

def get_neighbors(state,pathstring):
    neighbors = []
    blank_row, blank_col = find_blank(state)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
    for dr, dc in moves:
        new_row, new_col = blank_row + dr, blank_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [row[:] for row in state] 
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            neighbors.append(new_state)
    return neighbors, pathstring

def solve_8_puzzle_bfs(initial_state, goal_state,pathstring):
    queue = deque([(initial_state, [], 0)])
    visited = {tuple(map(tuple, initial_state))}
    nodes_visited = 0
    
    while queue:
        current_state, path, cost = queue.popleft()
        nodes_visited += 1

        if current_state == goal_state:
            return path, cost, nodes_visited, pathstring
        neighbors, pathstring = get_neighbors(current_state,pathstring)
        for neighbor in neighbors:
            if tuple(map(tuple, neighbor)) not in visited:
                visited.add(tuple(map(tuple, neighbor)))
                queue.append((neighbor, path + [neighbor], cost + 1))

    return None, None, nodes_visited, None


def draw_grid(state, goal_state, moved_indices=None):
    screen.fill(WHITE)  
    
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x, y = j * CELL_SIZE, i * CELL_SIZE
            if state[i][j] == goal_state[i][j]:
                color = GREEN  
            elif state[i][j] == 0:
                color = LIGHT_BLUE 
            elif moved_indices and (i, j) in moved_indices:
                color = RED  
            else:
                color = BLUE  

            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))  
            font = pygame.font.SysFont(None, 40)
            text = font.render(str(state[i][j]), True, (0, 0, 0))
            screen.blit(text, (x + CELL_SIZE // 3, y + CELL_SIZE // 3))

    pygame.display.update()

    
def show_iterations(iterations,pathstring):
    prev_state = None 
    for iteration in iterations:
        moved_indices = []
        if prev_state:
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    if prev_state[i][j] != iteration[i][j]:
                        moved_indices.append((i, j))
                        prev_blank_row, prev_blank_col = find_blank(prev_state)
                        cur_blank_row, cur_blank_col = find_blank(iteration)
                        if prev_blank_row == cur_blank_row:
                            if prev_blank_col < cur_blank_col:
                                pathstring += "Right "
                            else:
                                pathstring += "Left "
                        else:
                            if prev_blank_row < cur_blank_row:
                                pathstring += "Down "
                            else:
                                pathstring += "Up "


        draw_grid(iteration, goal_state, moved_indices)
        prev_state = iteration
        time.sleep(1 / FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
    return pathstring



def main():
    initial = random.sample(range(9), 9)
    initial_state = [initial[i * 3:(i + 1) * 3] for i in range(3)]
    start_time = time.time()
    solution_path, cost, nodes_visited,pathstring = solve_8_puzzle_bfs(initial_state, goal_state,pathstring='')
    end_time = time.time()
    running_time = end_time - start_time
    if solution_path:
        print("Solution found:")
        print(initial_state)
        for move in solution_path:
            print(move)
        pathstring = show_iterations(solution_path,pathstring)

        print("\n--- Performance Metrics ---")
        print(f"Path to goal: {len(solution_path)} moves") 
        print(f"Moves taken: {pathstring}")
        print(f"Cost of the path: {cost}")
        print(f"Number of visited nodes: {nodes_visited}")
        print(f"Running time: {running_time:.4f} seconds")
        memory_usage = nodes_visited * 36  
        print(f"Memory usage: {memory_usage} bytes")
        pygame.quit()
    else:
        print("No solution found.")
        main()

main()