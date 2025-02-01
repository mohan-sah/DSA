# LL: Constructor

## Table of Contents
 
*   [Node Class](#node-class)
*   [LinkedList Class](#linked-list-class)
*   [LL: Print List](#ll-print-list)
*   [LL: Append](#ll-append)
*   [LL: Pop](#ll-pop)
*   [LL: Prepend](#ll-prepend)
*   [LL: Pop First](#ll-pop-first)
*   [LL: Get](#ll-get)
*   [LL: Set](#ll-set)
*   [LL: Insert](#ll-insert)
*   [LL: Remove](#ll-remove)
*   [LL: Reverse](#ll-reverse)

You are tasked with implementing a basic data structure: a singly linked list.

To accomplish this, you will create two classes, `Node` and `LinkedList`.

The `Node` class will represent an individual node within the linked list, while the `LinkedList` class will manage the overall list structure.

Your implementation should satisfy the following requirements:

## Node Class <a name="node-class"></a>

Create a `Node` class with the following features:

*   A constructor that takes a `value` as an argument and initializes the `value` attribute of the node.
*   A `next` attribute, initialized to `None`, which will store a reference to the next node in the list.

## LinkedList Class <a name="linked-list-class"></a>

Create a `LinkedList` class with the following features:

*   A constructor that takes a `value` as an argument, creates a new `Node` with that value, and initializes the `head` and `tail` attributes of the linked list to point to the new node.
*   A `length` attribute, initialized to `1`, which represents the current number of nodes in the list.

## LL: Print List <a name="ll-print-list"></a> 

Implement a method `print_list(self)` that prints the linked list's elements, one per line.

## LL: Append <a name="ll-append"></a>

Implement the `append` method for the `LinkedList` class.

The `append` method should add a new node with a given value to the end of the linked list, updating the `tail` attribute and the `length` attribute accordingly.

Keep in mind the following requirements:

*   The method should handle the cases where the list is empty and where the list already has one or more nodes.
*   The method should create a new node with the given value and add it to the end of the list.
*   The method should update the `tail` attribute of the `LinkedList` correctly.
*   The method should update the `length` attribute of the `LinkedList` to reflect the addition of the new node.

## LL: Pop <a name="ll-pop"></a>

Your task is to implement the `pop` method for the `LinkedList` class.

The `pop` method should remove the last node (`tail`) from the linked list and return the removed node. If the list is empty, the method should return `None`.

After the last node is removed, the second-to-last node should become the new tail of the list.

Additionally, if the list becomes empty after the `pop` operation, both the `head` and `tail` attributes should be set to `None`.

Keep in mind the following requirements:

*   The method should handle the cases where the list is empty, has only one node, or has multiple nodes.
*   The method should update the `tail` attribute of the `LinkedList` correctly.
*   The method should update the `length` attribute of the `LinkedList` to reflect the removal of the node.
*   The method should either return the removed node or `None` if the list is empty.

## LL: Prepend <a name="ll-prepend"></a>

Implement the `prepend` method for the `LinkedList` class.

The `prepend` method should add a new node with a given value to the beginning of the linked list, updating the `head` attribute and the `length` attribute accordingly.

Keep in mind the following requirements:

*   The method should handle the cases where the list is empty and where the list already has one or more nodes.
*   The method should create a new node with the given value and add it to the beginning of the list.
*   The method should update the `head` attribute of the `LinkedList` correctly.
*   The method should update the `length` attribute of the `LinkedList` to reflect the addition of the new node.
*   The method should return `True` if the operation is successful.

## LL: Pop First <a name="ll-pop-first"></a>

Implement the `pop_first` method for the `LinkedList` class.

The `pop_first` method should remove the first node (the `head`) from the linked list, update the `head` attribute and the `length` attribute accordingly, and return the removed node.

Keep in mind the following requirements:

*   The method should handle the cases where the list is empty and where the list has one or more nodes.
*   The method should save a reference to the current head node before updating the `head` attribute.
*   The method should update the `head` attribute to the second node in the list.
*   The method should disconnect the removed node from the list by setting its `next` attribute to `None`.
*   The method should update the `length` attribute of the `LinkedList` to reflect the removal of the node.
*   If the list becomes empty after removing the node, the method should set the `tail` attribute of the `LinkedList` to `None`.
*   The method should return the removed node, or `None` if the list is empty.

## LL: Get <a name="ll-get"></a>

Implement the `get` method for the `LinkedList` class.

The `get` method should take an integer index as a parameter and return a pointer to the node at the specified index in the linked list.

If the index is out of bounds (less than 0 or greater than or equal to the length of the list), the method should return `None`.

Keep in mind the following requirements:

*   The method should handle the cases where the index is out of bounds.
*   The method should start at the head of the list and traverse the list using the `next` attribute of the nodes.
*   The method should stop traversing the list when it reaches the specified index and return the node at that position.
*   If the index is out of bounds, the method should return `None`.

## LL: Set <a name="ll-set"></a> 

Implement the `set_value` method for the `LinkedList` class.

The `set_value` method should take an integer index and a value as parameters and update the value of the node at the specified index in the linked list.

If the index is out of bounds, the method should return `False`. If the value is successfully updated, the method should return `True`.

Keep in mind the following requirements:

*   The method should utilize the `get` method to find the node at the specified index.
*   The method should update the value of the node if the node is found.
*   The method should return `True` if the value is successfully updated.
*   If the node is not found (i.e., the index is out of bounds), the method should return `False`.

## LL: Insert <a name="ll-insert"></a>

Implement the `insert` method for the `LinkedList` class.

Method signature: `def insert(self, index, value):`

The `insert` method should take an integer index and a value as parameters and insert a new node with the given value at the specified index in the linked list.

If the index is out of bounds, the method should return `False`. If the new node is successfully inserted, the method should return `True`.

Keep in mind the following requirements:

*   The method should handle edge cases, such as inserting a new node at the beginning or end of the list.
*   The method should utilize the `prepend`, `append`, and `get` methods for handling these edge cases.
*   The method should create a new node with the given value and insert it at the specified index.
*   The method should update the `next` attribute of the previous node to point to the new node.
*   The method should increment the `length` attribute of the `LinkedList` class.
*   The method should return `True` if the new node is successfully inserted.
*   If the index is out of bounds, the method should return `False`.

## LL: Remove <a name="ll-remove"></a>

Implement the `remove` method for the `LinkedList` class.

The `remove` method should take an integer `index` as a parameter and remove the node at the specified index in the linked list, returning the removed node.

If the index is out of bounds, the method should return `None`.

Keep in mind the following requirements:

*   The method should handle edge cases, such as removing a node at the beginning or end of the list.
*   The method should utilize the `pop_first()` and `pop()` methods for handling these edge cases.
*   The method should use the `get()` method to find the node previous to the one to be removed.
*   The method should update the `next` attribute of the previous node to point to the node after the removed one.
*   The method should decrement the `length` attribute of the `LinkedList` class.
*   The method should return the removed node if the removal is successful.
*   If the index is out of bounds, the method should return `None`.

## LL: Reverse <a name="ll-reverse"></a>

Implement the `reverse` method for the `LinkedList` class.

The `reverse` method should reverse the order of the nodes in the linked list so that the head becomes the tail and the tail becomes the head.

The method should not create any new nodes or modify the values of the nodes.

The method should only update the `next` attribute of each node to point to the previous node in the list.

Consider the following requirements while implementing the method:

*   The method should handle edge cases, such as an empty list or a list with a single node.
*   The method should utilize a temporary variable to swap the head and tail attributes of the `LinkedList` class.  (This might not be strictly necessary in all implementations, but it's a common approach.)
*   The method should use a loop to iterate through the nodes in the list and update the `next` attribute of each node.
*   The method should not modify the `length` attribute of the `LinkedList` class.

Here's a more detailed breakdown of a common approach to reversing a linked list:

1.  **Handle Edge Cases:** Check if the list is empty or has only one node. If so, there's nothing to reverse, so return (or handle as appropriate for your class).

2.  **Initialize Pointers:** You'll typically need three pointers:
    *   `previous`: Initially `None`.  This will track the reversed portion of the list.
    *   `current`: Initially the `head` of the list.  This is the node you're currently processing.
    *   `next_node`: Initially the node after `current` (i.e., `current.next`). This is needed to avoid losing the rest of the list when you reverse the `current` node's `next` pointer.

3.  **Iterate and Reverse:**  Loop while `current` is not `None`:
    *   Store `current.next` in `next_node`.
    *   Reverse the `current` node's `next` pointer: `current.next = previous`.
    *   Move `previous` one step forward: `previous = current`.
    *   Move `current` one step forward: `current = next_node`.

4.  **Update Head and Tail:** After the loop, `previous` will be pointing to the new head of the reversed list.  Update `self.head` to `previous`.  The original head is now the tail. Update `self.tail` to the node that was originally the head.

Example (Conceptual):

Let's say you have a list:  1 -> 2 -> 3 -> None

*   Initially: `previous` = None, `current` = 1, `next_node` = 2
*   1st iteration: `current.next` (1 -> 2) becomes `None` (1 -> None), `previous` becomes 1, `current` becomes 2
*   2nd iteration: `current.next` (2 -> 3) becomes 1 (2 -> 1), `previous` becomes 2, `current` becomes 3
*   3rd iteration: `current.next` (3 -> None) becomes 2 (3 -> 2), `previous` becomes 3, `current` becomes None
*   Loop ends.  `head` becomes 3, `tail` becomes 1.  Result: 3 -> 2 -> 1 -> None