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
matrix = knapsack.knapsack(*tup, weight_bound=int(sys.argv[1]))
pprint_2d_arr(matrix)
print knapsack.walkback(*tup, matrix=matrix)
