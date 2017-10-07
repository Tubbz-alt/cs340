class ComponentTree:
  def __init__(self, key):
    self.key = key
    self.parent = self
    self.children = []

  def add_child(self, tree):
    self.children.append(tree)
    tree.parent = self

  @property
  def root(self):
    curr = self
    while curr.parent != curr:
      curr = curr.parent
    return curr
  
  @property
  def depth(self):
    return self.root.inner_depth()

  def inner_depth(self):
    if len(self.children) == 0:
      return 1
    depths = map(lambda x: x.inner_depth(), self.children)
    return max(depths) + 1

def find_set(forest, key):
  for tree in forest:
    if tree.key == key:
      return tree
    val = find_set(tree.children, key)
    if val:
      return val
