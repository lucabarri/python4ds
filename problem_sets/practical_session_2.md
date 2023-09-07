# Problem 1

Given two integers $(n, m)$, write a program that computes the following sum,

$$S = \sum_{i=1}^{n}\sum_{j=1}^{m}\frac{i^{2} * j}{3^{i}(j*3^{i} + i * 3^{j})}$$

# Problem 2

Create a program that stores [Pascal's Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle) in a nested list.

Example

```
Input: n = 4
Output:
[
    [1,],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1]
]
```

# Problem 3

Write a program that, given $n$, it tests the [Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture). The Collatz conjecture states that, given an arbitrary integer $n$, iterating the following operations,

1. If $n_{it}$ is even, $n_{it+1} \leftarrow n_{it} / 2 $ 
2. If $n_{it}$ is odd, $n_{it+1} \leftarrow 3n_{it} + 1$

The sequence $\{n_{it}\}_{it=1}^{\infty}$ will eventually converge to $1$.

The program you write should iterate $n$ following the rules previously stated. Save each iterate to a list. You should print the sequence of iterates, as well as the number of iterations required to reach 1.

Example,

```
Input: n = 12

List of iterates: [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
Number of steps: 9
```

# Problem 3

In a talk show, the host wants to give a gift to one person from the audience. The program's director comes up with the following strategy:

1. Organize every single person, among the $n$ persons in the audience, in a circle,
2. Count $k$ persons,
3. Eliminate person $k + 1$
4. Repeat from step 2.

Given $n$ and $k$, write a program that prints the gifted person from the audience.

# Problem 4

Write a program that,

1. Reads the contents of ```shakespeare.txt```
2. Extracts every single word from the contents of the file,
3. From the set of words, extracts the unique words,
4. Counts the frequency of each unique word,
5. prints the 30 most frequent words.

__Warning.__ Be mindful of punctuation, line breaks, lower and captal letters, and trailing whitespaces
