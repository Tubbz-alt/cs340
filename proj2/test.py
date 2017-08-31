import trees

arr = ['cat', 'dog']

tree = trees.binary_tree(arr)

print 'looking for cat'
if trees.search_binary_tree(tree, 'cat'):
  print 'found em!'

print 'looking for bat'
if not trees.search_binary_tree(tree, 'bat'):
  print 'no dice!'
