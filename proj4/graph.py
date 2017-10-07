def make_weighted_graph(edges):
  graph = {}
  for vs, weight in edges:
    (v1, v2) = vs
    if not v1 in graph:
      graph[v1] = []
    if not v2 in graph:
      graph[v2] = []
    graph[v1].append((v2, weight))
    graph[v2].append((v1, weight))
  return graph
