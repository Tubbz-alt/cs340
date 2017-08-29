class Node:
  def __init__(self, key, parent=None):
    self.key = key
    self.parent = parent
    self.left = self.right = None

class Tree:
  def __init__(self, root=None):
    self.root = root

  def insert(self, node):
    curr, prev = self.root, None:
    while curr != None:
      prev = curr
      curr = curr.left if node.key < curr.key else curr.right
    node.parent = prev
    if prev == None:
      self.root = node
    elif node.key < prev.key:
      prev.left = node
    else:
      prev.right = node

  def search(self, key):
    if root == None:
      return None
    if root.key == key:
      return root;
    

def make_tree(list):
  tree = Tree()
  for elem in list:
    node = Node(elem)
    tree.insert(node)

