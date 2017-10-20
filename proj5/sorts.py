
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

class PriorityQueue:
  @classmethod
  def parent(cls, index): return (index - 1) / 2
  @classmethod
  def left(cls, index): return index * 2 + 1
  @classmethod
  def right(cls, index): return index * 2 + 2
  def __init__(self, compare, key, update):
    self.heap = []
    self.compare = compare
    self.key = key
    self.update = update

  def swap(self, a, b):
    temp = self.heap[a]
    self.heap[a] = self.heap[b]
    self.heap[b] = temp
    
  def insert(self, val):
    i = len(self.heap)
    self.heap.append(val)
    self.swim(i)

  def swim(self, i):
    parent = PriorityQueue.parent(i)
    if i != 0 and self.compare(self.heap[i], self.heap[parent]) < 0:
      self.swap(i, parent)
      self.swim(parent)

  def sink(self, i):
    left, right = PriorityQueue.left(i), PriorityQueue.right(i)
    if left >= len(self.heap):
      # Children are not in heap
      return
    if right >= len(self.heap):
      # Only left child is in the heap
      if self.compare(self.heap[i], self.heap[left]) > 0:
        self.swap(i, left)
      return
    # Both children are in the heap
    smaller = left if self.compare(self.heap[left], self.heap[right]) < 0 else right
    if self.compare(self.heap[i], self.heap[smaller]) > 0:
      self.swap(i, smaller)
      self.sink(smaller)

  def decrease_priority(self, key, val):
    for i, element in enumerate(self.heap):
      if self.key(element) == key:
        self.update(element, val)
        self.swim(i)
        return
      
  def pop(self):
    if len(self.heap) == 1: return self.heap.pop()
    bottom = self.heap.pop()
    top = self.heap.pop(0)
    self.heap.insert(0, bottom)
    return top

  def is_empty(self):
    return len(self.heap) == 0

  def get(self, key):
    for elem in self.heap:
      if self.key(elem) == key:
        return elem
    return None
