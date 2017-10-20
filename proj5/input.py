def get_lines(filename):
  with open(filename, 'r') as f:
    lines = f.read().split('\n')
    if lines[-1] == "":
      return lines[:-1]
    else:
      return lines

def partition(l, n):
  a = []
  for i in xrange(len(l) / n):
    a.append(tuple(l[i*n:(i+1)*n]))
  return a

def parse(lines):
  edges = []
  for line in lines:
    if line.split(':')[1].strip() == "":
      continue
    fromv = line.split(':')[0]
    for tov, weight in partition(filter(lambda x: x != '', line.split(':')[1].split(' ')), 2):
      edges.append((fromv, tov, int(weight)))
  return edges
