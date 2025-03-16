# Hash Tables: Implementation Guide

## Table of Contents

* [HashTable Class](#hash-table-class)
* [Hash Function](#hash-function)
* [HashTable: Insert](#hash-table-insert)
* [HashTable: Search](#hash-table-search)
* [HashTable: Delete](#hash-table-delete)
* [HashTable: Resize](#hash-table-resize)
* [HashTable: Collision Handling](#hash-table-collision-handling)

Design and implement a Python program that defines a class for a hash table.

## HashTable Class <a name="hash-table-class"></a>

Create a class called `HashTable`, which will represent a hash table data structure. The class should have the following attributes:

*   `capacity`: The initial capacity of the hash table (number of buckets).
*   `size`: The number of key-value pairs stored in the hash table.
*   `buckets`: A list (or array) to store the key-value pairs. Each bucket can be a list to handle collisions (e.g., using chaining).

When initializing a new instance of the `HashTable` class, the user should provide an initial capacity. The `buckets` should be initialized as a list of empty lists (or `None` values) with a length equal to the capacity. The `size` should be initialized to `0`.

## Hash Function <a name="hash-function"></a>

Implement a hash function that maps a key to an index in the hash table. The hash function should:

1.  Take a key as input.
2.  Convert the key into a hash code (e.g., using Python's built-in `hash()` function or a custom implementation).
3.  Map the hash code to an index within the range of the hash table's capacity using the modulo operation.
4.  Return the computed index.

## HashTable: Insert <a name="hash-table-insert"></a>

Implement an `insert` method that adds a key-value pair to the hash table. The method should:

1.  Use the hash function to compute the index for the key.
2.  If the bucket at the computed index is empty, store the key-value pair there.
3.  If the bucket is not empty (collision occurs), handle the collision using a chosen method (e.g., chaining or open addressing).
4.  Increment the `size` by `1`.
5.  If the load factor (size / capacity) exceeds a threshold (e.g., 0.7), resize the hash table.
6.  Return `True` if the insertion is successful.

## HashTable: Search <a name="hash-table-search"></a>

Implement a `search` method that retrieves the value associated with a given key. The method should:

1.  Use the hash function to compute the index for the key.
2.  If the bucket at the computed index is empty, return `None`.
3.  If the bucket is not empty, search for the key in the bucket (handling collisions if necessary).
4.  Return the value if the key is found, otherwise return `None`.

## HashTable: Delete <a name="hash-table-delete"></a>

Implement a `delete` method that removes a key-value pair from the hash table. The method should:

1.  Use the hash function to compute the index for the key.
2.  If the bucket at the computed index is empty, return `None`.
3.  If the bucket is not empty, search for the key in the bucket (handling collisions if necessary).
4.  If the key is found, remove the key-value pair and decrement the `size` by `1`.
5.  Return the removed value if the key is found, otherwise return `None`.

## HashTable: Resize <a name="hash-table-resize"></a>

Implement a `resize` method that increases the capacity of the hash table when the load factor exceeds a threshold. The method should:

1.  Create a new list of buckets with double the current capacity.
2.  Rehash all existing key-value pairs into the new buckets.
3.  Update the `capacity` and `buckets` attributes.
4.  Return `True` when the resizing is complete.

## HashTable: Collision Handling <a name="hash-table-collision-handling"></a>

Implement a collision handling mechanism to manage cases where multiple keys hash to the same index. Common methods include:

1.  **Chaining**: Store multiple key-value pairs in the same bucket using a linked list or another data structure.
2.  **Open Addressing**: Probe for the next available bucket using a probing sequence (e.g., linear probing, quadratic probing, or double hashing).

Choose one method and implement it consistently in the `insert`, `search`, and `delete` methods.

---

This guide provides a structured approach to implementing a hash table and its common operations