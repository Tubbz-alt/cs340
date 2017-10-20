from input import get_lines, parse
from graph import make_graph, topological_sort
from sp import dag_sp, bellman_ford, dijkstra, get_shortest_path

edges = parse(get_lines("dag.txt"))
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


dag_sol = dag_sp(graph, vec, '1')
bf_sol = bellman_ford(graph, '1')
dijk_sol = dijkstra(graph, '1')

print dag_sol
print bf_sol
print dijk_sol

d, parent = dag_sol
print get_shortest_path(d, parent, '5')
