def get_lines(filename):
  with open(filename, 'r') as f:
    lines = f.read().split('\n')
    if lines[-1] == "":
      return lines[:-1]
    else:
      return lines

def parse(lines):
  edges = []
  for line in lines:
    if line.split(':')[1].strip() == "":
      continue
    fromv = int(line.split(':')[0])
    for tov in filter(lambda x: x != '', line.split(':')[1].split(' ')):
      edges.append((fromv, int(tov)))
  return edges
