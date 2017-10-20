from input import get_lines, parse
from graph import make_graph, topological_sort
from sp import dag_sp, bellman_ford

edges = parse(get_lines("dag.txt"))
graph = make_graph(edges)
vec, _ = topological_sort(graph)

print dag_sp(graph, vec, '1')
print bellman_ford(graph, '1')
