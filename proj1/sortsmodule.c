#include <stdio.h>
#include <string.h>

#include "Python.h"

#define INFINITY "~";

void insertion_sort(char**, int);
void merge_sort(char**, int, int);
void merge(char**, int, int, int);
void pylist_to_array(PyObject*, char**, int);
void array_to_pylist(char**, int, PyObject*);

void insertion_sort(char* arr[], int n) {
  char* curr;
  int i, j;
  
  for (i = 1; i < n; i++) {
    curr = arr[i];
    j = i - 1;
    while (j >= 0 && strcmp(curr, arr[j]) < 0) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = curr;
  }
}

void merge_sort(char* arr[], int left, int right) {
  int mid;
  
  if (left + 1 == right) return;
  mid = left + (right - left) / 2;
  merge_sort(arr, left, mid);
  merge_sort(arr, mid, right);
  merge(arr, left, mid, right);
}

void merge(char* arr[], int left, int mid, int right) {
  int i, j, na, nb;
  na = mid - left + 1;
  nb = right - mid + 1;
  char* a[na];
  char* b[nb];

  memcpy(a, arr + left, sizeof(char*) * (na - 1));
  memcpy(b, arr + mid, sizeof(char*) * (nb - 1));
  a[na - 1] = INFINITY;
  b[nb - 1] = INFINITY;

  for (i = 0, j = 0; i + j < na + nb - 2;) {
    if (strcmp(a[i], b[j]) < 0) {
      arr[left + i + j] = a[i];
      i++;
    } else {
      arr[left + i + j] = b[j];
      j++;
    }
  }
}

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

static PyMethodDef SortsMethods[] = {
  {"insertion_sort", py_insertion_sort, METH_VARARGS, ""},
  {"merge_sort", py_merge_sort, METH_VARARGS, ""},
  {NULL, NULL, 0, NULL} //Sentinel
};

PyMODINIT_FUNC initsorts(void) {
  (void) Py_InitModule("sorts", SortsMethods);
}
  
