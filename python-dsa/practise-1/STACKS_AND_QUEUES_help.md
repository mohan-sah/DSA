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

Create a class called `Stack`, which will represent a stack data structure. The class should have the following attributes:

*   `items`: A list to store the elements of the stack.

When initializing a new instance of the `Stack` class, the `items` list should be empty.

## Queue Class <a name="queue-class"></a>

Create a class called `Queue`, which will represent a queue data structure. The class should have the following attributes:

*   `items`: A list to store the elements of the queue.

When initializing a new instance of the `Queue` class, the `items` list should be empty.

## Stack: Push <a name="stack-push"></a>

Extend the `Stack` class by adding a `push` method that adds an element to the top of the stack. The method should:

1.  Append the provided value to the `items` list.
2.  Return `True`.

## Stack: Pop <a name="stack-pop"></a>

Add a `pop` method to the `Stack` class that removes and returns the top element of the stack. The method should:

1.  Return `None` if the stack is empty.
2.  Remove and return the last element from the `items` list.

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

1.  Append the provided value to the `items` list.
2.  Return `True`.

## Queue: Dequeue <a name="queue-dequeue"></a>

Add a `dequeue` method to the `Queue` class that removes and returns the front element of the queue. The method should:

1.  Return `None` if the queue is empty.
2.  Remove and return the first element from the `items` list.

## Queue: Peek <a name="queue-peek"></a>

Implement a `peek` method that returns the front element of the queue without removing it. The method should:

1.  Return `None` if the queue is empty.
2.  Return the first element from the `items` list.

## Queue: Is Empty <a name="queue-is-empty"></a>

Implement an `is_empty` method that checks if the queue is empty. The method should:

1.  Return `True` if the `items` list is empty.
2.  Return `False` otherwise.