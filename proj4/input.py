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

def dedupe(s):
  s = sorted(s, key=lambda x: x[1]) # sort by weight
  def keep_if_missing(s, c):
    if not s or c != s[-1]:
      s.append(c)
      return s
    else:
      return s
  return reduce(keep_if_missing, s, [])

def parse(lines):
  edges = []
  for line in lines:
    if line.split(':')[1].strip() == "":
      continue
    fromv = int(line.split(':')[0])
    for tov, weight in partition(filter(lambda x: x != '', line.split(':')[1].split(' ')), 2):
      edges.append(({fromv, int(tov)}, int(weight)))
  return edges
