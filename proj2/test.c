#include <stdio.h>
#include <stdio.h>
#include "trees.h"

void print_tree(node* tree) {
  if (tree) {
    print_tree(tree->left);
    printf("<-%s->", tree->key);
    print_tree(tree->right);
  }
}

void main() {
  char* arr[] =
    {"cat", "dog", "alpaca", "elephant", "carrot", "buffalo", "carp"};

  node* tree;
  tree = make_rb_tree(arr, 7);
  if (search(tree, "cat")) {
    printf("Found cat!\n");
  }
  if (!search(tree, "bat")) {
    printf("Didn't find bat!\n");
  }
}
