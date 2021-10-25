from collections import defaultdict
def shortestPath(edgelist, start_node):
    graph = defaultdict(list)
    # build the DAG
    for a, b, v in edgelist:
        graph[a].append((b, v))

    # topological sort
    def topoSort(node, stack, visited):
        visited.add(node)
        for child, weight in graph[node]:
            if child not in visited:
                topoSort(child, stack, visited)
        stack.append(node)
    
    stack = []
    visited = set()
    nodes = list(graph.keys())
    for node in nodes:
        if node not in visited:
            topoSort(node, stack, visited)
            
    # relaxation
    distance = {vertex:float('inf') for vertex in graph} 
    distance[start_node] = 0
    while stack:
        node = stack.pop()
        
        for child, weight in graph[node]:
            distance[child] = min(distance[node] + weight, distance[child])
            
    return distance


edgelist = [(0, 1, 5),
(0, 2, 3),
(1, 3, 6),
(1, 2, 2),
(2, 4, 4),
(2, 5, 2),
(2, 3, 7),
(3, 4, -1),
(4, 5, -2)]

d = shortestPath(edgelist, 1)
print(d)
# {0: inf, 1: 0, 2: 2, 3: 6, 4: 5, 5: 3}
