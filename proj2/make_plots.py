#!/usr/bin/env python

import time
import datetime
from multiprocessing import Process, Lock

from trees import binary_tree, red_black_tree

mux = Lock()

def time_trees(tree, size, arrangement):
  # Get the data from the input file
  input_file = '%s/%s%dK.txt' % (arrangement, arrangement, size)
  data = None
  with open(input_file, 'r') as f:
    data = f.read().split('\n')
    data.pop() # Drop last element, its an empty string

  # Sort and time the sorting
  t1 = time.time()
  tree(data)
  t2 = time.time()
  delta = t2 - t1

  # Write our data to the csv
  data = '%s,%s,%d,%.8f\n' % (arrangement, tree.__name__, size, delta)
  # Aquire the lock to write to the output file
  mux.acquire()
  # Write the data
  with open('runs.csv', 'a') as f:
    f.write(data)
  # Release the lock
  mux.release()

  # Print that we're done
  name = '%s%dK.txt - %s' % (arrangement, size, tree.__name__)
  print '%s is done.' % name

def main():
  # Create the csv file
  with open('runs.csv', 'w') as f:
    f.write('ARRANGEMENT,TREE,SIZE,TIME\n')

  trees = [binary_tree, red_black_tree]
  sizes = [30, 60, 90, 120, 150]
  arrangements = ['sorted', 'perm']

  threads = []
  for tree in trees:
    for size in sizes:
      for arrangement in arrangements:
        t = Process(target=time_trees, args=(tree, size, arrangement))
        threads.append(t)
        try:
          t.start()
        except OSError:
          time.sleep(1) # Wait a second while the system frees a process
          t.start()
  for t in threads:
    t.join()

if __name__ == '__main__':
  main()
