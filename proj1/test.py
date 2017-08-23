from sorts import insertion_sort, merge, merge_sort

arr = [3, 2, 1, 4, 80, 3, 6, 10, 6]
print arr
insertion_sort(arr)
print arr

arr = ['corn', 'carn', 'cow']
print arr
merge(arr, 0, 1, 3)
print arr

arr = ['a', 'c', 'b', 'f', 'd', 'aa', 'zzzzzz']
print arr
merge_sort(arr)
print arr

arr = ['a', 'c', 'b', 'f', 'd', 'aa', 'zzzzzz']
print arr
insertion_sort(arr)
print arr
