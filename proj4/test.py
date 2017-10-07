from input import parse, get_lines, dedupe
from graph import make_weighted_graph
from sorts import merge_sort

edges = dedupe(parse(get_lines("graph.txt")))
merge_sort(edges)
print edges
