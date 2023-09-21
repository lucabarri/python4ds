# Problem 1

Implement a class called vector,

with the following attributes,

- ```data```: contains a list with the coordinates of the vector (canonical basis).

implementing the following magic functions,

- ```__str__(self)```: prints the list of vector's coordinates,
- ```__len__(self)```: returns the number of coordinates in the vector.
- ```__getitem__(self, idx)```: returns the coordinate at position ```idx```
- ```__abs__```: returns the 2-norm of the vector,
- ```__add__(self, other)```: If other is a Vector, adds two vectors in a coordinate-wise fashion. If it is a scalar, adds the scalar to each coordinate. Otherwise, raises a ValueError.
- ```__sub__(self, other)```: If other is a Vector, subtracts two vectors in a coordinate-wise fashion. If it is a scalar, subtracts the scalar to each coordinate. Otherwise, raises a ValueError.
- ```__mul__(self, other)```: If other is a Vector, performs an inner product. If other is a scalar, multiply each coordinate by it. Otherwise, raise a ValueError.

__Hint.__ use __math__ for calculating square-roots.

Test the behavior of you class as you wish.

# Problem 2

This problem will deal with Natural Language Processing (NLP). Briefly, a document is characterized by a set of words. A major challenge in NLP is finding a number representation for a document (e.g., a vector). A solution coming from statistics is to count the frequencies of words in documents. In this sense, a document is characterized by a __vocabulary of unique words__, called $V$. $V$ is defined as $V = \set{w_{1},\cdots,w_{n}}$ of $n$ unique words. As such, a document is represented as a vector $x \in \mathbb{R}^{|V|}$, where $|V| = n$ is the cardinality of the vocabulary.

In this problem, we start to build some intuition on the statistical analysis of documents. You will build a class, called ```Document```, that models the representation of a single document. Your class should have the following attributes,

- ```raw_data```: contains the raw data (text).
- ```preprocessing_fn```: is a function that receives raw text and __normalize it__.
- ```data```: contains the preprocessed data (text).
- ```vocabulary```: is the set of unique words.
- ```frequencies```: is a dictionary containing the assignment $w \mapsto f$, where $w$ is the word, and $f$ is how many times it appears on ```data```.

## Problem 2.1: the ```__init__``` method

The ```Document``` class will receive a ```path``` to the document you want to read, and a ```preprocessing_fn```, which is a function that receives text and normalizes it.

In the ```__init__``` method, you should open the file located at ```path```. Look at the 1st lecture for more information about reading files. You should store the file contents in ```self.raw_data```.

Next, you will apply the preprocessing function on the raw data, i.e.,

```python
self.preprocessed_data = preprocessing_fn(self.raw_data)
```

Once you get your preprocessed data, you should build the vocabulary. You should extract the set of unique words from ```self.preprocessed_data```, and save it into ```self.vocabulary```.

we're going to cover the preprocessing steps in the next section.

With your vocabulary at hand, you will then create the ```frequencies``` dictionary. For each word in your vocabulary, count how many times it appers in the preprocessed text. __Use list comprehension__.

## Problem 2.2: text preprocessing

Assemble the text preprocessing steps in [this tutorial](https://www.geeksforgeeks.org/normalizing-textual-data-with-python/). Your function should receive ```text``` as input, and __return__ ```preprocessed_text``` with the modifications made.

__Note.__ do not worry about removing stop words. We are going to cover that in future lectures.

## Problem 2.3: implemeting ```__getitem__```

You will implement a method, called ```__getitem__(self, idx)```. The behavior of this method is as follows,

- If ```idx``` is a string, you should check if $idx \in V$.
    - If True, you return a tuple ```(idx, frequencies[idx])```
    - If False, you should __raise__ an IndexError
- If ```idx``` is an integer, you should __return__ the "idx-th" item from the dictionary of frequencies (i.e. ```frequencies.items()```).
- Otherwise, you should raise an IndexError.

## Conceptual Questions

- How the preprocessing steps affect the vector representation of a document?
- Suppose you have two instances of the class ```Document```. How can you compare these documents?
    - Could you, for instance, directly calculate the (Euclidean) distance between vectors $x_{1}$ and $x_{2}$?
    - How does the number of unique words affect the distance? For long documents, do you thinkg $dist(x_{1}, x_{2})$ [would make any geometrical sense](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=1ea82cc13f6b7352943aba6c987e3895e5161b9b)?

# Problem 3

__Context.__ In Deep Learning, it is impractical to hold complete datasets in memory at once. For instance, the [ImageNet-1k](https://en.wikipedia.org/wiki/ImageNet) datasets contains over 1,281,167 images from 1000 classes. Assuming each image being a $(3,224,224)$ tensor of pixels, and each pixel being encoded by a 8-bit integer, one has $150.53$ _KB_ per image. Overall, the total size of the dataset is $192.85$ _GB_, which is over 24 times the RAM memory of consumer-level laptops.

As a consequence, in Deep Learning practice one actually loads data into memory on-the-fly, that is, when training a neural net, you keep in memory only a couple of mini-batches needed for forward and backward passes.

__The problem.__ You will write a class, called ```ImageDataset``` that will manage the access to individual images from a list of paths. You will work with datasets with the following directory structure,

```
root
|- class_1
| |- img_1
| |- img_2
| ...
| |- img_n
|- class_2
...
|- class_k
```

## Problem 3.1

1. Install [gdown](https://github.com/wkentaro/gdown) on Google Colab using,

```sh
!pip install gdown
```

2. Import gdown on Google Colab,

```python
import gdown
```

3. Use the following snippet to download the [Office-31 Dataset](https://faculty.cc.gatech.edu/~judy/domainadapt/)

```python
url = "https://drive.google.com/uc?id=0B4IapRTv9pJ1WGZVd1VDMmhwdlE"
output = "office31_images.tar.zip"
gdown.download(url, output, quiet=False)
```

4. Unzip the dataset contents,

```sh
!mkdir "./office31"
!tar -xf "./office31_images.tar.zip" -C "./office31"
```

## Problem 3.2

__Class Specification.__ Your class needs to have the following attributes,

- ```root```: contains a string with the path to the root directory of the dataset. __It needs to be specified in the class constructor__.
- ```class_names```: a list containing the name of each class in the dataset
- ```class_name_to_int```: contains a dictionary, where keys are class names (e.g. backpack or bike), and the output is an integer specifying to which class the image belongs to (e.g. assign 0 to backpack and 1 to bike).
- ```filepaths```: contains the path of each image in the dataset. Should be set by running through the folds (starting from root).

and implement the following methods,

- ```__len__(self)```: returns the number of elements in the dataset.
- ```__getitem__(self, idx)```: Returns a tuple ```(x, y)```, where ```x``` is an image, and ```y``` is a label corresponding to ```self.filepaths[idx]```.

__Hint 1.__ You can use the following snippet for reading an image

```python
import numpy as np
from PIL import Image

im = np.array(Image.open(filepath))
```

__Important.__ here, filepath indicates the complete path to the file.

__Hint 2.__ For managing paths, and listing the files in a directory, use the [os library](https://docs.python.org/3/library/os.html). You can find a reference of the library [in here](https://www.geeksforgeeks.org/os-module-python-examples/).

__Hint 3.__ For debugging, it may be useful to use Matplotlib for visualizing the outputs of ```__getitem__```. If ```x``` is a numpy array of shape ```(h,w,c)```, you can use the following snippet to visualize your image,

```python
x, y = dataset[0]

plt.figure()
plt.imshow(x)
plt.title(f'Class: {y}')
plt.axis('off')
```