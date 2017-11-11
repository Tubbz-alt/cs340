from knapsack import knapsack, walkback

def main():
  algo = prompt("Longest common subsequence", "Optimal alignment")
  if algo == 0:
    w1, w2 = prompt("First word"), prompt("Second word")
    score, alignment = longest_common_subsequence(w1, w2)
  else:
    match_score = int(prompt("Match score"))
    gap_score = int(prompt("Gap score"))
    similar_score = int(prompt("Similar letter score"))
    dissimilar_score = int(prompt("Dissimilar letter score"))
    w1, w2 = prompt("First word"), prompt("Second word")
    score, alignment = optimal_alignment(w1, w2, match_score, gap_score,
                                         similar_score, dissimilar_score)

  print "Score %d" % score
  print "Optimal alignment:"
  print alignment[0]
  print alignment[1]

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
    main()
