import sys

INFINITY = sys.maxint
UP = 0
DIAGONAL = 1
RIGHT = 2
BASE = 4
SIMILAR_LETTERS = set(map(frozenset,[
  ["b","p"], ["c","k"], ["c","s"], ["d","t"],
  ["e","y"], ["g","j"], ["g","k"], ["i","y"],
  ["k","q"], ["k","q"] ,["m","n"], ["s","z"], ["v","w"]]))
VOWELS = 'aeiou'

def are_similar(l1, l2):
  return frozenset([l1, l2]) in SIMILAR_LETTERS or (
    l1 in VOWELS and l2 in VOWELS)

def walkback(w1, w2, direction_matrix):
  r1, r2 = "", ""
  i = len(w2)
  j = len(w1)
  dir = direction_matrix[i][j]
  while dir  != BASE:
    if dir == UP:
      r1 = "_" + r1
      r2 = w2[i-1] + r2
      i -= 1
    elif dir == RIGHT:
      r1 = w1[j-1] + r1
      r2 = "_" + r2
      j -= 1
    else:
      r1 = w1[j-1] + r1
      r2 = w2[i-1] + r2
      i -= 1
      j -= 1
    dir = direction_matrix[i][j]
  return r1, r2
      
def optimal_alignment(w1, w2, match_score=2, gap_score=-2,
                      similar_score=1, dissimilar_score=-1):
  score_matrix = [[0 for j in range(len(w1) + 1)]
                  for i in range(len(w2) + 1)]
  direction_matrix = [[BASE for j in range(len(w1) + 1)]
                      for i in range(len(w2) + 1)]

  for i in xrange(len(w2) + 1):
    for j in xrange(len(w1) + 1):
      ## Base cases
      if i == 0 and j == 0:
        continue
      elif j == 0:
        score_matrix[i][j] = score_matrix[i-1][j] + gap_score
        direction_matrix[i][j] = UP
      elif i == 0:
        score_matrix[i][j] = score_matrix[i][j-1] + gap_score
        direction_matrix[i][j] = RIGHT
      ## General case
      else:
        diagonal_score = score_matrix[i-1][j-1] + (
          match_score if w1[j-1] == w2[i-1] else
          similar_score if are_similar(w1[j-1], w2[i-1]) else
          dissimilar_score)
        up_score = score_matrix[i-1][j] + gap_score
        right_score = score_matrix[i][j - 1] + gap_score
        max_score = max([up_score, right_score, diagonal_score])

        if diagonal_score == max_score:
          score_matrix[i][j] = diagonal_score
          direction_matrix[i][j] = DIAGONAL
        elif up_score == max_score:
          score_matrix[i][j] = up_score
          direction_matrix[i][j] = UP
        else:
          score_matrix[i][j] = right_score
          direction_matrix[i][j] = RIGHT

  return score_matrix[-1][-1], walkback(w1, w2, direction_matrix)

def longest_common_subsequence(w1, w2):
  return optimal_alignment(w1, w2, 1, 0, -INFINITY, -INFINITY)
  
