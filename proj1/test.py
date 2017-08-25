#!/usr/bin/env python
from sorts import insertion_sort, merge_sort, heap_sort, build_heap

arr = ['a', 'c', 'b', 'f', 'd', 'aa', 'zzzzzz']
print arr
merge_sort(arr)
print arr

arr = ['a', 'c', 'b', 'f', 'd', 'aa', 'zzzzzz']
print arr
insertion_sort(arr)
print arr

arr = ['a', 'c', 'b', 'f', 'd', 'aa', 'zzzzzz']
print arr
heap_sort(arr)
print arr

arr = ['a', 'c', 'b', 'f', 'd', 'aa', 'zzzzzz']
print arr
build_heap(arr)
print arr
