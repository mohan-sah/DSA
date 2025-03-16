# Recursive Binary Search Trees: Implementation Guide

## Table of Contents

* [Node Class](#node-class)
* [RecursiveBST Class](#recursive-bst-class)
* [BST: Insert](#bst-insert)
* [BST: Search](#bst-search)
* [BST: Delete](#bst-delete)
* [BST: In-order Traversal](#bst-in-order-traversal)
* [BST: Pre-order Traversal](#bst-pre-order-traversal)
* [BST: Post-order Traversal](#bst-post-order-traversal)
* [BST: Find Minimum](#bst-find-minimum)
* [BST: Find Maximum](#bst-find-maximum)
* [BST: Height](#bst-height)
* [BST: Check if Balanced](#bst-check-if-balanced)

Design and implement a Python program that defines classes for a **Recursive Binary Search Tree (BST)** and its nodes.

---

## Node Class <a name="node-class"></a>

Create a class called `Node`, which will represent a single node in the binary search tree. The class should have the following attributes:

*   `value`: The data contained in the node.
*   `left`: A reference to the left child node.
*   `right`: A reference to the right child node.

When initializing a new instance of the `Node` class, the user should provide a value for the node. The `left` and `right` attributes should be initialized to `None`.

---

## RecursiveBST Class <a name="recursive-bst-class"></a>

Create a class called `RecursiveBST`, which will represent a recursive binary search tree. The class should have the following attributes:

*   `root`: A reference to the root node of the tree.

When initializing a new instance of the `RecursiveBST` class, the `root` attribute should be initialized to `None`.

---

## BST: Insert <a name="bst-insert"></a>

Implement an `insert` method that adds a new node with a given value to the BST. The method should:

1.  If the tree is empty (`root` is `None`), set the `root` to the new node.
2.  If the tree is not empty, recursively traverse the tree to find the appropriate position for the new node based on the value:
    *   If the value is less than the current node's value, move to the left subtree.
    *   If the value is greater than the current node's value, move to the right subtree.
3.  Insert the new node as the left or right child of the appropriate parent node.
4.  Return `True` if the insertion is successful.

---

## BST: Search <a name="bst-search"></a>

Implement a `search` method that searches for a node with a given value in the BST. The method should:

1.  If the tree is empty, return `None`.
2.  Recursively traverse the tree to find the node with the given value:
    *   If the value is less than the current node's value, move to the left subtree.
    *   If the value is greater than the current node's value, move to the right subtree.
    *   If the value matches the current node's value, return the node.
3.  Return `None` if the node is not found.

---

## BST: Delete <a name="bst-delete"></a>

Implement a `delete` method that removes a node with a given value from the BST. The method should:

1.  If the tree is empty, return `None`.
2.  Recursively traverse the tree to find the node with the given value.
3.  Handle three cases:
    *   **Node has no children**: Simply remove the node.
    *   **Node has one child**: Replace the node with its child.
    *   **Node has two children**: Find the in-order successor (the smallest node in the right subtree), replace the node's value with the successor's value, and delete the successor.
4.  Return `True` if the node is found and deleted, otherwise return `False`.

---

## BST: In-order Traversal <a name="bst-in-order-traversal"></a>

Implement an `in_order_traversal` method that performs an in-order traversal of the BST. The method should:

1.  Recursively traverse the left subtree.
2.  Visit the root node.
3.  Recursively traverse the right subtree.
4.  Return a list of values in the order they were visited.

---

## BST: Pre-order Traversal <a name="bst-pre-order-traversal"></a>

Implement a `pre_order_traversal` method that performs a pre-order traversal of the BST. The method should:

1.  Visit the root node.
2.  Recursively traverse the left subtree.
3.  Recursively traverse the right subtree.
4.  Return a list of values in the order they were visited.

---

## BST: Post-order Traversal <a name="bst-post-order-traversal"></a>

Implement a `post_order_traversal` method that performs a post-order traversal of the BST. The method should:

1.  Recursively traverse the left subtree.
2.  Recursively traverse the right subtree.
3.  Visit the root node.
4.  Return a list of values in the order they were visited.

---

## BST: Find Minimum <a name="bst-find-minimum"></a>

Implement a `find_min` method that finds and returns the node with the minimum value in the BST. The method should:

1.  If the tree is empty, return `None`.
2.  Recursively traverse the left subtree until the leftmost node is found.
3.  Return the leftmost node.

---

## BST: Find Maximum <a name="bst-find-maximum"></a>

Implement a `find_max` method that finds and returns the node with the maximum value in the BST. The method should:

1.  If the tree is empty, return `None`.
2.  Recursively traverse the right subtree until the rightmost node is found.
3.  Return the rightmost node.

---

## BST: Height <a name="bst-height"></a>

Implement a `height` method that calculates the height of the BST. The method should:

1.  If the tree is empty, return `0`.
2.  Recursively calculate the height of the left and right subtrees.
3.  Return the maximum height of the two subtrees plus `1` (for the root node).

---

## BST: Check if Balanced <a name="bst-check-if-balanced"></a>

Implement an `is_balanced` method that checks if the BST is balanced. The method should:

1.  If the tree is empty, return `True`.
2.  Recursively check the height of the left and right subtrees.
3.  Return `True` if the difference in heights is no more than `1` and both subtrees are balanced, otherwise return `False`.

---

This guide provides a structured approach to implementing a **Recursive Binary Search Tree** and its common operations