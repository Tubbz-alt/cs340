#include <stdlib.h>
#include <string.h>
#include "trees.h"

node* make_tree(char** arr, int n) {
  int i;
  node* tree;
  tree = NULL;

  for (i = 0; i < n; i++) {
    insert(&tree, arr[i]);
  }

  return tree;
}

void insert(node** tree, char* key) {
  node* mine;
  node* curr;
  node* prev;

  mine = (node*)malloc(sizeof(node));
  mine->key = key;

  curr = *tree;
  prev = NULL;

  while (curr) {
    prev = curr;

    if (strcmp(key, curr->key) < 0) {
      curr = curr->left;
    } else {
      curr = curr->right;
    }
  }

  mine->parent = prev;

  if (!prev) {
    // Edge case, root is null
    *tree = mine;
  } else if (strcmp(key, prev->key) < 0) {
    prev->left = mine;
  } else {
    prev->right = mine;
  }
}

node* search(node* tree, char* key) {
  if (tree == NULL) return NULL;
  if (strcmp(tree->key, key) == 0) return tree;
  if (strcmp(tree->key, key) > 0) return search(tree->left, key);
  return search(tree->right, key);
}
