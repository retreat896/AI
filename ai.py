import queue
import re
import pygame
from collections import deque



def converttogrid(boardstr):
    #converts string board to a list
    #validate the board to make sure there is only 9 digits and not repeating and if space separated
    #check if it is 9 digits
    
    if( not re.match("^([0-8]{1}[\s]*){9}$", boardstr)):
        print("Invalid board")
        return None
    #split the board into a list that has single digits only.
    boardstr = boardstr.replace(" ", "")
    #split
    board = [boardstr[i:i+1] for i in range(0, len(boardstr), 1)]
    print(board)
    #check for 9 digits
    if(len(boardstr) != 9):
        return None
    #check for repeating digits
    if(len(set(board)) != 9):
        return None
    
    return board

def converttoobject(board):
    boardlist = board
    boardobject = {}
    #split into example object like so {00:7, 01:2, 02:4, 10:5, 11:0, 12:6, 20:8, 21:3, 22:1}
    for i in range(len(boardlist)):
        boardobject[str(int(i/3))+","+str(i%3)] = boardlist[i]
    return boardobject

def displayboardpygame(board):
    #display board in pygame
    #create a 3x3 grid
    #draw the board
    #display the board
    return 0


def findchildren(element,gridmap):
    #using a 3x3 grid find the children of the element
    #return a list of children
    #example string : "7 2 4 5 0 6 8 3 1"
    #`0 1 2`
    #`3 4 5`
    #`6 7 8`
    # 0 is the empty space
    return 0


def breadthfirstsearch(start,goal, gridmap):
    #BREADTH_FIRST_SEARCH on a grid
    #grid will be a space seperated list "7 2 4 5 0 6 8 3 1"
    #start with empty queue and path
    q=queue.Queue()
    path=[]
    #add root to queue
    q.put(start)
    #color the root green

    #while queue is not empty
    while not q.empty():
    #    get first element from queue
        element=q.get()
    #    add element to path
        path.append(element)
    #    if element is goal
        if element==goal:
    #        print path to user
            print(path)
    #        return element to user
            return element
    #    else
        else:
    #        find children of element
            children=findchildren(element,gridmap)
    #        add children to queue
            for child in children:
                q.put(child)
    #    return None to user
    return None

def drawnumbers(board, screen, cell_width, cell_height):
    font = pygame.font.Font(None, 36)
    for i in range(3):
        for j in range(3):
            text = font.render(board[i * 3 + j], True, (255, 255, 255))
            screen.blit(text, (j * cell_width + cell_width // 2 - text.get_width() // 2, i * cell_height + cell_height // 2 - text.get_height() // 2))
    
def __main__():
    board = "7 2 4 5 0 6 8 3 1"
    #board = input("Enter board (9 digits, not repeating, 0-9, space separated): ")
    start = input("Enter start: ")
    goal = "0 1 2 3 4 5 6 7 8"
    board = converttogrid(board)
    print(converttoobject(board))
    #breadthFirstSearch(start, goal, convertToGrid(board))
    pygame.init()
    width, height = 300, 300
    screen = pygame.display.set_mode((width, height))
    text_surface = pygame.surface.Surface(width, height)
    pygame.display.set_caption("3x3 Grid")

    # Grid line color
    line_color = (255, 255, 255)

    # Calculate cell size
    cell_width = width // 3
    cell_height = height // 3

    # Draw vertical lines
    for i in range(1, 3):
        pygame.draw.line(screen, line_color, (i * cell_width, 0), (i * cell_width, height), 3)

    # Draw horizontal lines
    for i in range(1, 3):
        pygame.draw.line(screen, line_color, (0, i * cell_height), (width, i * cell_height), 3)

    # Draw numbers
    drawnumbers(board, text_surface, cell_width, cell_height)




    # Sort the board using breadth first search
    # use pauses to show the sorting progress
    # blue means selected
    # green means in correct spot
    # red means moved but not in right spot

    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

__main__()

