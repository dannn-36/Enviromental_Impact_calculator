using System;
using System.Collections.Generic;

// Algoritmos de ejemplo para el analizador (C#).
public static class Algoritmos
{
    public static int Fibonacci(int n)
    {
        // Recursión con dos llamadas por invocación: O(2^n)
        if (n < 2)
        {
            return n;
        }
        return Fibonacci(n - 1) + Fibonacci(n - 2);
    }

    public static int[] BubbleSort(int[] arr)
    {
        int n = arr.Length;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n - i - 1; j++)
            {
                if (arr[j] > arr[j + 1])
                {
                    (arr[j], arr[j + 1]) = (arr[j + 1], arr[j]);
                }
            }
        }
        return arr;
    }

    public static int BinarySearch(int[] arr, int target, int lo, int hi)
    {
        if (lo > hi) return -1;
        int mid = (lo + hi) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) return BinarySearch(arr, target, mid + 1, hi);
        return BinarySearch(arr, target, lo, mid - 1);
    }

    public static int Total(IEnumerable<int> values)
    {
        int s = 0;
        foreach (var v in values)
        {
            s += v;
        }
        return s;
    }

    static void Merge(int[] arr, int l, int m, int r)
    {
        var left = new int[m - l + 1];
        var right = new int[r - m];
        Array.Copy(arr, l, left, 0, left.Length);
        Array.Copy(arr, m + 1, right, 0, right.Length);
        int i = 0, j = 0, k = l;
        while (i < left.Length && j < right.Length)
        {
            arr[k++] = left[i] <= right[j] ? left[i++] : right[j++];
        }
        while (i < left.Length) arr[k++] = left[i++];
        while (j < right.Length) arr[k++] = right[j++];
    }

    public static void MergeSort(int[] arr, int l, int r)
    {
        if (l >= r) return;
        int m = l + (r - l) / 2;
        MergeSort(arr, l, m);
        MergeSort(arr, m + 1, r);
        Merge(arr, l, m, r);
    }

    static bool IsEven(int n) => n == 0 ? true : IsOdd(n - 1);

    static bool IsOdd(int n) => n == 0 ? false : IsEven(n - 1);

    public static void Main()
    {
        int[] data = { 5, 3, 8, 1, 9, 2 };
        Console.WriteLine($"{Fibonacci(10)} {Total(data)}");
        BubbleSort((int[])data.Clone());
        MergeSort(data, 0, data.Length - 1);
        Console.WriteLine($"{BinarySearch(data, 8, 0, data.Length - 1)} {IsEven(10)}");
    }
}
