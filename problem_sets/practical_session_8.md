# Introduction

For this problem set, you will use the file "gtzan_53fts.csv", located in the "./data" folder.

__Hint.__ If you have difficulties with the next steps, check the past lectures or take a look on [Pandas documentation](https://pandas.pydata.org/)

## Reading the data

Use ```pandas.read_csv``` for reading the data, then, display the dataframe on Jupyter. What is the meaning of columns?

## Separating features from labels

Extract the columns corresponding to features, and those corresponding to labels. Convert the sub-dataframes to numpy arrays.

# Exploratory Data Analysis

## One-dimensional Analysis

In this part, you will analyze each feature independently from the others. Plot the histogram for the 53 features grouped as follows,

- 42 histograms for the MFCC features (mean + variance)
- 2 histograms for the chromagram features (mean + variance)
- 3 histograms for the tempo and beat features (mean + variance)
- 6 histograms for the rolloff, zcr and spectral centroid features (mean + variance)

__Hint.__ This should generate a large number of plots (i.e., 53). You may find easier to save these to a folder "./experiments/audio/1d" then group similar histograms into similar folders (e.g. "./experiments/audio/1d/mfcc_feats").

__Question.__ At this stage, what can be said about the __range__ of different features? How are they distributed?

## One-dimensional class-based analysis

Repeat the process of the last part, but take labels into account. More specifically, you will plot __on the same figure__, for each feature, 10 histograms, corresponding to the filtered sampled of a given class. You should use a color for each class-histogram, and add a legend.

__Hint.__ To facilitate your analysis, save your histograms to "./experiments/audio/1d_class/"

__Question.__ Are there any particular features that allow you to make a difference between classes? Are there any classes that stand out from the rest?

## Note

From now on, scale the data to the same range (i.e., [0, 1]) using,

$$x\_{ij} = \frac{x\_{ij} - min\_{i}x_{ij}}{(max\_{i}x\_{ij}) - (min\_{i}x\_{ij})}$$

## Two-Dimensional Analysis

In this part, you will analyze __linear relationships__ between pairs of features. To that end, you will use __Pearson's Correlation Coefficient__, i.e.,

$$\rho\_{i,j} = \frac{\Sigma\_{ij}}{\sigma\_{i} \sigma\_{j}}$$

where $\Sigma\_{ij} = \mathbb{E}[(X\_{i}-\mu\_{i})(X\_{j}-\mu\_{j})]$ is the covariance between $X\_{i}$ and $X\_{j}$, $\mu_{i}=\mathbb{E}[X_{i}]$, and $\sigma\_{i} = \mathbb{E}[(X\_{i}-\mu\_{i})^{2}]$. Based on this definition, calculate the __correlation matrix__,

$$R\_{ij} = \rho\_{ij} \in [-1, +1]$$

for $i=1,\cdots,53$ and $j=1,\cdots,53$. Visualize it using ```plt.imshow```. Note that two features are __strongly correlated__ if $|R\_{ij}| \approx 1$. If $|R\_{ij}| \approx 0$, the features are called __uncorrelated__. 

__Hint.__ use ```ax.set_xticks``` (resp. yticks) for renaming the x-axis ticks for the variable names.

__Question.__ Are there strongly correlated features? Do you see any pattern in the correlation matrix?

## Multi-Dimensional Analysis

Compute the __Principal Component Analysis (PCA)__ of the dataset:

1. Standardize the data, i.e.,

$$x\_{ij} = \frac{x\_{ij} - \mu\_{j}}{\sigma\_{j}}$$

2. Compute the correlation matrix $R\_{ij}$

3. Compute the Eigendecomposition of $R$,

$$\mathbf{R} = \mathbf{VDV}$$

where $\mathbf{VV}^{T} = \mathbf{I}$ and $\mathbf{D}$ is a diagonal matrix.

__Hint.__ Use [```np.linalg.eig```](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html).

4. Sort the values of $\mathbf{D}$ in __decreasing__ order, i.e., $D = [\lambda\_{1}, \cdots, \lambda\_{d}]$ in which $\lambda\_{1} \geq \lambda\_{2} \geq \cdots \geq \lambda\_{d}$. Apply the same ordering to the columns of $\mathbf{V}$.

5. Select the $k=2$ columns of $\mathbf{V}$ into $\tilde{\mathbf{V}} \in \mathbb{R}^{d \times k}$. Transform the data as $\tilde{\mathbf{X}} = \mathbf{XV} \in \mathbb{R}^{n \times k}$.

Upon computing $\tilde{\mathbf{X}}$, visualize the data over the plane through a scatterplot, separating between classes using colors and a legend. Are there any classes that are distinguishable from the others?

# Inference

Based on the previous problem set,

1. Partition the data into train-test with 80\%-20\% of the data in each split.
2. Use a nearest neighbors classifier for predicting on the test set.

__Q1.__ How many instances do the classifier gets correctly?
__Q2.__ Measure the __classification accuracy__ per class. Which classes the classifier predicts better?