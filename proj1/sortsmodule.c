#include "Python.h"

extern void insertion_sort(char**, int);
extern void merge_sort(char**, int, int);
extern void heap_sort(char**, int);
extern void build_heap(char**, int);

void pylist_to_array(PyObject*, char**, int);
void array_to_pylist(char**, int, PyObject*);

void pylist_to_array(PyObject* list, char** arr, int n) {
  int i;
  
  for (i = 0; i < n; i++) {
    arr[i] = PyString_AsString(PyList_GetItem(list, i));
  }
}

void array_to_pylist(char** arr, int n, PyObject* list) {
  int i;

  for (i = 0; i < n; i++) {
    PyList_SetItem(list, i, PyString_FromString(arr[i]));
  }
}

static PyObject* py_insertion_sort(PyObject* self, PyObject* args) {
  char** arr;
  int n;

  PyObject *list;
  PyArg_ParseTuple(args, "O", &list);

  n = PyList_Size(list);
  arr = calloc(n, sizeof(char**));
  pylist_to_array(list, arr, n);
  insertion_sort(arr, n);
  array_to_pylist(arr, n, list);
  free(arr);
  return Py_None;
}

static PyObject* py_merge_sort(PyObject* self, PyObject* args) {
  char** arr;
  int n;

  PyObject *list;
  PyArg_ParseTuple(args, "O", &list);

  n = PyList_Size(list);
  arr = calloc(n, sizeof(char**));
  pylist_to_array(list, arr, n);
  merge_sort(arr, 0, n);
  array_to_pylist(arr, n, list);
  free(arr);
  return Py_None;
}

static PyObject* py_heap_sort(PyObject* self, PyObject* args) {
  char** arr;
  int n;

  PyObject *list;
  PyArg_ParseTuple(args, "O", &list);

  n = PyList_Size(list);
  arr = calloc(n, sizeof(char**));
  pylist_to_array(list, arr, n);
  heap_sort(arr, n);
  array_to_pylist(arr, n, list);
  free(arr);
  return Py_None;
}

static PyObject* py_build_heap(PyObject* self, PyObject* args){
  char** arr;
  int n;

  PyObject *list;
  PyArg_ParseTuple(args, "O", &list);

  n = PyList_Size(list);
  arr = calloc(n, sizeof(char**));
  pylist_to_array(list, arr, n);
  build_heap(arr, n);
  array_to_pylist(arr, n, list);
  free(arr);
  return Py_None;
}

static PyMethodDef SortsMethods[] = {
  {"insertion_sort", py_insertion_sort, METH_VARARGS, ""},
  {"merge_sort", py_merge_sort, METH_VARARGS, ""},
  {"heap_sort", py_heap_sort, METH_VARARGS, ""},
  {"build_heap", py_build_heap, METH_VARARGS, ""},
  {NULL, NULL, 0, NULL} //Sentinel
};

PyMODINIT_FUNC initsorts(void) {
  (void) Py_InitModule("sorts", SortsMethods);
}
  
