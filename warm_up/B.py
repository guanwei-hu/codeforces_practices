import sys
from collections import deque

# a
char = 97


def raw_input():
    return sys.stdin.readline().strip()


def bfs(graph, src_idx, n, seen, place_holder, char):
    """
    :type graph: dict[int, int]
    :type src_idx: int
    :type n: int
    :type seen: set
    :type place_holder: List[str]
    :type char: int
    :rtype: int, -1 / 0

    start breadth first search from `src_idx`
    return 0 if no restriction is violated
    return -1 otherwise
    """

    # z
    if char > 122:
        return -1

    q = deque([src_idx])
    seen.add(src_idx)

    while q:
        curr_idx = q.popleft()

        # termination condition
        if curr_idx == n:
            return 0

        place_holder[curr_idx] = chr(char)
        next_idx = graph[curr_idx]

        # restrictions on `next_idx`
        if next_idx in seen or next_idx > n or next_idx <= curr_idx:
            return -1

        q.append(next_idx)
        if next_idx != n:
            seen.add(next_idx)

    return 0


def bfs_all(graph, src_indices, n, place_holder):
    global char
    seen = set()

    for src_idx in src_indices:
        if src_idx not in seen:
            flag = bfs(graph, src_idx, n, seen, place_holder, char)
            if flag == -1:
                return -1
            char += 1

    return 0


# if 1:
#     n = 11
#     arr = [4, 9, 10, 6, 12, 8, 12, 11, 12, 12, 12]
#
# if 1:
#     n = 6
#     arr = [3, 4, 6, 5, 4, 7]
#
# if 1:
#     n = 7
#     arr = [4, 6, 8, 8, 8, 8, 8]
#
# if 1:
#     n = 10
#     arr = [2, 5, 4, 6, 8, 9, 8, 10, 11, 11]

# input
n = int(raw_input())
arr = map(int, raw_input().split())

#
place_holder = ['!' for i in range(n)]

# construct graph
graph = {}
for idx, num in enumerate(arr):
    graph[idx] = num - 1

if bfs_all(graph=graph, src_indices=list(range(0, n)), n=n, place_holder=place_holder) == 0:
    print("".join(place_holder))
else:
    print(-1)

