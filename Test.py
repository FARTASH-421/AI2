# Python program explaining
# argwhere() function

import numpy as np

def heuristic(state):
    # Manhattan distance heuristic
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    dist = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                print(i,' index')
                print(i - np.argwhere(goal_state == state[i][j]))
                dist += abs(i - np.argwhere(goal_state == state[i][j])[0][0]) +\
                        abs(j - np.argwhere(goal_state == state[i][j])[0][1])
    return dist

state = [[1,0,2],[4,5,7],[8,6,2]]
heuristic(state)

