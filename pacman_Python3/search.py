# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import random


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    stack.push((problem.getStartState(), []))
    visited = set()

    while not stack.isEmpty():
        (node, path) = stack.pop()
        if problem.isGoalState(node):
            return path
        
        visited.add(node)
        for successor, action, cost in problem.getSuccessors(node):
            if successor not in visited:
                new_path = path + [action]
                stack.push((successor, new_path))

    return None 
    util.raiseNotDefined()


def breadthFirstSearch(problem):
    queue = util.Queue()
    start_state = problem.getStartState()
    queue.push((start_state, []))
    visited = set()
    visited.add(start_state)

    while not queue.isEmpty():
        node, path = queue.pop()
        if problem.isGoalState(node):
            return path
        for successor, action, step_cost in problem.getSuccessors(node):
            if successor not in visited:
                visited.add(successor)
                queue.push((successor, path + [action]))

    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    costs = {}
    visited = set()
    problem.getSuccessors(problem.getStartState())
    for successor, action, cost in problem.getSuccessors(problem.getStartState()):
        if successor not in visited:
            new_cost = cost
            new_path = [action]
            pq.push((new_cost, successor, new_path), -new_cost)
            costs[successor] = new_cost

    while not pq.isEmpty():
        (cost, node, path) = pq.pop()
        if problem.isGoalState(node):
            return path
        
        visited.add(node)
        for successor, action, succ_cost in problem.getSuccessors(node):
            if successor not in visited:
                new_cost = cost + succ_cost
                new_path = path + [action]
                total_cost = new_cost + problem.getCostOfActions(new_path)
                pq.push((total_cost, successor, new_path), -total_cost)
                costs[successor] = total_cost

    return None
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    start_state = problem.getStartState()
    initial_cost = 0
    initial_priority = heuristic(start_state, problem) + initial_cost
    priority_queue = util.PriorityQueue()
    priority_queue.push((start_state, [], initial_cost), initial_priority)
    visited = {}
    while not priority_queue.isEmpty():
        state, path, cost = priority_queue.pop()
        if problem.isGoalState(state):
            return path
        
        if state in visited and visited[state] <= cost:
            continue

        visited[state] = cost
        for successor, action, step_cost in problem.getSuccessors(state):
            new_cost = cost + step_cost
            heuristic_cost = heuristic(successor, problem)
            new_priority = new_cost + heuristic_cost
            new_path = path + [action]
            priority_queue.push((successor, new_path, new_cost), new_priority)

    return [] 

import heapq

def hillClimbing(problem):
    """
    Hill Climbing search for the PositionSearchProblem.
    It selects the best successor (closest to the goal) at each step.
    """
    from util import manhattanDistance  
    current_state = problem.getStartState()
    path = []
    while not problem.isGoalState(current_state):
        successors = problem.getSuccessors(current_state)
        if not successors:
            print("No moves, stuck")
            return path  
        
        best_move = min(successors, key=lambda s: manhattanDistance(s[0], problem.goal))
        next_state, action, cost = best_move
        if manhattanDistance(current_state, problem.goal) <= manhattanDistance(next_state, problem.goal):
            print("Local optimum reached, stopping search.")
            return path
        
        path.append(action)
        current_state = next_state

    return path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
hlclimb = hillClimbing
ucs = uniformCostSearch
