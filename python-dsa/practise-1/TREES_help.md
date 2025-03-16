# Trees: Implementation Guide

## Table of Contents

* [TreeNode Class](#tree-node-class)
* [BinaryTree Class](#binary-tree-class)
* [Tree Traversal: Pre-order](#tree-pre-order)
* [Tree Traversal: In-order](#tree-in-order)
* [Tree Traversal: Post-order](#tree-post-order)
* [Tree: Insert](#tree-insert)
* [Tree: Search](#tree-search)
* [Tree: Delete](#tree-delete)
* [Tree: Height](#tree-height)
* [Tree: Level-order Traversal (BFS)](#tree-level-order-traversal)

Design and implement a Python program that defines two classes: `TreeNode` and `BinaryTree`.

## TreeNode Class <a name="tree-node-class"></a>

Create a class called `TreeNode`, which will represent a single node in a binary tree. The class should have the following attributes:

*   `value`: The data contained in the node.
*   `left`: A reference to the left child node.
*   `right`: A reference to the right child node.

When initializing a new instance of the `TreeNode` class, the user should provide a value for the node. The `left` and `right` attributes should be initialized to `None`.

## BinaryTree Class <a name="binary-tree-class"></a>

Create a class called `BinaryTree`, which will represent a binary tree. The class should have the following attributes:

*   `root`: A reference to the root node of the tree.

When initializing a new instance of the `BinaryTree` class, the `root` attribute should be initialized to `None`.

## Tree Traversal: Pre-order <a name="tree-pre-order"></a>

Implement a `pre_order` method that performs a pre-order traversal of the tree. The method should:

1.  Visit the root node.
2.  Recursively traverse the left subtree.
3.  Recursively traverse the right subtree.
4.  Return a list of values in the order they were visited.

## Tree Traversal: In-order <a name="tree-in-order"></a>

Implement an `in_order` method that performs an in-order traversal of the tree. The method should:

1.  Recursively traverse the left subtree.
2.  Visit the root node.
3.  Recursively traverse the right subtree.
4.  Return a list of values in the order they were visited.

## Tree Traversal: Post-order <a name="tree-post-order"></a>

Implement a `post_order` method that performs a post-order traversal of the tree. The method should:

1.  Recursively traverse the left subtree.
2.  Recursively traverse the right subtree.
3.  Visit the root node.
4.  Return a list of values in the order they were visited.

## Tree: Insert <a name="tree-insert"></a>

Implement an `insert` method that adds a new node with a given value to the tree. The method should:

1.  If the tree is empty (`root` is `None`), set the `root` to the new node.
2.  If the tree is not empty, traverse the tree to find the appropriate position for the new node based on the value (assuming a binary search tree structure).
3.  Insert the new node as the left or right child of the appropriate parent node.
4.  Return `True`.

## Tree: Search <a name="tree-search"></a>

Implement a `search` method that searches for a node with a given value in the tree. The method should:

1.  If the tree is empty, return `None`.
2.  Traverse the tree to find the node with the given value.
3.  Return the node if found, otherwise return `None`.

## Tree: Delete <a name="tree-delete"></a>

Implement a `delete` method that removes a node with a given value from the tree. The method should:

1.  If the tree is empty, return `None`.
2.  Traverse the tree to find the node with the given value.
3.  Handle three cases:
    *   **Node has no children**: Simply remove the node.
    *   **Node has one child**: Replace the node with its child.
    *   **Node has two children**: Find the in-order successor, replace the node's value with the successor's value, and delete the successor.
4.  Return `True` if the node was found and deleted, otherwise return `False`.

## Tree: Height <a name="tree-height"></a>

Implement a `height` method that calculates the height of the tree. The method should:

1.  If the tree is empty, return `0`.
2.  Recursively calculate the height of the left and right subtrees.
3.  Return the maximum height of the two subtrees plus `1` (for the root node).

## Tree: Level-order Traversal (BFS) <a name="tree-level-order-traversal"></a>

Implement a `level_order` method that performs a level-order traversal (Breadth-First Search) of the tree. The method should:

1.  If the tree is empty, return an empty list.
2.  Use a queue to traverse the tree level by level.
3.  Return a list of values in the order they were visited.

---
