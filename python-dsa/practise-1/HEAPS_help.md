# Heaps: Implementation Guide

## Table of Contents

* [Heap Class](#heap-class)
* [Heap: Insert](#heap-insert)
* [Heap: Extract Min/Max](#heap-extract-min-max)
* [Heap: Peek](#heap-peek)
* [Heap: Heapify](#heap-heapify)
* [Heap: Build Heap](#heap-build-heap)
* [Heap: Size](#heap-size)
* [Heap: Is Empty](#heap-is-empty)

Design and implement a Python program that defines a class for a heap data structure.

## Heap Class <a name="heap-class"></a>

Create a class called `Heap`, which will represent a heap data structure. The class should have the following attributes:

*   `heap`: A list to store the elements of the heap.
*   `is_min_heap`: A boolean indicating whether the heap is a min-heap (`True`) or a max-heap (`False`).

When initializing a new instance of the `Heap` class, the user should specify whether the heap is a min-heap or a max-heap. The `heap` list should be initialized as empty.

## Heap: Insert <a name="heap-insert"></a>

Implement an `insert` method that adds a new element to the heap while maintaining the heap property. The method should:

1.  Append the new element to the end of the `heap` list.
2.  Use the `_heapify_up` method to restore the heap property by moving the new element up the heap as necessary.
3.  Return `True` if the insertion is successful.

## Heap: Extract Min/Max <a name="heap-extract-min-max"></a>

Implement an `extract` method that removes and returns the minimum element (for a min-heap) or the maximum element (for a max-heap) from the heap. The method should:

1.  If the heap is empty, return `None`.
2.  Swap the root element (first element in the `heap` list) with the last element.
3.  Remove the last element (which is now the root element) and store it.
4.  Use the `_heapify_down` method to restore the heap property by moving the new root element down the heap as necessary.
5.  Return the extracted element.

## Heap: Peek <a name="heap-peek"></a>

Implement a `peek` method that returns the minimum element (for a min-heap) or the maximum element (for a max-heap) without removing it from the heap. The method should:

1.  If the heap is empty, return `None`.
2.  Return the root element (first element in the `heap` list).

## Heap: Heapify <a name="heap-heapify"></a>

Implement a `_heapify_up` method and a `_heapify_down` method to maintain the heap property after insertions and extractions.

*   `_heapify_up`: This method should:
    1.  Start from the last element in the heap.
    2.  Compare the element with its parent and swap if necessary to maintain the heap property.
    3.  Repeat until the heap property is restored or the root is reached.

*   `_heapify_down`: This method should:
    1.  Start from the root element.
    2.  Compare the element with its children and swap with the smallest (for min-heap) or largest (for max-heap) child if necessary.
    3.  Repeat until the heap property is restored or a leaf node is reached.

## Heap: Build Heap <a name="heap-build-heap"></a>

Implement a `build_heap` method that constructs a heap from a given list of elements. The method should:

1.  Assign the list of elements to the `heap` attribute.
2.  Starting from the last non-leaf node, use the `_heapify_down` method to heapify each node.
3.  Return `True` when the heap is built.

## Heap: Size <a name="heap-size"></a>

Implement a `size` method that returns the number of elements in the heap. The method should:

1.  Return the length of the `heap` list.

## Heap: Is Empty <a name="heap-is-empty"></a>

Implement an `is_empty` method that checks if the heap is empty. The method should:

1.  Return `True` if the `heap` list is empty.
2.  Return `False` otherwise.

---

This guide provides a structured approach to implementing a heap and its common operations