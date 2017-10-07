import sys

INFINITY = (None, sys.maxint)

def merge(arr, left, mid, right):
  a = arr[left:mid]
  b = arr[mid:right]
  a.append(INFINITY)
  b.append(INFINITY)
  for i in xrange(left, right):
    arr[i] = a.pop(0) if a[0][1] < b[0][1] else b.pop(0)
  
  
def merge_sort(arr, left=0, right=None):
  if right == None: right = len(arr)
  if left + 1 == right: return
  mid = left + (right - left) / 2
  merge_sort(arr, left, mid)
  merge_sort(arr, mid, right)
  merge(arr, left, mid, right)
