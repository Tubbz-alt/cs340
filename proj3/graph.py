import sys

BLACK = 0
GREY = 1
WHITE = 2

INFINITY = sys.maxint

class Graph:
  def __init__(self, edges):
    self.vertices = {}
    for fromv, tov in edges:
      if not fromv in self.vertices:
        self.vertices[fromv] = []
      if not tov in self.vertices:
        self.vertices[tov] = []
      self.add_edge(fromv, tov)
      
  def add_edge(self, v1, v2):
    self.vertices[v1].append(v2)      

class Vertex:
  def __init__(self, key):
    self.color = WHITE
    self.distance = INFINITY
    self.discovered = INFINITY
    self.finished = INFINITY
    self.parent = None
    self.children = []
    self.key = key

def depth_first_search(graph):
  vertices = map(lambda x: Vertex(x), graph.vertices.keys())
  return vertices
