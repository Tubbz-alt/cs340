from sorts import merge_sort
from trees import ComponentTree, find_set
from graph import make_weighted_graph

def kruskals(edges):
  mst = []
  graph = make_weighted_graph(edges)
  forest = []
  cost = 0
  for vertex in graph.keys():
    forest.append(ComponentTree(vertex))

  merge_sort(edges)
  
  for edge, weight in edges:
    (v1, v2) = edge
    # See if the trees have the same root
    r1, r2 = find_set(forest, v1).root, find_set(forest, v2).root
    if r1 != r2:
      cost += weight
      mst.append(edge)
      if r1.depth > r2.depth:
        r1.add_child(r2)
        forest.remove(r2)
      else:
        r2.add_child(r1)
        forest.remove(r1)
  return mst, cost
      
