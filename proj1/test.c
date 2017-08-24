#include <stdlib.h>
#include <stdio.h>

extern void insertion_sort(char**, int);
extern void merge_sort(char**, int, int);

void print_arr(const char* arr[], int n){
  int i;
  for (i = 0; i < n; i++){
    printf("%s,", arr[i]);
  }
  printf("\n");
}

void main() {
  char* arr[] = {"c", "a", "b", "aa", "duck", "apple"};
  print_arr(arr, 6);
  merge_sort(arr, 0, 6);
  print_arr(arr, 6);
}
