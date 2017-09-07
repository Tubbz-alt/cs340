#include <stdio.h>
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
  mine->left = NULL;
  mine->right = NULL;
  mine->parent = NULL;

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

node* search(node* tree, const char* key) {
  if (tree == NULL) return NULL;
  if (strcmp(tree->key, key) == 0) return tree;
  if (strcmp(tree->key, key) > 0) return search(tree->left, key);
  return search(tree->right, key);
}

node* make_rb_tree(char** arr, int n) {
  int i;
  node* tree;
  tree = NULL;

  for (i = 0; i < n; i++) {
    insert_rb(&tree, arr[i]);
  }
  return tree;
}

void insert_rb(node** tree, char* key) {
  node* mine;
  node* curr;
  node* prev;

  mine = (node*)malloc(sizeof(node));
  mine->key = key;
  mine->left = NULL;
  mine->right = NULL;
  mine->parent = NULL;
  mine->color = RED;

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

  fixup_rb(tree, mine);
}

void fixup_rb(node** tree, node* mine) {
  node* uncle;
  
  while (mine->parent && mine->parent->color == RED) {
    if (mine->parent == mine->parent->parent->left) {
      uncle = GRANDPARENT(mine)->right;
      if (uncle && uncle->color == RED) {
        mine->parent->color = BLACK;
        uncle->color = BLACK;
        GRANDPARENT(mine)->color = RED;
        mine = GRANDPARENT(mine);
      } else {
        if (mine == mine->parent->right) {
          mine = mine->parent;
          left_rotate(tree, mine);
        }
        mine->parent->color = BLACK;
        GRANDPARENT(mine)->color = RED;
        right_rotate(tree, GRANDPARENT(mine));
      }
    } else {
      uncle = GRANDPARENT(mine)->left;
      if (uncle && uncle->color == RED) {
        mine->parent->color = BLACK;
        uncle->color = BLACK;
        GRANDPARENT(mine)->color = RED;
        mine = GRANDPARENT(mine);
      } else {
        if (mine == mine->parent->left) {
          mine = mine->parent;
          right_rotate(tree, mine);
        }
        mine->parent->color = BLACK;
        GRANDPARENT(mine)->color = RED;
        left_rotate(tree, GRANDPARENT(mine));
      }
    }
  }
  (*tree)->color = BLACK;
}

void left_rotate(node** tree, node* parent) {
  node* mine;

  // Give my subtree to my parent
  mine = parent->right;
  parent->right = mine->left; 

  if (mine->left) {
    mine->left->parent = parent;
  }

  mine->parent = parent->parent;

  if (!mine->parent) {
    // If my parent used to be the root, I am become root
    *tree = mine;
  } else if (parent == parent->parent->left) {
    parent->parent->left = mine;
  } else {
    parent->parent->right = mine;
  }

  // I become my own grandfather
  mine->left = parent;
  parent->parent = mine;
}

void right_rotate(node** tree, node* parent) {
  node* mine;
  
  // Give my subtree to my parent
  mine = parent->left;
  parent->left = mine->right; 

  if (mine->right) {
    mine->right->parent = parent;
  }

  mine->parent = parent->parent;

  if (!mine->parent) {
    // If my parent used to be the root, I am become root
    *tree = mine;
  } else if (parent == parent->parent->right) {
    parent->parent->right = mine;
  } else {
    parent->parent->left = mine;
  }

  // I become my own grandfather
  mine->right = parent;
  parent->parent = mine;
}
