# Python3 program to check if a given
# instance of 8 puzzle is solvable or not
import random
# A utility function to count
# inversions in given array 'arr[]'
# def getInvCount(arr, n):
# 	inv_count = 0
# 	empty_value = -1
# 	if arr is None or len(arr) != n:
# 		raise ValueError("Array must be of length {}".format(n))
# 	for i in range(0, n):
# 		if arr[i] is None:
# 			raise ValueError("Array can't contain null values")
# 		for j in range(i + 1, n):
# 			if arr[j] is None:
# 				raise ValueError("Array can't contain null values")
# 			if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
# 				inv_count += 1
# 	return inv_count

# # This function returns true
# # if given 8 puzzle is solvable.
# def isSolvable(puzzle):
#     if puzzle is None or len(puzzle) != 3 or any(len(row) != 3 for row in puzzle):
#         raise ValueError("Puzzle must be a 3x3 grid")

#     flat_puzzle = []
#     for row in puzzle:
#         if any(item is None for item in row):
#             raise ValueError("Puzzle cannot contain None values")
#         flat_puzzle.extend(row)

#     inv_count = getInvCount(flat_puzzle, len(flat_puzzle))
    
#     return (inv_count % 2 == 0)

import random

def getInvCount(arr, n):
    inv_count = 0
    empty_value = -1
    if arr is None or len(arr) != n:
        raise ValueError("Array must be of length {}".format(n))
    for i in range(0, n):
        if arr[i] is None:
            raise ValueError("Array can't contain null values")
        for j in range(i + 1, n):
            if arr[j] is None:
                raise ValueError("Array can't contain null values")
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

def isSolvable(puzzle):

    flat_puzzle = []
    for row in puzzle:
        if any(item is None for item in row):
            raise ValueError("Puzzle cannot contain None values")
        flat_puzzle.extend(row)

    inv_count = getInvCount(flat_puzzle, len(flat_puzzle))
    
    return (inv_count % 2 == 0)

def main(grid_size):
    puzzle = random.sample(range(grid_size * grid_size), grid_size * grid_size)
    puzzle = [puzzle[i:i + grid_size] for i in range(0, grid_size * grid_size, grid_size)]
    if isSolvable(puzzle):
        print("Solvable")
        for item in puzzle:
            print(*item, end=" ")
    else:
        print("Not Solvable")
        main(grid_size)

grid_size = int(input("Enter the grid size (e.g., 3 for 3x3): "))
main(grid_size)

