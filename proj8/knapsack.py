from heapq import heappush, heappop, heapify

def knapsack(weights, values, weight_bound):
  densities = [float(value)/weight for value, weight in zip(values, weights)]
  boundargs = (weights, values, densities, weight_bound)
  
  state = ['*'] * len(weights)
  queue = []
  heappush(queue, (-upper_bound(state, *boundargs), state))
  best_solution = 0
  best_state = ['N'] * len(weights)
  
  while len(queue) != 0:
    ## Best-first visitations
    bound, state = heappop(queue)
    if '*' not in set(state):
      solution = -bound
      if solution > best_solution:
        best_solution = solution
        best_state = state
      queue = prune(queue, bound)
    else:
      ## Backtracking
      branch(queue, state, *boundargs)
  return items_as_vec(best_state), best_solution

## Upper Bound
def upper_bound(state, weights, values, densities, weight_bound):
  remaining_weight = weight_bound
  bound = 0
  best_density = 0
  for taken, weight, value, density in zip(state, weights,
                                           values, densities):
    if taken == 'Y':
      remaining_weight -= weight
      bound += value
    elif taken == 'N':
      pass ##Make sure not taken densities not included
    else:
      best_density = max([best_density, density])
  bound += remaining_weight * best_density
  return bound      

def branch(queue, state, weights, values, densities, weight_bound):
  boundargs = (weights, values, densities, weight_bound)
  i = state.index('*')
  did, didnt = state[:], state[:] ## Slice to avoid mutation
  did[i] = 'Y'
  didnt[i] = 'N'
  did_bound = upper_bound(did, *boundargs)
  didnt_bound = upper_bound(didnt, *boundargs)
  heappush(queue,(-didnt_bound, didnt))
  did_weight = 0
  for taken, weight in zip(did, weights):
    if taken == 'Y':
      did_weight += weight
  if did_weight <= weight_bound:
    heappush(queue, (-did_bound, did))

## Pruning
def prune(queue, bound):
  queue = filter(lambda x: x[0] < bound, queue)
  heapify(queue)
  return queue

def items_as_vec(state):
  items = []
  for i, val in enumerate(state):
    if val == 'Y':
      items.append(i + 1)
  return items
