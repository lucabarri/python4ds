# Functions

## Problem 1

Write a program that receives a dictionary with floating point values (arbitrary keys) and returns a new dictionary with keys sorted by values.

__Example.__

```
Input: {'Person1': 22, 'Person2': 35, 'Person3': 5, 'Person4': 53}
Output: {'Person3': 5, 'Person1': 22, 'Person2': 35, 'Person4': 53}
```

## Problem 2

The factorial of a non-negative integer $n$, denoted by $n!$, is defined as,

$n! = n \times (n-1) \times \cdots \times 2 \times 1$

Henceforth let $f(n) = n!$

### Problem 2.1

From the definition of factorial, derive an expression of $f(n)$ in terms of $f(n-1)$.

### Problem 2.2

From the recursive definition in Step 1, program a function $f(n)$ that returns $n!$.

## Problem 3

### Problem 3.1

The Fibonacci sequence is defined as follows,

$$f(1) = 1, f(2) = 1,$$

$$f(n) = f(n-1) + f(n-2)$$

write a recursive program that computes $f(n)$.

### Problem 3.2

Based on your last program, write a recursive program that stores $f(i)$ on a list, for $i=1,\cdots,n$.

## Problem 4

### Problem 4.1

Write a sequential program that converts a decimal number into binary.

### Problem 4.2

Rewrite your program using a recursive function.

## Problem 5

Assume that $x$ is a monotonically non-decreasing array, i.e., $x_{0} \leq x_{2} \leq \cdots \leq x_{n-1}$. Implement an algorithm that receives a searched value $x_{0}$. The algorithm follows the steps,

1. Compare the middle element of $x_{m}$ to $x_{0}$.
2. IF $x_{m} = x_{0}$, returns $m$
3. ELSE
    1. IF $x_{m} < x_{0}$ then searches the sub-array $x_{m+1}, \cdots, x_{n-1}$
    2. ELSE then searches the sub-array $x_{0},\cdots,x_{m-1}$
4. Repeat untill found or all search space is exausted.

### Problem 5.1.

Provide a sequential implementation of this algorithm.

### Problem 5.2.

Provide a recursive implementation of this algorithm.

__Hint.__ In the recursive version of the algorithm, the function should receive the left and right extremities of the search space

### Problem 5.3

What is the [algorithmic complexity](https://en.wikipedia.org/wiki/Computational_complexity_theory) for finding an element with binary search?

# Classes

## Problem 6

In this problem, we are going to cover binary search tree. Follow the next steps,

### Problem 6.1

Code a class ```Node``` with the following specification,

#### Attributes

Objects of the class ```Node``` have the following attributes,

- ````left````
- ````right````
- ````value````

The attribute ```value``` stores the node's value. It is a float.

The attributes ```left``` and ```right``` store children nodes. In a binary search tree, the children nodes have a special structure. Assume a node $p$. The tree is structured such that

$$\text{p.left.value} \leq \text{p.value} \leq \text{p.right.value}.$$

#### Methods

Objects of the class ```Node``` have the following methods,

- ```insert_children(other_node)```

In ```insert_children(other_node)```, you insert a new object of the class ```other_node``` in ```left``` or ```right```.


### Problem 6.2

Write a class ```Tree``` with the following specification. Henceforth we refer to a generic object from ```Tree``` as ```tree```

#### Attributes

- ```root```

The attribute ```root``` stores the root of the binary search tree. It should be initialized as ```None```.

#### Methods

- ```insert_node(node)```

here, ```node``` is an instance of the class ```Node```. The logic of ```insert_node``` is as follows,

1. __If__ ```tree.root is None```, then the root was not set, set ```node``` as the root and terminate execution.
2. __Else__
    1. Run over the tree untill hitting a dead end (either ```node.left``` or ```node.right``` being None).
    2. Add to the left or right based on ```node.value```.

__Hint.__ A while loop would be appropriate.

- ```__str__()```

here, you should print the tree as follows,

Start by printing the root node, alongside with its two children. For instance:

```
8 (left: 3, right: 10)
```

Then, you proceed to print all nodes,

```
8 (root, left: 3, right: 10)
3 (left: 1, right: 7)
1 (left: None, right: None)
7 (left: None, right: None)
10 (left: 9, right: 14)
9 (left: None, right: None)
14 (left: None, right: None)
```

__Hint.__ Think recursively.

- ```search(x)```

Searches for the node such that ```node.value = x```

### Problem 6.3

- What is the computational complexity of inserting an element to a binary search tree?
- What is the computational complexity of searching for an element in a binary search tree?