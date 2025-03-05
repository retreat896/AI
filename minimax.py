import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # base case : targetDepth reached
    """
    Implementation of the minimax algorithm.

    Parameters
    ----------
    curDepth : int
        The current depth in the tree.
    nodeIndex : int
        The index of the current node.
    maxTurn : bool
        A boolean indicating whether it is the maximizing player's turn.
    scores : list
        A list of scores for each node in the tree.
    targetDepth : int
        The target depth of the search.

    Returns
    -------
    int
        The score of the best possible move.

    Notes
    -----
    The tree is assumed to be a binary tree, where the root is at depth 0.
    The maximizing player is trying to maximize the score, and the
    minimizing player is trying to minimize the score.
    """
    if curDepth == targetDepth:
        return scores[nodeIndex]
    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        )
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )

# Scores
scores = [5, 2, 6, 8]
treeDepth = int(math.log(len(scores), 2))
print("Tree Depth :", treeDepth)
print("The optimal value is :", end=" ")
print(minimax(0, 0, True, scores, treeDepth))
# This code is contributed
# by rootshadow

