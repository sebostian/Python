def dijkstra(graph, cost, vertex):
    parent = {}
    for key in graph:
        for value in graph[key]: 
            s = []
            s.insert(key)
            s.insert(value)
            print(cost[s])
    return graph[vertex]