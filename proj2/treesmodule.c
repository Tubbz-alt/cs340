#include "Python.h"
#include "binary_tree.h"

void pylist_to_array(PyObject*, char**, int);

void pylist_to_array(PyObject* list, char** arr, int n) {
  int i;
  
  for (i = 0; i < n; i++) {
    arr[i] = PyString_AsString(PyList_GetItem(list, i));
  }
}


static PyObject* py_make_binary_tree(PyObject* self, PyObject* args) {
  TREE* tree;
  char** arr;
  int n;

  PyObject *list;
  PyArg_ParseTuple(args, "O", &list);

  n = PyList_Size(list);
  arr = calloc(n, sizeof(char**));
  pylist_to_array(list, arr, n);
  tree = make_tree(arr, n);
  free(arr); // Don't need this anymore, data should be in tree
  return PyCapsule_New(tree, NULL, NULL);
}

static PyObject* py_search_binary_tree(PyObject* self, PyObject* args) {
  TREE* tree;
  NODE* node;
  const char* key;

  PyObject* capsule;
  PyArg_ParseTuple(args, "Os", &capsule, &key);

  tree = PyCapsule_GetPointer(capsule, NULL);
  node = search(tree->root, key);

  if (node) {
    return Py_True;
  } else {
    return Py_False;
  }
}

static PyMethodDef TreesMethods[] = {
  {"binary_tree", py_make_binary_tree, METH_VARARGS, ""},
  {"search_binary_tree", py_search_binary_tree, METH_VARARGS, ""},
  /* TODO:  Replace with real RBTree methods*/
  {"red_black_tree", py_make_binary_tree, METH_VARARGS, ""},
  {"search_red_black_tree", py_search_binary_tree, METH_VARARGS, ""},
  {NULL, NULL, 0, NULL} //Sentinel
};

PyMODINIT_FUNC inittrees(void) {
  (void) Py_InitModule("trees", TreesMethods);
}
