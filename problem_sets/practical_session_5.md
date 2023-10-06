## Problem 1: Entropy

Let $n$ and $n_{c}$ be, respectively, the number of samples and the number of classes in a machine learning problem. In this exercise we are going to calculate the entropy of randomly generated predictions.

### Step 1: Randomly generating predictions

Randomly generate a matrix of shape $(n, n_{c})$, for $n = 1000$ and $n_{c} = 10$

__Note.__ Look up online, or in the lecture, which NumPy function generates random matrices.

### Step 2: Softmax operation

Given a vector $\mathbf{x} \in \mathbb{R}^{n_{c}}$, it can be __transformed__ into a vector of __probabilities__ through the [__softmax__ function](https://en.wikipedia.org/wiki/Softmax_function),

$$\text{softmax}(\mathbf{x})_{i} = \frac{e^{x_{i}}}{\sum_{j=1}^{n_{c}}e^{x_{j}}}$$

__Code.__ Implement a function that, given $\mathbf{x}$, outputs $\text{softmax}(\mathbf{x})$.

### Step 3: Entropy

For a vector $\mathbf{p} \in \mathbb{R}_{+}^{n_{c}}$ s.t. $\sum_{i=1}^{n_{c}}p_{i}=1$, the entropy of $\mathbf{p}$ is,

$$H(\mathbf{p}) = -\sum_{i=1}^{n_{c}}p_{i}\log p_{i}$$

Using the probabilities acquired in the last problem,

#### Naïve Approach

Compute $H(\mathbf{p}_{i})$ for $i=1,\cdots,n$ using a __for loop__.

#### Optimized Approach

Compute $H(\mathbf{p}_{i})$ for $i=1,\cdots,n$ without a __for loop__.

## Problem 2: Pairwise distances

Let's say you have 2 sets of points in a $d-$dimensional Euclidean space. These are represented in the canonical basis, through 2 matrices, $\mathbf{X}$ and $\mathbf{Y}$, of shape $(n, d)$ and $(m, d)$. You want to compute the following,

### Problem 2.1: Euclidean Distance

#### Naïve Approach

Compute the matrix of pairwise Euclidean distances between them,

$$D_{ij} = \lVert \mathbf{x}_{i} - \mathbf{y}_{j} \rVert_{2}$$

Do so with a standard for loop (i.e. loop through all $i$ and $j$.)

__Note.__ You should store these in the entries of a matrix of shape $(n,m)$.

#### Optimized Approach

Based on,

$$D_{ij}^{2} = \lVert \mathbf{x}_{i} \rVert_{2}^{2} + \lVert \mathbf{y}_{j} \rVert_{2}^{2} - 2 \langle \mathbf{x}_{i},\mathbf{y}_{j} \rangle$$

Calculate $\mathbf{D} \in \mathbb{R}^{n \times m}$ through __broadcasting__.

### Problem 2.2: Cossine Similarity

Given the same matrices $\mathbf{X} \in \mathbb{R}^{n\times d}$ and $\mathbf{Y} \in \mathbb{R}^{m\times d}$, compute the similarity matrix $\mathbf{S} \in \mathbb{R}^{n \times m}$ defined as,

$$S_{ij} = \text{cossim}(\mathbf{x}_{i},\mathbf{y}_{j}) = \frac{\langle \mathbf{x}_{i}, \mathbf{y}_{j} \rangle}{\lVert \mathbf{x}_{i} \rVert_{2}\cdot \lVert \mathbf{y}_{j} \rVert_{2}}$$

#### Naïve Approach

Compute $\mathbf{S}$ with a double for loop.

#### Optimized Approach

Compute $\mathbf{S}$ using __broadcasting__.

## Problem 3: PDEs over Images

### The Heat Equation

In mathematics and physics, the [heat equation](https://en.wikipedia.org/wiki/Heat_equation) is defined in terms of a function $u(t, \mathbf{x})$ of a temporal variable $t$, and a spatial variable $\mathbf{x} \in \mathbb{R}^{d}$. In this problem, we are going to explore the heat equation in the context of $d = 2$, hence, let us express $u(t, x, y)$. In its continuous form, the equation is expressed in terms of partial derivatives,

$$\frac{\partial u}{\partial t} = \alpha\biggr(\frac{\partial^{2} u}{\partial x^{2}} + \frac{\partial^{2} u}{\partial y^{2}}\biggr)$$

### Step 1: Discretizing the Heat Equation

Here, we are going to work on a grid of shape $(n, n)$. This means that we discretize the $x-y$ plane into $n$ values. Likewise, we discretize the time variable.

Under discretization, the finite-differences of (partial) derivatives is given by,

$$\frac{\partial u}{\partial t} \approx \frac{u(t+\delta t,x,y) - u(t, x, y)}{\delta t}$$

Show that, for $\delta t> 0$, $\delta x = \delta y > 0$, the heat equation boils down to the following expression,

$$u_{i,j}^{(k+1)} = u_{i,j}^{(k)} + \gamma(u_{i+1,j}^{(k)} + u_{i-1,j}^{(k)} + u_{i,j+1}^{(k)} + u_{i,j-1}^{(k)} - 4u_{i,j}^{(k)}),$$

where $\gamma = \alpha\frac{\delta t}{\delta x^{2}}$

__Image Interpretation.__ $\mathbf{u}$ is going to be a 3D array, of shape $(n_{iter}, h, w)$, where $h$ denotes the height of the image ($\#$ of rows), and $w$ denotes the width of the image ($\#$ of columns). The diffusion process sets $u^{(0)}_{ij}$ as the initial conditions, then iterates the heat equation for $n_{iter} - 1$ steps filling the array. Note that under this interpretation, the spatial variables are the pixel positions $(i, j)$, whereas the time variable is the diffusion step $k$.

__Note.__ From Von Neumann's analysis, these iterations are stable for $\gamma \leq 0.5$. Since here we are interested on how the Heat Equation affects images, and not really about the physics of the problem, we are going to ignore $\delta t$ and $\delta x$, and set $\gamma := 0.25$.

### Step 2: Initial Conditions

Each image consists of a matrix $(n, n)$, where $n = 256$.

As initial conditions for the problem, we assume the following case:

- let $\mathbf{c}_{0} = (170, 170)$. $u_{ij}^{(0)} = 1$ for all $\mathbf{x} = (i,j)$ s.t. $\lVert \mathbf{x}_{0} - \mathbf{x} \rVert_{2} \leq 20$
- let $\mathbf{c}_{1} = (85, 85)$. $u_{ij}^{(0)} = 1$ for all $\mathbf{x} = (i,j)$ s.t. $\lVert \mathbf{c}_{1} - \mathbf{x} \rVert_{2} \leq 30$

This should generate two circles on the image. For plotting, use the following script,

```python
import matplotlib.pyplot as plt

plt.figure()
plt.imshow(u0, cmap=plt.cm.Reds, vmin=0., vmax=1.)
plt.show()
```

where ```u0``` is a $(n, n)$ matrix initialized as described.

### Step 3: Naïve Implementation

Implement the PDE using 3 nested for loops (one for the time, and 2 for the spatial variables).

### Step 4: Optimized Implementation

Vectorize your implementation on the two spatial variables.

### Visualization

Assuming $\mathbf{u}$ is a 3D array with shape $(100, 256, 256)$, you can create a cool gif using,

```python
from matplotlib.animation import FuncAnimation

# Plots initial conditions
fig, ax = plt.subplots(1, 1, figsize=(5, 5))

ax.imshow(u[0, ...], cmap=plt.cm.Reds, vmin=0., vmax=1.)
ax.set_title(f'Iteration = {0}')

# Function for animation
anim_it = 0


def update(frame):
    global it
    # clear the axis each frame
    ax.clear()
    ax.imshow(frame, cmap=plt.cm.Reds, vmin=0., vmax=1.)
    ax.set_title(f'Iteration = {it}')

    anim_it += 1

anim = FuncAnimation(fig, update, frames=u)
anim.save('circles.gif', writer='imagemagick', fps=5)
```

### Optional

Test your code with the following initial conditions,

$$
u^{(0)}_{ij} = \begin{cases}
1 & \text{if }(100 \leq i \leq 156) \text{ and } (100 \leq j \leq 156)\\
0 & \text{otherwise}
\end{cases}
$$

and,

$$
u^{(0)}_{ij} = \begin{cases}
1 & \text{if }(i = j + k)\text{ , }k=-5,\cdots,5\\
0 & \text{otherwise}
\end{cases}
$$