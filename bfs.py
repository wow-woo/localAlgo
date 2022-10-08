from collections import deque
graph = [
        [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * len(graph)
start = 1
q = deque()


def bfs(graph, idx, visited):
    if not visited[idx]:
        visited[idx] = True
        q.append(idx)

    next_idx = q.popleft()
    while next_idx:
        print(next_idx, end=" ")
        for idx in graph[next_idx]:
            if not visited[idx]:
                visited[idx] = True
                q.append(idx)
        if q:
            next_idx = q.popleft()
        else:
            next_idx = False


bfs(graph, 1, visited)
