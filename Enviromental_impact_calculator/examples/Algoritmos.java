import java.util.Arrays;

/** Algoritmos de ejemplo para el analizador (Java). */
public class Algoritmos {

    static int fibonacci(int n) {
        // Recursión con dos llamadas por invocación: O(2^n)
        if (n < 2) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    static int[] bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int tmp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = tmp;
                }
            }
        }
        return arr;
    }

    static int binarySearch(int[] arr, int target, int lo, int hi) {
        if (lo > hi) return -1;
        int mid = (lo + hi) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) return binarySearch(arr, target, mid + 1, hi);
        return binarySearch(arr, target, lo, mid - 1);
    }

    static int total(int[] values) {
        int s = 0;
        for (int v : values) {
            s += v;
        }
        return s;
    }

    static void merge(int[] arr, int l, int m, int r) {
        int[] left = Arrays.copyOfRange(arr, l, m + 1);
        int[] right = Arrays.copyOfRange(arr, m + 1, r + 1);
        int i = 0, j = 0, k = l;
        while (i < left.length && j < right.length) {
            arr[k++] = left[i] <= right[j] ? left[i++] : right[j++];
        }
        while (i < left.length) arr[k++] = left[i++];
        while (j < right.length) arr[k++] = right[j++];
    }

    static void mergeSort(int[] arr, int l, int r) {
        if (l >= r) return;
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }

    static boolean isEven(int n) { return n == 0 ? true : isOdd(n - 1); }

    static boolean isOdd(int n) { return n == 0 ? false : isEven(n - 1); }

    public static void main(String[] args) {
        int[] data = {5, 3, 8, 1, 9, 2};
        System.out.println(fibonacci(10) + " " + total(data));
        bubbleSort(data.clone());
        mergeSort(data, 0, data.length - 1);
        System.out.println(binarySearch(data, 8, 0, data.length - 1) + " " + isEven(10));
    }
}
