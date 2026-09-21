"""Algoritmos de ejemplo para el analizador (Python)."""


def fibonacci(n):
    # Recursión con dos llamadas por invocación: O(2^n)
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(arr, target, lo, hi):
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, hi)
    return binary_search(arr, target, lo, mid - 1)


def total(values):
    s = 0
    for v in values:
        s += v
    return s


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def is_even(n):
    return True if n == 0 else is_odd(n - 1)


def is_odd(n):
    return False if n == 0 else is_even(n - 1)


if __name__ == "__main__":
    data = [5, 3, 8, 1, 9, 2]
    print(fibonacci(10), bubble_sort(list(data)), total(data), merge_sort(data))
    print(binary_search(sorted(data), 8, 0, len(data) - 1), is_even(10))
