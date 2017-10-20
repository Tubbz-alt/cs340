from input import get_lines, parse
from graph import make_graph, topological_sort
from sp import dag_sp, bellman_ford, dijkstra

edges = parse(get_lines("cyclic.txt"))
graph = make_graph(edges)
vec, backs = topological_sort(graph)

negs = False
for _, _, w in edges:
  if w < 0:
    negs = True
cycle = len(backs) > 0

if negs:
  print "Negatives"
if cycle:
  print "Cyclic"
  print backs

print dag_sp(graph, vec, '1')
print bellman_ford(graph, '1')
print dijkstra(graph, '1') ## This is gonna be wrong cus it has neg edges
