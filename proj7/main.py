import sys
from input import parse
from knapsack import knapsack, walkback

def main():
  weights, values = parse(sys.argv[1])
  weight_bound = int(prompt("Weight Bound"))
  matrix = knapsack(weights, values, weight_bound)

  score = matrix[-1][-1] ##Best score will always be in the last position
  items = walkback(weights, values, matrix)

  print "The best score is %d and the items are %s" % (score, str(items))

def usage():
  print "Usage: %s input_file" % sys.argv[0]

def prompt(*args):
  if len(args) == 1:
    return raw_input(args[0] + "? ")
  else:
    while True:
      for i, w in enumerate(args):
        print "%d) %s" %((i + 1), w)
      choice = int(raw_input("Selection? ")) - 1
      if choice < 0 or choice >= len(args):
        print "Bad selection"
      else:
        return choice

if __name__ == '__main__':
  if len(sys.argv) != 2:
    usage()
    sys.exit(1)
  main()
