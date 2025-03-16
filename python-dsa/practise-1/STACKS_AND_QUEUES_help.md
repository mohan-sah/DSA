# Stack and Queues: Implementation Guide

## Table of Contents

* [Stack Class](#stack-class)
* [Queue Class](#queue-class)
* [Stack: Push](#stack-push)
* [Stack: Pop](#stack-pop)
* [Stack: Peek](#stack-peek)
* [Stack: Is Empty](#stack-is-empty)
* [Queue: Enqueue](#queue-enqueue)
* [Queue: Dequeue](#queue-dequeue)
* [Queue: Peek](#queue-peek)
* [Queue: Is Empty](#queue-is-empty)

Design and implement a Python program that defines two classes: `Stack` and `Queue`.

## Stack Class <a name="stack-class"></a>

Create a `Stack` class that represents a last-in, first-out (LIFO) data structure using a linked list implementation.

The `Stack` class should contain the following components:

1. A `Node` class, which serves as the building block for the linked list. The `Node` class should have an `__init__` method that initializes the following attributes:

   * `value`: The value of the node.

   *   `next`: A reference to the next node in the list, initialized to None.

2. The `Stack` class should have an `__init__` method that initializes the stack with a single node, using the given value. The `__init__` method should perform the following tasks:

   *   Create a new instance of the Node class using the provided value.

   *   Set the top attribute of the Stack class to point to the new node.

   *   Initialize a height attribute for the Stack class, which represents the current number of nodes in the stack, and set it to 1.

## Queue Class <a name="queue-class"></a>

Create a class called `Queue`, which will represent a queue data structure. The class should have the following attributes:

1. A `Node` class, which serves as the building block for the linked list. The Node class should have an __init__ method that initializes the following attributes:

   *   `value`: The value of the node.

   *   `next`: A reference to the next node in the list, initialized to None.

2. The `Queue` class should have an `__init__` method that initializes the queue with a single node, using the given value. The `__init__` method should perform the following tasks:

   *   Create a new instance of the `Node` class using the provided value.

   *   Set the `first` attribute of the Queue class to point to the new node.

   *   Set the `last` attribute of the Queue class to point to the new node.

   *   Initialize a `length` attribute for the Queue class, which represents the current number of nodes in the queue, and set it to 1.

## Stack: Push <a name="stack-push"></a>

Implement the `push` method for the Stack class that adds a new node with a given value to the top of the stack.

The method should perform the following tasks:


1. Create a new instance of the `Node` class using the provided value.

2. Set the `next` attribute of the new node to point to the current top node.

3. Update the `top` attribute of the Stack class to point to the new node.

4. Increment the `height` attribute of the Stack class by 1.

## Stack: Pop <a name="stack-pop"></a>

Add a `pop` method to the `Stack` class that removes and returns the top element of the stack. The method should:

1.  If the stack is empty (i.e., the `height` is 0), return None.

2. Store a reference to the current top node in a temporary variable, `temp`.

3. Update the `top` attribute of the Stack class to point to the next node in the stack.

4. Set the next attribute of the removed node (stored in the temporary variable) to None.

5. Decrement the `height` attribute of the Stack class by 1.

6. Return the removed node (stored in the temporary variable).

## Stack: Peek <a name="stack-peek"></a>

Implement a `peek` method that returns the top element of the stack without removing it. The method should:

1.  Return `None` if the stack is empty.
2.  Return the last element from the `items` list.

## Stack: Is Empty <a name="stack-is-empty"></a>

Implement an `is_empty` method that checks if the stack is empty. The method should:

1.  Return `True` if the `items` list is empty.
2.  Return `False` otherwise.

## Queue: Enqueue <a name="queue-enqueue"></a>

Extend the `Queue` class by adding an `enqueue` method that adds an element to the end of the queue. The method should:

1.  Create a new instance of the `Node` class using the provided value.

2.  If the queue is empty (i.e., `self.first` is None), set the `first` and `last` attributes of the Queue class to point to the new node.

3.  If the queue is not empty, perform the following steps:

   *   Set the `next` attribute of the current last node to point to the new node.

   * Update the `last` attribute of the Queue class to point to the new node.

4.  Increment the `length` attribute of the Queue class by 1.


## Queue: Dequeue <a name="queue-dequeue"></a>

Add a `dequeue` method to the `Queue` class that removes and returns the front element of the queue. The method should:

1. If the queue is empty (i.e., the length is 0), return None.

2. Store a reference to the current first node in a temporary variable, temp.

3. If the queue has only one node (i.e., the length is 1), set both the first and last attributes of the Queue class to None.

4. If the queue has more than one node, perform the following steps:

   *   Update the first attribute of the Queue class to point to the next node in the queue.

   *   Set the next attribute of the removed node (stored in the temporary variable) to None.

5. Decrement the length attribute of the Queue class by 1.

6. Return the removed node (stored in the temporary variable).

## Queue: Peek <a name="queue-peek"></a>

Implement a `peek` method that returns the front element of the queue without removing it. The method should:

1.  Return `None` if the queue is empty.
2.  Return the first element from the `items` list.

## Queue: Is Empty <a name="queue-is-empty"></a>

Implement an `is_empty` method that checks if the queue is empty. The method should:

1.  Return `True` if the `items` list is empty.
2.  Return `False` otherwise.