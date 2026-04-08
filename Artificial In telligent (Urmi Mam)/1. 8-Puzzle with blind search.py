# 8-puzzle problem solve - using blind/uninformed search:

from collections import deque

GOAL = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def find_zero(s):
    for i in range(3):
        for j in range(3):
            if s[i][j] == 0:
                return i, j

def to_tuple(s):
    return tuple(tuple(row) for row in s)

def neighbors(s):
    result = []
    x, y = find_zero(s)

    moves = [(1,0), (-1,0), (0,1), (0,-1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new = [row[:] for row in s]
            new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
            result.append(new)

    return result

def bfs(start):
    q = deque([(start, [start])])  # state + path(history) *tuple
    visited = set()

    while q:
        s, path = q.popleft()

        if s == GOAL:
            return path

        visited.add(to_tuple(s))

        for n in neighbors(s): # n means one of the next possible state
            if to_tuple(n) not in visited:
                q.append((n, path + [n]))

    return None

# Example
start = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

result = bfs(start)

# Print steps
if result:
    print("Steps:", len(result) - 1)
    for step in result:
        for row in step:
            print(row)
        print("-----")
else:
    print("No solution")