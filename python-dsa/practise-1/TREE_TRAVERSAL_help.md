# Tree Traversal: Implementation Guide

## Table of Contents

* [Tree Traversal Overview](#tree-traversal-overview)
* [Pre-order Traversal](#pre-order-traversal)
* [In-order Traversal](#in-order-traversal)
* [Post-order Traversal](#post-order-traversal)
* [Level-order Traversal (BFS)](#level-order-traversal)
* [Depth-First Search (DFS)](#depth-first-search)
* [Breadth-First Search (BFS)](#breadth-first-search)
* [Iterative Traversal Methods](#iterative-traversal-methods)

This guide provides a structured approach to implementing various tree traversal algorithms, similar to the formatting used in the `DLL_help.md` file.

---

## Tree Traversal Overview <a name="tree-traversal-overview"></a>

Tree traversal refers to the process of visiting all the nodes in a tree data structure in a specific order. There are two main categories of tree traversal:

1. **Depth-First Traversal**: Traverses the tree by exploring as far as possible along each branch before backtracking.
   - Pre-order Traversal
   - In-order Traversal
   - Post-order Traversal

2. **Breadth-First Traversal**: Traverses the tree level by level, visiting all nodes at the current level before moving to the next level.
   - Level-order Traversal (BFS)

---

## Pre-order Traversal <a name="pre-order-traversal"></a>

Implement a `pre_order_traversal` method that performs a pre-order traversal of the tree. The method should:

1. **Visit the root node**.
2. **Recursively traverse the left subtree**.
3. **Recursively traverse the right subtree**.
4. Return a list of values in the order they were visited.

**Example**:
```python
def pre_order_traversal(root):
    if root is None:
        return []
    return [root.value] + pre_order_traversal(root.left) + pre_order_traversal(root.right)
```

---

## In-order Traversal <a name="in-order-traversal"></a>

Implement an `in_order_traversal` method that performs an in-order traversal of the tree. The method should:

1. **Recursively traverse the left subtree**.
2. **Visit the root node**.
3. **Recursively traverse the right subtree**.
4. Return a list of values in the order they were visited.

**Example**:
```python
def in_order_traversal(root):
    if root is None:
        return []
    return in_order_traversal(root.left) + [root.value] + in_order_traversal(root.right)
```

---

## Post-order Traversal <a name="post-order-traversal"></a>

Implement a `post_order_traversal` method that performs a post-order traversal of the tree. The method should:

1. **Recursively traverse the left subtree**.
2. **Recursively traverse the right subtree**.
3. **Visit the root node**.
4. Return a list of values in the order they were visited.

**Example**:
```python
def post_order_traversal(root):
    if root is None:
        return []
    return post_order_traversal(root.left) + post_order_traversal(root.right) + [root.value]
```

---

## Level-order Traversal (BFS) <a name="level-order-traversal"></a>

Implement a `level_order_traversal` method that performs a level-order traversal (Breadth-First Search) of the tree. The method should:

1. Use a **queue** to traverse the tree level by level.
2. Start from the root node and enqueue it.
3. While the queue is not empty:
   - Dequeue a node and visit it.
   - Enqueue its left and right children (if they exist).
4. Return a list of values in the order they were visited.

**Example**:
```python
from collections import deque

def level_order_traversal(root):
    if root is None:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
```

---

## Depth-First Search (DFS) <a name="depth-first-search"></a>

Implement a `dfs` method that performs a depth-first search traversal of the tree. The method should:

1. Use a **stack** or **recursion** to traverse the tree.
2. Start from the root node and explore as far as possible along each branch before backtracking.
3. Return a list of values in the order they were visited.

**Example (Recursive)**:
```python
def dfs(root):
    if root is None:
        return []
    return [root.value] + dfs(root.left) + dfs(root.right)
```

**Example (Iterative)**:
```python
def dfs(root):
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
```

---

## Breadth-First Search (BFS) <a name="breadth-first-search"></a>

Implement a `bfs` method that performs a breadth-first search traversal of the tree. The method should:

1. Use a **queue** to traverse the tree level by level.
2. Start from the root node and enqueue it.
3. While the queue is not empty:
   - Dequeue a node and visit it.
   - Enqueue its left and right children (if they exist).
4. Return a list of values in the order they were visited.

**Example**:
```python
from collections import deque

def bfs(root):
    if root is None:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
```

---

## Iterative Traversal Methods <a name="iterative-traversal-methods"></a>

For scenarios where recursion is not preferred, implement iterative versions of the traversal methods using stacks or queues.

### Iterative Pre-order Traversal
```python
def pre_order_traversal_iterative(root):
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
```

### Iterative In-order Traversal
```python
def in_order_traversal_iterative(root):
    if root is None:
        return []
    stack = []
    result = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    return result
```

### Iterative Post-order Traversal
```python
def post_order_traversal_iterative(root):
    if root is None:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]  # Reverse the result to get post-order
```

---

This guide provides a structured approach to implementing various tree traversal algorithms, including recursive and iterative methods