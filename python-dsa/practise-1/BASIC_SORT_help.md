# Basic Sorting Algorithms: Implementation Guide

## Table of Contents

* [Sorting Overview](#sorting-overview)
* [Bubble Sort](#bubble-sort)
* [Selection Sort](#selection-sort)
* [Insertion Sort](#insertion-sort)
* [Merge Sort](#merge-sort)
* [Quick Sort](#quick-sort)
* [Heap Sort](#heap-sort)
* [Counting Sort](#counting-sort)
* [Radix Sort](#radix-sort)
* [Bucket Sort](#bucket-sort)

This guide provides a structured approach to implementing basic sorting algorithms, similar to the formatting used in the `DLL_help.md` file.

---

## Sorting Overview <a name="sorting-overview"></a>

Sorting is the process of arranging elements in a specific order (ascending or descending). Sorting algorithms are fundamental in computer science and are used in various applications, such as searching, data analysis, and database operations.

This guide covers the following basic sorting algorithms:
- **Bubble Sort**
- **Selection Sort**
- **Insertion Sort**
- **Merge Sort**
- **Quick Sort**
- **Heap Sort**
- **Counting Sort**
- **Radix Sort**
- **Bucket Sort**

---

## Bubble Sort <a name="bubble-sort"></a>

Implement a `bubble_sort` function that sorts an array using the Bubble Sort algorithm. The method should:

1. Iterate through the array multiple times.
2. Compare adjacent elements and swap them if they are in the wrong order.
3. Repeat until no swaps are needed (the array is sorted).
4. Return the sorted array.

**Example**:
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

---

## Selection Sort <a name="selection-sort"></a>

Implement a `selection_sort` function that sorts an array using the Selection Sort algorithm. The method should:

1. Iterate through the array.
2. Find the minimum element in the unsorted portion of the array.
3. Swap the minimum element with the first element of the unsorted portion.
4. Repeat until the entire array is sorted.
5. Return the sorted array.

**Example**:
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

---

## Insertion Sort <a name="insertion-sort"></a>

Implement an `insertion_sort` function that sorts an array using the Insertion Sort algorithm. The method should:

1. Iterate through the array.
2. For each element, insert it into its correct position in the sorted portion of the array.
3. Repeat until the entire array is sorted.
4. Return the sorted array.

**Example**:
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
```

---

## Merge Sort <a name="merge-sort"></a>

Implement a `merge_sort` function that sorts an array using the Merge Sort algorithm. The method should:

1. Divide the array into two halves.
2. Recursively sort each half.
3. Merge the two sorted halves into a single sorted array.
4. Return the sorted array.

**Example**:
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr
```

---

## Quick Sort <a name="quick-sort"></a>

Implement a `quick_sort` function that sorts an array using the Quick Sort algorithm. The method should:

1. Choose a pivot element from the array.
2. Partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot.
3. Recursively sort the sub-arrays.
4. Return the sorted array.

**Example**:
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

---

## Heap Sort <a name="heap-sort"></a>

Implement a `heap_sort` function that sorts an array using the Heap Sort algorithm. The method should:

1. Build a max-heap from the array.
2. Repeatedly extract the maximum element from the heap and place it at the end of the array.
3. Return the sorted array.

**Example**:
```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
```

---

## Counting Sort <a name="counting-sort"></a>

Implement a `counting_sort` function that sorts an array using the Counting Sort algorithm. The method should:

1. Count the frequency of each element in the array.
2. Use the frequency counts to place each element in its correct position.
3. Return the sorted array.

**Example**:
```python
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    return sorted_arr
```

---

## Radix Sort <a name="radix-sort"></a>

Implement a `radix_sort` function that sorts an array using the Radix Sort algorithm. The method should:

1. Sort the array by each digit, starting from the least significant digit (LSD) to the most significant digit (MSD).
2. Use a stable sorting algorithm (e.g., Counting Sort) to sort the digits.
3. Return the sorted array.

**Example**:
```python
def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10
    return arr
```

---

## Bucket Sort <a name="bucket-sort"></a>

Implement a `bucket_sort` function that sorts an array using the Bucket Sort algorithm. The method should:

1. Divide the array into a number of buckets.
2. Sort each bucket individually (using another sorting algorithm or recursively using Bucket Sort).
3. Concatenate the sorted buckets to produce the final sorted array.
4. Return the sorted array.

**Example**:
```python
def bucket_sort(arr):
    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]
    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val) / num_buckets

    for num in arr:
        index = int((num - min_val) // bucket_range)
        if index >= num_buckets:
            index = num_buckets - 1
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    return sorted_arr
```

---

This guide provides a structured approach to implementing basic sorting algorithms, similar to the formatting used in the `DLL_help.md` file.