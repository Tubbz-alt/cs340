#ifndef _TREES_H
#define _TREES_H

typedef struct _node {
  char* key;
  struct _node *parent, *left, *right;
} node;

extern node* make_tree(char**, int);
extern void insert(node**, char*);
extern node* search(node*, char*);

#endif
