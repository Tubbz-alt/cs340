from input import get_lines, parse
from graph import make_graph

edges = parse(get_lines("dag.txt"))
print make_graph(edges)
