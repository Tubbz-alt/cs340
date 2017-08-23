#!/usr/bin/env python
import time
import datetime

from sorts import insertion_sort, merge_sort

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
  # Determine which sort we'll use
  sorts = [insertion_sort, merge_sort]
  sort_options = ['Insertion Sort', 'Merge Sort']
  sort = sorts[menu(sort_options, 'Choose a sort')]

  # Determine the file size
  sizes = [30, 60, 90, 120, 150]
  size_options = map(lambda s: '%dK' % s, sizes)
  size = sizes[menu(size_options, 'Choose a file size')]

  # Determine the arrangement
  arrangements = ['sorted', 'perm']
  arrangement_options = ['Sorted', 'Permuted']
  arrangement = arrangements[menu(arrangement_options, 'Choose an arrangement')]

  # Find the input file
  input_file = '%s/%s%dK.txt' % (arrangement, arrangement, size)
  data = None
  with open(input_file, 'r') as f:
    data = f.read().split('\n')
    data.pop() # File ends with a newline, so there's an
               # empty string to kill at the end

  # Sort the data
  t1 = time.time()
  sort(data)
  t2 = time.time()

  # Create the output file
  time_string = datetime.datetime.fromtimestamp(t1).strftime('%Y-%m-%d@%H:%M:%S')
  output_file = 'output/%s.txt' % (time_string)
  with open(output_file, 'w') as f:
    for line in data:
      f.write('%s\n' % line)

  # Tell user how long that took & where to find her data
  delta = t2 - t1
  print 'Execution took %ds %.8fms' % (int(delta), (delta % 1) * 1000)
  print 'Output located at %s' % output_file

if __name__ == '__main__':
  main()
