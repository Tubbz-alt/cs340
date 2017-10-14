from input import parse, get_lines, dedupe
from graph import make_weighted_graph
from sorts import merge_sort, PriorityQueue
from mst import kruskals, prims

edges = dedupe(parse(get_lines("graph.txt")))

print kruskals(edges)
print prims(edges)
