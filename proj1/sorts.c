#include <stdio.h>
#include <string.h>

#define INFINITY "~"
#define LEFT(i) (i*2+1)
#define RIGHT(i) (i*2+2)
#define PARENT(i) (i-1/2)

void insertion_sort(char**, int);
void merge_sort(char**, int, int);
void merge(char**, int, int, int);
void heap_sort(char**, int);
void heapify(char**, int, int);
void build_heap(char**, int);
void swap(char**, int, int);

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

void heap_sort(char** arr, int n){
  int i;
  
  build_heap(arr, n);
  for (i = n - 1; i > 0; i--) {
    swap(arr, 0, i);
    n--;
    heapify(arr, n, 0);
  }
}

void build_heap(char** arr, int n) {
  int i;
  for (i = (n - 1) / 2; i >= 0; i--){
    heapify(arr, n, i);
  }
}

void heapify(char** arr, int n, int i) {
  int l, r, pos;
  
  l = LEFT(i);
  r = RIGHT(i);
  pos = i;
  if (l < n && strcmp(arr[l], arr[i]) > 0) {
    pos = l;
  }
  if (r < n && strcmp(arr[r], arr[pos]) > 0) {
    pos = r;
  }
  if (pos != i) {
    swap(arr, i, pos);
    heapify(arr, n, pos);
  }
}

void swap(char** arr, int i, int j) {
  char* temp;
  temp = arr[j];
  arr[j] = arr[i];
  arr[i] = temp;
}
