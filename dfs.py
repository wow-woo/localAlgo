# Python copies references.

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


def dfs(graph, current_idx, visited):
    visited[current_idx] = True
    print(current_idx, end=' ')

    for next_idx in graph[current_idx]:
        if not visited[next_idx]:
            dfs(graph, next_idx, visited)


dfs(graph, start, visited)
