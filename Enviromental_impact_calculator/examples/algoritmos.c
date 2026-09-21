#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Algoritmos de ejemplo para el analizador (C). */

int fibonacci(int n) {
    /* Recursión con dos llamadas por invocación: O(2^n) */
    if (n < 2) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

void bubble_sort(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int tmp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = tmp;
            }
        }
    }
}

int binary_search(const int *arr, int target, int lo, int hi) {
    if (lo > hi) return -1;
    int mid = (lo + hi) / 2;
    if (arr[mid] == target) return mid;
    if (arr[mid] < target) return binary_search(arr, target, mid + 1, hi);
    return binary_search(arr, target, lo, mid - 1);
}

int total(const int *values, int n) {
    int s = 0;
    for (int i = 0; i < n; i++) {
        s += values[i];
    }
    return s;
}

void merge(int *arr, int l, int m, int r) {
    int n1 = m - l + 1, n2 = r - m;
    int *left = malloc(n1 * sizeof(int));
    int *right = malloc(n2 * sizeof(int));
    memcpy(left, arr + l, n1 * sizeof(int));
    memcpy(right, arr + m + 1, n2 * sizeof(int));
    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2) {
        arr[k++] = left[i] <= right[j] ? left[i++] : right[j++];
    }
    while (i < n1) arr[k++] = left[i++];
    while (j < n2) arr[k++] = right[j++];
    free(left);
    free(right);
}

void merge_sort(int *arr, int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    merge_sort(arr, l, m);
    merge_sort(arr, m + 1, r);
    merge(arr, l, m, r);
}

int is_odd(int n);

int is_even(int n) { return n == 0 ? 1 : is_odd(n - 1); }

int is_odd(int n) { return n == 0 ? 0 : is_even(n - 1); }

int main(void) {
    int data[] = {5, 3, 8, 1, 9, 2};
    int n = sizeof(data) / sizeof(data[0]);
    printf("%d %d\n", fibonacci(10), total(data, n));
    bubble_sort(data, n);
    merge_sort(data, 0, n - 1);
    printf("%d %d\n", binary_search(data, 8, 0, n - 1), is_even(10));
    return 0;
}
