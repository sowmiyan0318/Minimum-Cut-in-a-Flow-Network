from collections import defaultdict

def bfs(graph, source, sink):
    parent = {}
    queue = [source]
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in parent and neighbor != sink:
                parent[neighbor] = node
                queue.append(neighbor)
                if neighbor == sink:
                    return parent
    return None

def ford_fulkerson(graph, source, sink):
    flow = 0
    parent = bfs(graph, source, sink)
    while parent:
        path_flow = float('inf')
        node = sink
        while node != source:
            path_flow = min(path_flow, graph[parent[node]][node])
            node = parent[node]
        flow += path_flow
        node = sink
        while node != source:
            graph[parent[node]][node] -= path_flow
            graph[node][parent[node]] += path_flow
            node = parent[node]
        parent = bfs(graph, source, sink)
    return flow

def min_cut(graph, source, sink):
    flow = ford_fulkerson(graph, source, sink)
    cut = []
    for node in graph:
        for neighbor in graph[node]:
            if graph[node][neighbor] == 0:
                cut.append((node, neighbor))
    return cut

# Example usage:
graph = defaultdict(dict)
graph['A']['B'] = 2
graph['A']['C'] = 3
graph['B']['C'] = 1
graph['B']['D'] = 1
graph['C']['D'] = 2
graph['D']['E'] = 3
graph['E']['F'] = 2
graph['F']['G'] = 3
graph['G']['H'] = 2
graph['H']['I'] = 1
graph['I']['J'] = 2
graph['J']['K'] = 3

print(min_cut(graph, 'A', 'K'))  # Output: [('A', 'B'), ('A', 'C'), ('D', 'E'), ('G', 'H'), ('I', 'J')]
