import sys

from input import get_lines, parse
from graph import make_graph, topological_sort
from sp import dag_sp, bellman_ford, dijkstra, get_shortest_path, INFINITY

def main(filename):
  with open(filename, 'r') as f:
    edges = parse(get_lines(filename))
    graph = make_graph(edges)
  source = raw_input("Source vertex:")
  while not in_graph(graph, source):
    source = raw_input("Bad source\nSource vertex:")
    
  vec, back_edges = topological_sort(graph)
  negs = False
  for _, _, w in edges:
    if w < 0:
      negs = True
  cycle = len(back_edges) > 0

  if not cycle:
    print "Graph is a DAG, running DAG SP algorithm"
    d, parent = dag_sp(graph, vec, source)
  elif not negs:
    print "Graph has no negative edges, running Dijkstra's algorithm"
    d, parent = dijkstra(graph, source)
  else:
    print "Running Bellman-Ford algorithm"
    d, parent = bellman_ford(graph, source)

  if d == None: ## Sufficent to assume parent is also None
    print "Graph contains a negative-weight cycle."
    sys.exit(0)

  while True:
    dest = raw_input("Destination vertex:")
    while not in_graph(graph, dest):
      dest = raw_input("Bad destination\nDestination vertex:")
    dist, order = get_shortest_path(d, parent, dest)
    if dist >= INFINITY:
      print "There is no way to reach the destination from the source"
    else:
      print "The distance between the vertices is %d" % dist
      print "The shortest path is %s" % pprint_path(order)

def in_graph(graph, key):
  return key in graph

def pprint_path(order):
  return '->'.join(order)

def usage():
  print "Usage: %s <filename>" % sys.argv[0]

if __name__ == "__main__":
  if len(sys.argv) != 2:
    usage()
    sys.exit(1)
  main(sys.argv[1])
