#ifndef _TREES_H
#define _TREES_H

#define RED 0
#define BLACK 1

typedef struct _node {
  char* key;
  struct _node *parent, *left, *right;
  int color;
} node;

extern node* make_tree(char**, int);
extern void insert(node**, char*);
extern node* search(node*, const char*);
extern void make_rb_tree(char**, int);
extern void insert_rb(node**, char*);

#endif
