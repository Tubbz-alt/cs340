import sys

INFINITY = sys.maxint

def init_single_source(graph, source):
  d = {v: INFINITY for v in graph}
  d[source] = 0
  return d

def relax(graph, d, v, adj, weight):
  curr = d[v] + weight
  d[adj] = min([curr, d[adj]])

def dag_sp(graph, vec, source):
  d = init_single_source(graph, source)
  for v in vec:
    for adj, weight in graph[v]:
      relax(graph, d, v, adj, weight)
  return d

def bellman_ford(graph, source):
  d = init_single_source(graph, source)
  for i in xrange(1, len(graph)):
    for v in graph:
      for adj, weight in graph[v]:
        relax(graph, d, v, adj, weight)
  for v in graph:
    for adj, weight in graph[v]:
      if d[adj] > d[v] + weight:
        return None
  return d

# def dijkstra(graph, source):
#   def compare(x, y): return x[1] - y[1]
#   def key(x): return x[0]
#   def update(x, y): x[1] = y
#   d = init_single_source(graph, source)
#   pq  = PriorityQueue(compare, key, update)
  
  
