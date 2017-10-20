import sys
from sorts import PriorityQueue

INFINITY = sys.maxint

def init_single_source(graph, source):
  d = {v: INFINITY for v in graph}
  d[source] = 0
  parent = {v: v for v in graph}
  return d, parent

def relax(graph, d, parent, v, adj, weight):
  curr = d[v] + weight
  if curr < d[adj]:
    d[adj] = curr
    parent[adj] = v

def dag_sp(graph, vec, source):
  d, parent = init_single_source(graph, source)
  for v in vec:
    for adj, weight in graph[v]:
      relax(graph, d, parent, v, adj, weight)
  return d, parent

def bellman_ford(graph, source):
  d, parent = init_single_source(graph, source)
  for i in xrange(1, len(graph)):
    for v in graph:
      for adj, weight in graph[v]:
        relax(graph, d, parent, v, adj, weight)
  for v in graph:
    for adj, weight in graph[v]:
      if d[adj] > d[v] + weight:
        return None
  return d, parent

def dijkstra(graph, source):
  def compare(x, y): return x[1] - y[1]
  def key(x): return x[0]
  def update(x, y): x[1] = y
  d, parent = init_single_source(graph, source)
  pq  = PriorityQueue(compare, key, update)
  for v in graph:
    pq.insert([v, INFINITY])
  pq.decrease_priority(source, 0)
  while not pq.is_empty():
    v, w = pq.pop()
    d[v] = w
    for adj, weight in graph[v]:
      elem = pq.get(adj)
      if elem and elem[1] > d[v] + weight:
        pq.decrease_priority(adj, d[v] + weight)
        parent[adj] = v
  return d, parent

def get_shortest_path(d, parent, dest):
  dist = d[dest]
  curr = dest
  next = parent[curr]
  order = [curr]
  while curr != next:
    curr = next
    next = parent[curr]
    order.append(curr)
  return dist, order
