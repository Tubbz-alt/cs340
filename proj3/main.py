from input import get_lines, parse
from graph import Graph, depth_first_search

lines = get_lines('acyclic_in.txt')
edges = parse(lines)
print edges
#graph = Graph(edges)

#print depth_first_search(graph)
