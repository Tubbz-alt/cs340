import sys
from input import parse, get_lines, dedupe
from mst import kruskals, prims

def main():
  if len(sys.argv) != 2:
    usage()
    sys.exit(1)
  edges = dedupe(parse(get_lines(sys.argv[1])))
  kruskals_output, _ = kruskals(edges)
  prims_output, _ = prims(edges)

  print_edges(prims_output, "primout.txt")
  print_edges(kruskals_output, "kruskalout.txt")

def print_edges(edges, filename):
  with open(filename, "w") as f:
    for v1, v2 in edges:
      f.write("%s %s\n" % (v1, v2))

def usage():
  print "Usage: %s inputfile" % sys.argv[0]
  
if __name__ == "__main__":
  main()
