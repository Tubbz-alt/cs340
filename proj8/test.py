import input
import knapsack
import sys

def pprint_2d_arr(arr):
  for row in arr[::-1]:
    s = ""
    for elem in row:
      s += "%3d," % elem
    print s

tup = input.parse("knapsack.txt")
output = knapsack.knapsack(*tup, weight_bound=int(sys.argv[1]))
print output

