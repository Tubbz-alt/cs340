#!/usr/bin/env python
from input import get_lines, parse
from graph import make_graph, topological_sort
import sys
from os.path import isfile

filename = sys.argv[1]
if not isfile(filename):
  exit(1)

lines = get_lines(filename)
edges = parse(lines)
graph = make_graph(edges)
path, back_edges = topological_sort(graph)

if not back_edges:
  print "The path is: " + str(path)
else:
  print "The graph is cyclic. Back edges: " + str(back_edges)

