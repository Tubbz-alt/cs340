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
    self.discovered = INFINITY
    self.finished = INFINITY
    self.parent = None
    self.key = key

time = 0
def depth_first_search(graph):
  global time
  vertices = map(lambda x: Vertex(x), graph.vertices.keys())
  time = 0
  for v in vertices:
    if v.color == WHITE:
      depth_first_search_visit(graph, vertices, v)
  return vertices

def depth_first_search_visit(graph, vertices, vertex):
  global time
  time += 1
  vertex.discovered = time
  vertex.color = GREY
  for adj in get_adjacencies(graph, vertices, vertex):
    if adj.color == WHITE:
      adj.parent = vertex
      vertex.children.append(adj)
      depth_first_search_visit(graph, verticies, adj)
  vertex.color = BLACK
  time = time + 1
  vertex.finished = time
    
def get_adjacencies(graph, vertices, vertex):
  return filter(lambda x: x in graph.vertices[vertex.key], vertices)
