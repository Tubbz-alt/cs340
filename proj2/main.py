#!/usr/bin/env python
import os
import time
import datetime

from trees import binary_tree, red_black_tree, binary_tree_search, red_black_tree_search

def menu(options, prompt):
  while True:
    for i, option in enumerate(options):
      print '%d:\t%s' % (i + 1, option)
    val = raw_input('%s:\t' % prompt)
    try:
      val = int(val) - 1
    except ValueError:
      continue
    if val >= 0 and val < len(options): return val

def main():
  # Determine which tree we'll use
  trees = [(binary_tree, binary_tree_search), (red_black_tree, red_black_tree_search)]
  tree_options = ['Binary Tree', 'Red-Black Tree']
  tree, search = trees[menu(tree_options, 'Choose a tree')]

  # Determine the file size
  sizes = [30, 60, 90, 120, 150]
  size_options = map(lambda s: '%dK' % s, sizes)
  size = sizes[menu(size_options, 'Choose a file size')]

  # Determine the arrangement
  arrangements = ['sorted', 'perm']
  arrangement_options = ['Sorted', 'Permuted']
  arrangement = arrangements[menu(arrangement_options, 'Choose an arrangement')]

  # Determine which word we would like to find
  word = raw_input('Choose a word to search for:\t').upper()

  # Find the input file
  input_file = '%s/%s%dK.txt' % (arrangement, arrangement, size)
  data = None
  with open(input_file, 'r') as f:
    data = f.read().split('\n')
    data.pop() # File ends with a newline, so there's an
               # empty string to kill at the end

  # Tree the data
  t1 = time.time()
  my_tree = tree(data)
  t2 = time.time()

  # Tell user how long that took 
  delta = t2 - t1
  print 'Building tree took %ds %.8fms' % (int(delta), (delta % 1) * 1000)

  # Search for the word
  t1 = time.time()
  found = search(data)
  t1 = time.time()
  
  # Tell user how long that took 
  delta = t2 - t1
  print 'Searching tree took %ds %.8fms' % (int(delta), (delta % 1) * 1000)
  print 'The word %s was %s in the tree' % (word, 'found' if found else 'not found')

if __name__ == '__main__':
  main()
