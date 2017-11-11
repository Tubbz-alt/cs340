def parse(filename):
  weights, values = [], []
  with open(filename, 'r') as f:
    line = f.readline()
    while line != '':
      w, v = map(int, line.split(' '))
      weights.append(w)
      values.append(v)
      line = f.readline()
  return weights, values
