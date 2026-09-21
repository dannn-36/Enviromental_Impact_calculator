package main

import "fmt"

// Algoritmos de ejemplo para el analizador (Go).

func fibonacci(n int) int {
	// Recursión con dos llamadas por invocación: O(2^n)
	if n < 2 {
		return n
	}
	return fibonacci(n-1) + fibonacci(n-2)
}

func bubbleSort(arr []int) []int {
	n := len(arr)
	for i := 0; i < n; i++ {
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
	return arr
}

func binarySearch(arr []int, target, lo, hi int) int {
	if lo > hi {
		return -1
	}
	mid := (lo + hi) / 2
	if arr[mid] == target {
		return mid
	}
	if arr[mid] < target {
		return binarySearch(arr, target, mid+1, hi)
	}
	return binarySearch(arr, target, lo, mid-1)
}

func total(values []int) int {
	s := 0
	for _, v := range values {
		s += v
	}
	return s
}

func merge(left, right []int) []int {
	result := make([]int, 0, len(left)+len(right))
	i, j := 0, 0
	for i < len(left) && j < len(right) {
		if left[i] <= right[j] {
			result = append(result, left[i])
			i++
		} else {
			result = append(result, right[j])
			j++
		}
	}
	result = append(result, left[i:]...)
	return append(result, right[j:]...)
}

func mergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	mid := len(arr) / 2
	left := mergeSort(arr[:mid])
	right := mergeSort(arr[mid:])
	return merge(left, right)
}

func isEven(n int) bool {
	if n == 0 {
		return true
	}
	return isOdd(n - 1)
}

func isOdd(n int) bool {
	if n == 0 {
		return false
	}
	return isEven(n - 1)
}

func main() {
	data := []int{5, 3, 8, 1, 9, 2}
	fmt.Println(fibonacci(10), total(data))
	sorted := mergeSort(bubbleSort(data))
	fmt.Println(binarySearch(sorted, 8, 0, len(sorted)-1), isEven(10))
}
