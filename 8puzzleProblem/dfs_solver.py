from collections import deque
import pygame
import time
import argparse
import math

pygame.init()

WIDTH, HEIGHT = 300, 300
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 12000

MAX_ITERATIONS=100000

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (173, 216, 230)

def generate_goal_state(grid_size):
    return [[col + row * grid_size for col in range(grid_size)] for row in range(grid_size)]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid Iterations")


def find_blank(state):
    for i in range(len(state)):  
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state, pathstring):
    neighbors = []
    blank_row, blank_col = find_blank(state)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
    grid_size = len(state)  
    for dr, dc in moves:
        new_row, new_col = blank_row + dr, blank_col + dc
        if 0 <= new_row < grid_size and 0 <= new_col < grid_size:
            new_state = [row[:] for row in state]
            new_state[blank_row][blank_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[blank_row][blank_col]
            neighbors.append(new_state)

    return neighbors, pathstring

def solve_puzzle_dfs(initial_state, goal_state, pathstring):
    stack = [(initial_state, [])]  
    visited = set()
    nodes_visited = 0
    count = 0
    while stack:
        if nodes_visited >= MAX_ITERATIONS:  
            print("Max iterations reached, stopping search.")
            return None, None, nodes_visited, None  

        current_state, path = stack.pop() 
        nodes_visited += 1
        visited.add(tuple(map(tuple, current_state))) 

        if current_state == goal_state:
            return path, len(path), nodes_visited, pathstring  

        neighbors, pathstring = get_neighbors(current_state, pathstring)
        for neighbor in neighbors: 
            if tuple(map(tuple, neighbor)) not in visited:
                stack.append((neighbor, path + [neighbor]))
        count += 1
        if count % 1000 == 0:
            print(f"Iteration {count}")

    return None, None, nodes_visited, None  


def draw_grid(state, goal_state, moved_indices=None):
    grid_size = len(state)  
    cell_size = WIDTH // grid_size  
    screen.fill(WHITE)

    for i in range(grid_size):
        for j in range(grid_size):
            x, y = j * cell_size, i * cell_size
            if state[i][j] == goal_state[i][j]:
                color = GREEN
            elif state[i][j] == 0:
                color = LIGHT_BLUE
            elif moved_indices and (i, j) in moved_indices:
                color = RED
            else:
                color = BLUE

            pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
            font = pygame.font.SysFont(None, 40)
            text = font.render(str(state[i][j]), True, (0, 0, 0))
            screen.blit(text, (x + cell_size // 3, y + cell_size // 3))

    pygame.display.update()

def show_iterations(iterations, goal_state, pathstring):
    prev_state = None
    count = 0
    for iteration in iterations:
        moved_indices = []
        if prev_state:
            for i in range(len(iteration)):
                for j in range(len(iteration[i])):
                    if prev_state[i][j] != iteration[i][j]:
                        moved_indices.append((i, j))
                        prev_blank_row, prev_blank_col = find_blank(prev_state)
                        cur_blank_row, cur_blank_col = find_blank(iteration)
                        if prev_blank_row == cur_blank_row:
                            pathstring += "Right " if prev_blank_col < cur_blank_col else "Left "
                        else:
                            pathstring += "Down " if prev_blank_row < cur_blank_row else "Up "

        draw_grid(iteration, goal_state, moved_indices)
        prev_state = iteration
        count += 1
        time.sleep(60 / FPS)
        if count % 1000 == 0:
            print(f"Iteration {count}")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
    return pathstring



def validate_input(grid_size):
    while True:
        try:
            input_file = args.input_file  
            with open(input_file, 'r') as f:
                numbers = list(map(int, f.readline().strip().split()))

                expected_numbers = grid_size ** 2
                valid_range = set(range(expected_numbers))

                if len(numbers) == expected_numbers and set(numbers) == valid_range:
                    return [numbers[i:i + grid_size] for i in range(0, expected_numbers, grid_size)]
                else:
                    print(f"Invalid input. Ensure the file contains {expected_numbers} unique numbers from 0 to {expected_numbers - 1}.")
        except (ValueError, FileNotFoundError):
            input_file = input("Enter the name of the input file: ")  
            with open(input_file, 'r') as f:
                numbers = list(map(int, f.readline().strip().split()))

                expected_numbers = grid_size ** 2
                valid_range = set(range(expected_numbers))

                if len(numbers) == expected_numbers and set(numbers) == valid_range:
                    return [numbers[i:i + grid_size] for i in range(0, expected_numbers, grid_size)]
                else:
                    print(f"Invalid input. Ensure the file contains {expected_numbers} unique numbers from 0 to {expected_numbers - 1}.")


def calculate_grid_size(input_file):
    try:
        with open(input_file, 'r') as f:
            numbers = list(map(int, f.readline().strip().split()))
            grid_size = int(math.sqrt(len(numbers))) 
            if grid_size * grid_size != len(numbers):
                raise ValueError("The input file does not represent a perfect square grid.")
            return grid_size
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")
        return None


def main():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='The input file for the puzzle')
    args = parser.parse_args()
    global WIDTH, HEIGHT

    grid_size = calculate_grid_size(args.input_file)
    cell_size = WIDTH // grid_size
    goal_state = generate_goal_state(grid_size)
    initial_state = validate_input(grid_size)
    font = pygame.font.SysFont(None, 40)
    gamestart_text = font.render("Algorithm Running", True, GREEN)
    screen.fill((0,0,0))
    screen.blit(gamestart_text, (WIDTH // 2 - gamestart_text.get_width() // 2, HEIGHT // 2 - gamestart_text.get_height() // 2))
    pygame.display.flip()    
    time.sleep(2)
    start_time = time.time()
    solution_path, cost, nodes_visited, pathstring = solve_puzzle_dfs(initial_state, goal_state, pathstring='')
    end_time = time.time()
    running_time = end_time - start_time

    if solution_path:
        print("\nSolution found:")
        for move in solution_path:
            print(move)
        print("\n--- Performance Metrics ---")
        print(f"Path to goal: {len(solution_path)} moves")
        print(f"Number of visited nodes: {nodes_visited}")
        print(f"Running time: {running_time:.4f} seconds")
        memory_usage = nodes_visited * 36
        print(f"Memory usage: {memory_usage} bytes")

        pathstring = show_iterations(solution_path, goal_state, pathstring)
        print(f"Moves taken: {pathstring}")
    else:
        print("No solution found.")
        font = pygame.font.SysFont(None, 40)
        gameover_text = font.render("Not Solvable", True, RED)
        screen.fill(BLUE)
        screen.blit(gameover_text, (WIDTH // 2 - gameover_text.get_width() // 2, HEIGHT // 2 - gameover_text.get_height() // 2))
        pygame.display.flip()    
        time.sleep(2)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

main()