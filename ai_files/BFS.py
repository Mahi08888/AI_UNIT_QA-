from collections import deque


def is_valid(state):

    for peg in state:
        if list(peg) != sorted(peg, reverse=True):
            return False
    return True



def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set([start])

    moves = [(0,1), (0,2), (1,0), (1,2), (2,0), (2,1)]

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for s, d in moves:
            new_state = [list(peg) for peg in state]

            if new_state[s]: 
                disk = new_state[s].pop()

                if not new_state[d] or new_state[d][-1] > disk:
                    new_state[d].append(disk)

                    new_tuple = tuple(tuple(peg) for peg in new_state)

                    if new_tuple not in visited and is_valid(new_tuple):
                        visited.add(new_tuple)
                        queue.append((new_tuple, path + [new_tuple]))

    return None



start = ((3,2,1), (), ())
goal = ((), (), (3,2,1))

path = bfs(start, goal)

print("Path (states):")
for p in path:
    print(p)