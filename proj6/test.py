import alignment

def pprint_2d_arr(arr):
  for row in arr[::-1]:
    s = ""
    for elem in row:
      s += "%3d," % elem
    print s

print alignment.optimal_alignment("skel", "scale")
print alignment.optimal_alignment("ske", "scale")
print alignment.optimal_alignment("select", "salekt")
print alignment.longest_common_subsequence("select", "salekt")
