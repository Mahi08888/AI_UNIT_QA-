import heapq

def is_valid(state):
   
    for peg in state:
        if list(peg) != sorted(peg, reverse=True):
            return False
    return True



def heuristic(state):
    return len(state[0]) + len(state[1])


def astar(start, goal):
    pq = []
    heapq.heappush(pq, (0, start, [start]))
    visited = set()

    moves = [(0,1), (0,2), (1,0), (1,2), (2,0), (2,1)]

    while pq:
        cost, state, path = heapq.heappop(pq)

        if state == goal:
            return path

        visited.add(state)

        for s, d in moves:
            new_state = [list(peg) for peg in state]

            if new_state[s]:
                disk = new_state[s].pop()

                if not new_state[d] or new_state[d][-1] > disk:
                    new_state[d].append(disk)

                    new_tuple = tuple(tuple(peg) for peg in new_state)

                    if new_tuple not in visited and is_valid(new_tuple):
                        new_cost = len(path) + heuristic(new_tuple)
                        heapq.heappush(pq, (new_cost, new_tuple, path + [new_tuple]))

    return None


start = ((3,2,1), (), ())
goal = ((), (), (3,2,1))

path = astar(start, goal)

print("Path (states):")
for p in path:
    print(p)
    