import sys
import numpy as np
import heapq


# Heuristic function (Manhattan distance)
def heuristic(state, goal_state):
    goal_state = np.array(goal_state)
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                lis = np.argwhere(goal_state == state[i][j])
                distance += abs(i - lis[0][0]) + abs(j - lis[0][1])
    return distance


# Successor function
def successors(state):
    successors = []
    empty_i, empty_j = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                empty_i, empty_j = i, j

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for move in moves:
        new_i, new_j = empty_i + move[0], empty_j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]

            new_state[empty_i][empty_j] = new_state[new_i][new_j]
            new_state[new_i][new_j] = 0
            # print(new_state, ' new state => ', move)
            successors.append(new_state)
    # print()
    # print(successors,' successors')
    return successors


# Goal test function
def is_goal(state, goal_state):
    return state == goal_state


# Print puzzle
def print_puzzle(state):
    for row in state:
        print(row)


# Recursive Best-First Search
def rbfs(state, goal_state, f_limit):
    if is_goal(state, goal_state):
        return state, f_limit

    my_successors = [(heuristic(neighbor, goal_state), neighbor) for neighbor in successors(state)]
    heapq.heapify(my_successors)
    while my_successors:
        alternative, _ = my_successors[1] if len(my_successors) > 1 else (float("inf"), None)
        cost, current_state = heapq.heappop(my_successors)
        if cost <= f_limit:
            result, new_cost = rbfs(current_state, goal_state, min(f_limit, alternative))
            if result:
                return result, new_cost

    return None, float("inf")

# Example input
# initial_state = [
#     [1, 2, 3],
#     [8, 0, 4],
#     [7, 6, 5]
# ]

initial_state = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
try:

    f_limit = heuristic(initial_state, goal_state)
    result, _ = rbfs(initial_state, goal_state, f_limit)

    print("Initial state:")
    print_puzzle(initial_state)

    if result is not None:
        print("Goal state reached:")
        print_puzzle(result)
    else:
        print("Goal state could not be reached.")
except:
    print('maximum recursion depth exceeded')