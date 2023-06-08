import numpy as np
from queue import PriorityQueue

class PuzzleState:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return np.array_equal(self.puzzle, other.puzzle)

    def __hash__(self):
        return hash(str(self.puzzle))

    def __str__(self):
        return str(self.puzzle)

    def get_blank_position(self):
        return np.argwhere(self.puzzle == 0)[0]

    def get_children(self):
        children = []
        blank_pos = self.get_blank_position()

        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = blank_pos + move
            if 0 <= new_pos[0] < 3 and 0 <= new_pos[1] < 3:
                new_puzzle = np.copy(self.puzzle)
                new_puzzle[blank_pos[0], blank_pos[1]] = new_puzzle[new_pos[0], new_pos[1]]
                new_puzzle[new_pos[0], new_pos[1]] = 0
                child_state = PuzzleState(new_puzzle)
                child_state.parent = self
                print(child_state,' <==')
                children.append(child_state)
        return children

def heuristic(state):
    # Manhattan distance heuristic
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    dist = 0
    for i in range(3):
        for j in range(3):
            if state.puzzle[i, j] != 0:
                lis = np.argwhere(goal_state == state.puzzle[i, j])
                dist += abs(i - lis[0][0]) + abs(j - lis[0][1])

    # print(dist , ' <<-')
    return dist

def RBFS(state, f_limit):
    if np.array_equal(state.puzzle, np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])):
        return state, 0
    # print(state.get_children(),' get children')
    successors = []
    for child in state.get_children():
        child.g = state.g + 1
        child.h = heuristic(child)
        child.f = max(child.g + child.h, state.f)
        successors.append(child)

    while True:
        best = min(successors)
        print('----------')
        print(best,'  best ')
        if best.f > f_limit:
            return None, best.f
        alternative = min([s for s in successors if s != best], default=None)
        result, best.f = RBFS(best, min(f_limit, alternative.f))
        if result is not None:
            return result, best.f

def solve_puzzle(initial_state):
    f_limit = heuristic(initial_state)

    while True:
        result, f_limit = RBFS(initial_state, f_limit)
        print(f_limit,' f_limits')
        if result is not None:
            moves = []
            while result.parent is not None:
                moves.append(str(result))
                result = result.parent
            moves.append(str(result))
            moves.reverse()
            print(moves,' this is move list')
            return moves


initial_state = PuzzleState(np.array(
    [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
))
solution = solve_puzzle(initial_state)
print(solution)