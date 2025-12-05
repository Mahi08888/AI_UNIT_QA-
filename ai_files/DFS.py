def is_valid(state):

    for peg in state:
        if list(peg) != sorted(peg, reverse=True):
            return False
    return True

def dfs(state, goal, visited, path):
    path.append(state)

    if state == goal:
        return True

    visited.add(state)

    moves = [(0,1), (0,2), (1,0), (1,2), (2,0), (2,1)]

    for s, d in moves:
        new_state = [list(peg) for peg in state]

        if new_state[s]:
            disk = new_state[s].pop()

            if not new_state[d] or new_state[d][-1] > disk:
                new_state[d].append(disk)

                new_tuple = tuple(tuple(peg) for peg in new_state)

                if new_tuple not in visited and is_valid(new_tuple):
                    if dfs(new_tuple, goal, visited, path):
                        return True

    path.pop()
    return False

start = ((3,2,1), (), ())
goal = ((), (), (3,2,1))
visited = set()
path = []

dfs(start, goal, visited, path)

print("Path (states):")
for p in path:
    print(p)