import sys

BLACK = 0
GREY = 1
WHITE = 2

INFINITY = sys.maxint

def make_graph(edges):
  graph = {}
  for fromv, tov, weight in edges:
    if not fromv in graph:
      graph[fromv] = []
    if not tov in graph:
      graph[tov] = []
    graph[fromv].append((tov, weight))
  return graph

def topological_sort(graph):
  color = {}
  stack, back_edges = [], []
  for v in graph:
    color[v] = WHITE
  for v in graph:
    if color[v] == WHITE:
      dfs_visit(graph, v, color, stack, back_edges)
  return stack[::-1], back_edges

def dfs_visit(graph, v, color, stack, back_edges):
  color[v] = GREY
  for adj, _ in graph[v]:
    if color[adj] == WHITE:
      dfs_visit(graph, adj, color, stack, back_edges)
    elif color [adj] == GREY:
      back_edges.append((v, adj))
  color[v] = BLACK
  stack.append(v)

