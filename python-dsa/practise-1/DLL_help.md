# DLL: Constructor

## Table of Contents

* [Node Class](#node-class)
* [DoublyLinkedList Class](#doubly-linked-list-class)
* [DLL: Append](#dll-append)
* [DLL: Pop](#dll-pop)
* [DLL: Prepend](#dll-prepend)
* [DLL: Pop First](#dll-pop-first)
* [DLL: Get](#dll-get)
* [DLL: Set](#dll-set)
* [DLL: Insert](#dll-insert)
* [DLL: Remove](#dll-remove)
* [DLL: Reverse](#dll-reverse)

Design and implement a Python program that defines two classes: `Node` and `DoublyLinkedList`.

## Node Class <a name="node-class"></a>

Create a class called `Node`, which will represent a single node in a doubly-linked list. The class should have the following attributes:

*   `value`: The data contained in the node.
*   `next`: A reference to the next node in the list.
*   `prev`: A reference to the previous node in the list.

## DoublyLinkedList Class <a name="doubly-linked-list-class"></a>

Create a class called `DoublyLinkedList`, which will represent a doubly-linked list. The class should have the following attributes:

*   `head`: A reference to the head (first) node of the list.
*   `tail`: A reference to the tail (last) node of the list.
*   `length`: An integer representing the number of nodes in the list.

When initializing a new instance of the `DoublyLinkedList` class, the user should provide a value for the first node. The constructor should create a new instance of the `Node` class using the provided value and assign it as both the `head` and `tail` of the list. The `length` attribute should be initialized to `1`.

## DLL: Append <a name="dll-append"></a>

Extend the `DoublyLinkedList` class by adding an `append` method that inserts a new node with a given value at the end of the list. The method should:

1.  Create a new `Node` with the provided value.
2.  If the list is empty (`head` is `None`), set the `head` and `tail` to the new node.
3.  If the list is not empty:
    *   Set the `next` of the current `tail` to the new node.
    *   Set the `prev` of the new node to the current `tail`.
    *   Update the `tail` to the new node.
4.  Increment the `length` by `1`.
5.  Return `True`.

## DLL: Pop <a name="dll-pop"></a>

Add a `pop` method to the `DoublyLinkedList` class that removes the last node and returns it. The method should:

1.  Return `None` if the list is empty.
2.  Store the current `tail` in a temporary variable.
3.  If the list has one node, set `head` and `tail` to `None`.
4.  If the list has more than one node:
    *   Update the `tail` to the previous node of the current `tail`.
    *   Set the new `tail.next` to `None`.
    *   Set the removed node’s `prev` to `None`.
5.  Decrement the `length` by `1`.
6.  Return the removed node.

## DLL: Prepend <a name="dll-prepend"></a>

Implement a `prepend` method that inserts a new node at the beginning of the list. The method should:

1.  Create a new `Node` with the provided value.
2.  If the list is empty, set `head` and `tail` to the new node.
3.  If the list is not empty:
    *   Set the `next` of the new node to the current `head`.
    *   Set the `prev` of the current `head` to the new node.
    *   Update the `head` to the new node.
4.  Increment the `length` by `1`.
5.  Return `True`.

## DLL: Pop First <a name="dll-pop-first"></a>

Implement a `pop_first` method that removes the first node and returns it. The method should:

1.  Return `None` if the list is empty.
2.  Store the current `head` in a temporary variable.
3.  If the list has one node, set `head` and `tail` to `None`.
4.  If the list has more than one node:
    *   Update the `head` to the `next` node of the current `head`.
    *   Set the new `head.prev` to `None`.
    *   Set the removed node’s `next` to `None`.
5.  Decrement the `length` by `1`.
6.  Return the removed node.

## DLL: Get <a name="dll-get"></a>

Implement a `get` method that retrieves a node at a specific index. The method should:

1.  Return `None` if the index is out of bounds (less than `0` or greater than or equal to `length`).
2.  Start from the `head` if the index is in the first half of the list.
3.  Start from the `tail` if the index is in the second half of the list.
4.  Traverse to the desired index and return the node.

## DLL: Set <a name="dll-set"></a>

Implement a `set_value` method that updates the value of a node at a specific index. The method should:

1.  Use the `get` method to retrieve the node at the index.
2.  Update the node’s value if it exists and return `True`.
3.  Return `False` if the node does not exist.

## DLL: Insert <a name="dll-insert"></a>

Implement an `insert` method that inserts a new node at a specific index. The method should:

1.  Return `False` if the index is out of bounds (less than `0` or greater than `length`).
2.  Use `prepend` if the index is `0`.
3.  Use `append` if the index equals `length`.
4.  Create a new node and link it between the nodes at positions `index-1` and `index`.
5.  Adjust the `prev` and `next` pointers of the surrounding nodes.
6.  Increment the `length` by `1`.
7.  Return `True`.

## DLL: Remove <a name="dll-remove"></a>

Implement a `remove` method that removes a node at a specific index and returns it. The method should:

1.  Return `None` if the index is out of bounds.
2.  Use `pop_first` if the index is `0`.
3.  Use `pop` if the index is `length-1`.
4.  Retrieve the node to remove using `get`.
5.  Adjust the `prev` and `next` pointers of the surrounding nodes to bypass the removed node.
6.  Set the removed node’s `prev` and `next` to `None`.
7.  Decrement the `length` by `1`.
8.  Return the removed node.

## DLL: Reverse <a name="dll-reverse"></a>

Implement a `reverse` method that reverses the list. The method should:

1.  Swap the `head` and `tail` pointers.
2.  Traverse the list, swapping the `prev` and `next` pointers of each node.
3.  Ensure no new nodes are created, and node values are not modified.
4.  Maintain the integrity of the `head` and `tail` after reversal.