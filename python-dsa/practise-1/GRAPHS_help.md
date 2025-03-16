# Graphs: Implementation Guide

## Table of Contents

* [Graph Class](#graph-class)
* [Vertex Class](#vertex-class)
* [Graph: Add Vertex](#graph-add-vertex)
* [Graph: Add Edge](#graph-add-edge)
* [Graph: Remove Vertex](#graph-remove-vertex)
* [Graph: Remove Edge](#graph-remove-edge)
* [Graph: Depth-First Search (DFS)](#graph-depth-first-search)
* [Graph: Breadth-First Search (BFS)](#graph-breadth-first-search)
* [Graph: Shortest Path (Dijkstra's Algorithm)](#graph-shortest-path-dijkstra)
* [Graph: Detect Cycle](#graph-detect-cycle)
* [Graph: Topological Sort](#graph-topological-sort)

Design and implement a Python program that defines classes for a graph and its vertices.

## Graph Class <a name="graph-class"></a>

Create a class called `Graph`, which will represent a graph data structure. The class should have the following attributes:

*   `vertices`: A dictionary to store the vertices of the graph, where the keys are the vertex labels and the values are instances of the `Vertex` class.
*   `directed`: A boolean indicating whether the graph is directed (`True`) or undirected (`False`).

When initializing a new instance of the `Graph` class, the user should specify whether the graph is directed or undirected. The `vertices` dictionary should be initialized as empty.

## Vertex Class <a name="vertex-class"></a>

Create a class called `Vertex`, which will represent a single vertex in the graph. The class should have the following attributes:

*   `label`: The label or identifier of the vertex.
*   `edges`: A list to store the edges connected to this vertex. Each edge can be represented as a tuple `(destination_vertex, weight)`.

When initializing a new instance of the `Vertex` class, the user should provide a label for the vertex. The `edges` list should be initialized as empty.

## Graph: Add Vertex <a name="graph-add-vertex"></a>

Implement an `add_vertex` method that adds a new vertex to the graph. The method should:

1.  Check if the vertex already exists in the `vertices` dictionary.
2.  If the vertex does not exist, create a new `Vertex` instance and add it to the `vertices` dictionary.
3.  Return `True` if the vertex is added, otherwise return `False`.

## Graph: Add Edge <a name="graph-add-edge"></a>

Implement an `add_edge` method that adds an edge between two vertices. The method should:

1.  Check if both vertices exist in the `vertices` dictionary.
2.  If both vertices exist, add an edge from the source vertex to the destination vertex in the `edges` list of the source vertex.
3.  If the graph is undirected, also add an edge from the destination vertex to the source vertex.
4.  Return `True` if the edge is added, otherwise return `False`.

## Graph: Remove Vertex <a name="graph-remove-vertex"></a>

Implement a `remove_vertex` method that removes a vertex and all its associated edges from the graph. The method should:

1.  Check if the vertex exists in the `vertices` dictionary.
2.  If the vertex exists, remove it from the `vertices` dictionary.
3.  Remove all edges pointing to the removed vertex from other vertices.
4.  Return `True` if the vertex is removed, otherwise return `False`.

## Graph: Remove Edge <a name="graph-remove-edge"></a>

Implement a `remove_edge` method that removes an edge between two vertices. The method should:

1.  Check if both vertices exist in the `vertices` dictionary.
2.  If both vertices exist, remove the edge from the source vertex to the destination vertex.
3.  If the graph is undirected, also remove the edge from the destination vertex to the source vertex.
4.  Return `True` if the edge is removed, otherwise return `False`.

## Graph: Depth-First Search (DFS) <a name="graph-depth-first-search"></a>

Implement a `dfs` method that performs a depth-first search traversal of the graph starting from a given vertex. The method should:

1.  Check if the starting vertex exists in the `vertices` dictionary.
2.  Use a stack or recursion to traverse the graph, visiting each vertex and its neighbors in depth-first order.
3.  Return a list of visited vertices in the order they were visited.

## Graph: Breadth-First Search (BFS) <a name="graph-breadth-first-search"></a>

Implement a `bfs` method that performs a breadth-first search traversal of the graph starting from a given vertex. The method should:

1.  Check if the starting vertex exists in the `vertices` dictionary.
2.  Use a queue to traverse the graph, visiting each vertex and its neighbors in breadth-first order.
3.  Return a list of visited vertices in the order they were visited.

## Graph: Shortest Path (Dijkstra's Algorithm) <a name="graph-shortest-path-dijkstra"></a>

Implement a `shortest_path` method that finds the shortest path between two vertices using Dijkstra's algorithm. The method should:

1.  Check if both vertices exist in the `vertices` dictionary.
2.  Use Dijkstra's algorithm to compute the shortest path from the source vertex to the destination vertex.
3.  Return the shortest path as a list of vertices and the total weight of the path.

## Graph: Detect Cycle <a name="graph-detect-cycle"></a>

Implement a `detect_cycle` method that detects whether the graph contains a cycle. The method should:

1.  Use Depth-First Search (DFS) or Union-Find (Disjoint Set Union) to detect cycles.
2.  Return `True` if a cycle is detected, otherwise return `False`.

## Graph: Topological Sort <a name="graph-topological-sort"></a>

Implement a `topological_sort` method that performs a topological sort on a directed acyclic graph (DAG). The method should:

1.  Check if the graph is directed.
2.  Use Depth-First Search (DFS) to perform the topological sort.
3.  Return a list of vertices in topological order.

---

This guide provides a structured approach to implementing a graph and its common operations