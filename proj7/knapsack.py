def knapsack(weights, values, weight_bound):
  matrix = [[0 for j in range(weight_bound + 1)]
             for i in range(len(values) + 1)]
  for i in xrange(1, len(values) + 1):
    for j in xrange(weight_bound + 1):
      ## Base Cases
      if j == 0:
        continue
      ## General Case
      weight = weights[i - 1]
      value = values[i - 1]
      include_score = 0
      if j - weight >= 0:
        include_score = matrix[i - 1][j - weight] + value
      exclude_score = matrix[i - 1][j]
      if include_score > exclude_score:
        matrix[i][j] = include_score
      else:
        matrix[i][j] = exclude_score
        
  return matrix
        
def walkback(weights, values, matrix):
  i = len(matrix) - 1
  j = len(matrix[i]) - 1
  items = []
  
  while i > 0:
    weight = weights[i - 1]
    value = values[i - 1]
    score = matrix[i][j]

    exclude_score = matrix[i - 1][j]
    if score != exclude_score:
      items.append(i)
      j = j - weight
    i -= 1

  return items[::-1]
      
