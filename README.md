# MLA0107 – Artificial Intelligence & Expert Systems For Dynamic Agent Architectures Lab Programs

This repository contains implementations of **Artificial Intelligence and Expert Systems (AI & ES) laboratory programs** using Python.

Each program includes:
- Python source code (.py)
- Output screenshots
- Algorithm pseudocode

---


# 1. Breadth First Search (BFS)

## Problem
Traverse a graph using Breadth First Search starting from a given node.

## Pseudocode

```
BFS(Graph, StartNode)

1. Create an empty list called visited
2. Create an empty queue

3. Add StartNode to visited
4. Add StartNode to queue

5. While queue is not empty:

      Remove first element from queue → node
      Print node

      For each neighbour of node:

            If neighbour is not in visited:
                  Add neighbour to visited
                  Add neighbour to queue
```

---

# 2. Depth First Search (DFS)

## Problem
Traverse a graph using Depth First Search.

## Pseudocode

```
DFS(Graph, Node, Visited)

1. If Node is not in Visited:

      Print Node
      Add Node to Visited

2. For each neighbour of Node:

      Call DFS(Graph, neighbour, Visited)
```

---

# 3. Uniform Cost Search (UCS)

## Problem
Find the least cost path from a start node to a goal node in a weighted graph.

## Pseudocode

```
UCS(Graph, Start, Goal)

1. Create a list called queue storing (node, cost)

2. Insert (Start, 0) into queue

3. Create an empty visited list

4. While queue is not empty:

      Find node with minimum cost
      Remove it from queue

      If node already visited:
            Continue

      Add node to visited

      If node equals Goal:
            Print cost
            Stop

      For each neighbour of node:

            Add (neighbour, cost + weight) to queue
```

---

# 4. Water Jug Problem

## Problem
Measure a target amount of water using two jugs of given capacities.

## Pseudocode

```
WaterJug(Jug1Capacity, Jug2Capacity, Target)

1. Start with initial state (0,0)

2. Create visited list

3. Create queue and add (0,0)

4. While queue is not empty:

      Remove first state (x,y)

      If state already visited:
            Continue

      Print state
      Add state to visited

      If x == Target OR y == Target:
            Print "Target Achieved"
            Stop

5. Perform all possible operations:

      Fill Jug1
      Fill Jug2
      Empty Jug1
      Empty Jug2
      Pour Jug1 → Jug2
      Pour Jug2 → Jug1
```

