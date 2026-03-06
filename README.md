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
---

# 5. A* Search Algorithm

## Problem
Find the optimal path from a start node to a goal node using A* Search.

## Pseudocode

```
AStar(Graph, Heuristic, Start, Goal)

1. Create a list called open_list
2. Insert (Start, cost = 0)

3. Create empty visited list

4. While open_list is not empty:

      Select node with minimum f(n)

      Remove it from open_list

      If node already visited:
            Continue

      Print node
      Add node to visited

      If node equals Goal:
            Print "Goal reached"
            Stop

      For each neighbour:

            g = cost + edge_weight
            h = heuristic(neighbour)

            f = g + h

            Add (neighbour, f) to open_list
```
---

# 5. A* Search Algorithm

## Problem
Find the optimal path from a start node to a goal node in a weighted graph using A* Search.

## Pseudocode

```
AStar(Graph, Heuristic, Start, Goal)

1. Create an open_list containing:
       (node, cost_from_start, path)

2. Add (Start, 0, [Start]) to open_list

3. Create an empty list called closed

4. While open_list is not empty:

       Select node with lowest
       f(n) = g(n) + h(n)

       Remove that node from open_list

       If node == Goal:
             Print path
             Print total cost
             Stop

       Add node to closed

       For each neighbour of node:

             If neighbour not in closed:

                   new_cost = g + edge_cost

                   Add (neighbour, new_cost, updated_path)
                   to open_list
```
---

# 6. Alpha-Beta Pruning

## Problem
Optimize the Minimax algorithm by eliminating branches of the game tree that cannot influence the final decision.

## Pseudocode

```
AlphaBeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta)

1. If depth == maximum depth:
       Return value of leaf node

2. If maximizingPlayer:

       best = -∞

       For each child node:

             val = AlphaBeta(depth+1, childIndex, False, values, alpha, beta)

             best = max(best, val)

             alpha = max(alpha, best)

             If beta <= alpha:
                    Break   // Beta Cutoff (pruning)

       Return best

3. Else (minimizing player):

       best = +∞

       For each child node:

             val = AlphaBeta(depth+1, childIndex, True, values, alpha, beta)

             best = min(best, val)

             beta = min(beta, best)

             If beta <= alpha:
                    Break   // Alpha Cutoff (pruning)

       Return best
```
---

# 7. Decision Tree (ID3 Algorithm)

## Problem
Construct a decision tree from a dataset using the ID3 algorithm based on Information Gain.

## Pseudocode

```
Entropy(Data)

1. Count number of positive and negative examples
2. Compute probabilities:
       p1 = positive / total
       p2 = negative / total
3. If either probability is 0:
       Return 0
4. Return entropy value:
       - (p1 log2 p1 + p2 log2 p2)


InformationGain(Data, Attribute)

1. Compute entropy of entire dataset
2. Partition data according to values of Attribute
3. For each partition:
       Compute entropy
       Multiply by proportion of samples
4. Sum all partition entropies
5. Information Gain =
       Total entropy - Weighted partition entropy
6. Return Information Gain


BuildTree(Data, Attributes)

1. If all examples belong to same class:
       Return that class label

2. If Attributes list is empty:
       Return majority class

3. Compute Information Gain for each attribute

4. Select attribute with highest gain → BestAttribute

5. Create a decision node for BestAttribute

6. For each value of BestAttribute:

       Create subset of data with that value

       If subset is empty:
             Attach majority class

       Else:
             Recursively call BuildTree on subset
             with remaining attributes

7. Return the constructed tree
```
---

# 8. Minimax Algorithm

## Problem
Determine the optimal value for a player in a two-player game tree assuming both players play optimally.

## Pseudocode

```
MiniMax(depth, nodeIndex, isMaximizingPlayer, values)

1. If depth == maximum depth:
       Return value of leaf node

2. If isMaximizingPlayer is TRUE:

       Return maximum of
            MiniMax(depth + 1, nodeIndex*2, False, values)
            MiniMax(depth + 1, nodeIndex*2 + 1, False, values)

3. Else (Minimizing Player):

       Return minimum of
            MiniMax(depth + 1, nodeIndex*2, True, values)
            MiniMax(depth + 1, nodeIndex*2 + 1, True, values)
```
---

# 9. Greedy Best First Search (GBFS)

## Problem
Find a path from a start node to a goal node using the Greedy Best First Search strategy, which expands the node with the lowest heuristic value.

## Pseudocode

```
GBFS(Graph, Heuristic, Start, Goal)

1. Create an open_list containing:
       (node, path, heuristic_value)

2. Insert (Start, [Start], h(Start)) into open_list

3. Create an empty visited list

4. While open_list is not empty:

       Select node with smallest heuristic value

       Remove that node from open_list

       If node == Goal:
             Print path
             Print cost
             Stop

       Add node to visited

       For each neighbour of node:

             If neighbour not in visited:

                   Add (neighbour,
                        updated_path,
                        heuristic_cost)
                   to open_list
```