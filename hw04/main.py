from collections import deque

def bipartition(graph):
    color = {}
    for node in graph:
        if node not in color:
            queue = deque([node])
            color[node] = 0
            while queue:
                u = queue.popleft()
                for v in graph.get(u, []):
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return None
    left = {n for n, c in color.items() if c == 0}
    right = {n for n, c in color.items() if c == 1}
    return (left, right)
