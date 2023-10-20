# Image Restoration

## Introduction

Let $\mathbf{f} \in \mathbb{R}^{h \times w}$ denote a gray-scale image. A noisy version of $\mathbf{f}$ is another image $\tilde{\mathbf{f}} \in \mathbb{R}^{h \times w}$ for which a noising process $H$ has acted, i.e.,

$$\tilde{\mathbf{f}} = H(\mathbf{f})$$

__Note 1.__ For this lecture, you will test your algorithms on images from the __set 68__, available at the data folder. See the lecture for how to read these images.

## 1. Noising Processes

In the first part of this problem set, you will program two noise generating functions,

1. ```additive_white_gaussian_noise(im, std)```
2. ```s_and_p_noise(im, p)```

here, all functions take as input ```im```, which represent the input image $\mathbf{f}$. The function should output $\tilde{\mathbf{f}}$.

### 1.2 Gaussian Noise

Additive White Gaussian Noise (AWGN) is the simplest kind of noise. It consists on sampling $\epsilon_{ij} \sim \mathcal{N}(0, \sigma)$, then,

$$\tilde{f}\_{ij} = f\_{ij} + \epsilon\_{ij}$$

### 1.3 Salt and Pepper Noise

Salt and Pepper noise represents sudden changes in the signal, such as defective pixels. The idea is the following: given a probability $p$, and for each pixel $(i, j)$,

$$
\tilde{f}\_{ij} = \begin{cases}
f\_{ij}&\text{ with prob. } 1-p\\
1 & \text{ with prob. } p/2\\
0 & \text{ with prob. } p/2
\end{cases}
$$

## 2. Measuring Image Restoration Quality

When comparing algorithms of image restoration, it is crucial to have metrics to compare the "goodness" of restoration. To that end we are going to explore 2 metrics,

- ```mean_squared_error(f_true, f)```
- ```peak_signal_to_noise_ratio(f_true, f)```

__Note 2.__ While ```f_true``` represents the original, non-noisy image, ```f``` can be either the restored, or noisy image. ```f_true``` is often called reference or ground truth.

__Note 3.__ Both of these metrics correlate quite poorly with human percepction. For a more intricate metric see the [Structural Similarity Index Measure (SSIM)](https://en.wikipedia.org/wiki/Structural_similarity)

### 2.1. Mean Squared Error

For images of shape $(h,w)$, the Mean Squared Error (MSE) is defined as,

$$\text{MSE}(\mathbf{f},\tilde{\mathbf{f}})=\frac{1}{hw}\sum_{i=0}^{h-1}\sum_{j=0}^{w-1}(f_{ij}-\tilde{f}_{ij})^{2}$$

### 2.2. Peak Signal to Noise Ratio

The PSNR is based on the MSE, but on a logarithmic scale,

$$\text{PSNR}(\mathbf{f},\tilde{\mathbf{f}})=10\log_{10}\biggr(\frac{1}{MSE(\mathbf{f},\tilde{\mathbf{f}})}\biggr)$$

### 2.3. Measuring Quality Degradation

Plot the MSE and PSNR of $\mathbf{f}, \tilde{\mathbf{f}}$ as a function of $\sigma$ (AWGN) and $p$ (S & P). Is there a relationship between these variables and the quality metrics?

__Challenge.__ Prove that $PSNR(\mathbf{f}, \tilde{\mathbf{f}}) = -20\log_{10}(\sigma)$, for AWGN

## 3. Linear Filtering

Linear filters are based on the convolution operation. As we saw in today's lecture, the Heat kernel, through the Laplacian filter, is a filter that acts on the image's spatial domain (i.e., image pixels). This translates to the frequency domain through the Fourier transform. The two things are linked through the [__convolution theorem__](https://en.wikipedia.org/wiki/Convolution_theorem), which roughly states that,

$$\mathcal{F}(f \star g) = FG$$

where $F = \mathcal{F}(f)$ (resp. $G$) is the Fourier transform of the image $f$ (resp. $g$).

### 3.1. Convolution

Let $f$ and $g$ be two images, and $F$ and $G$ their respective Fourier transforms. Implement a function ```frequency_convolve(F, G)``` which returns $\mathcal{F}^{-1}(FG)$.

### 3.2. Gaussian Filtering

Implement a Gaussian filter, which is defined as,

$$g(x, y) = \frac{1}{Z}\text{exp}\biggr(\frac{x^{2}+y^{2}}{2\sigma^{2}}\biggr)$$,

for $Z = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}g(x, y)dxdy$.

__Note 4.__ $g$ is defined in spatial coordinates. Compute $G$, the FFT of $g$.

__Hint 1.__ Let $h, w$ be given. You will compute the __unormalized__ kernel $\tilde{g}(i,j)=ZG(i,j)$, $i=0,\cdots,h-1$ and $w=0,\cdots,1$. Aftewards, you compute $Z$ by summing over the rows and columns of $\tilde{g}(i,j)$.

__Hint 2.__ You will implement $g(x, y)$ over an uniform and __symmetric__ grid. This means that, instead of using ```np.meshgrid(x, y)``` over ```x = np.arange(h)```, you will define $x$ over $\{-h/2,\cdots,h/2\}$. Make sure $h / 2$ is rounded and casted to an integer. The definition of $y$ is analogous to $x$ (with $w$ in place of $h$).

### 3.3. Choosing $\sigma$

As you may have noticed, $\sigma$ plays an important role in the definition of $G(x, y)$. Pick an image from set 68, and plot the MSE and PSNR as a function of $\sigma$. Set $\hat{\sigma}$ to the value achieving the highest PSNR..

## 4. Exploring Linear Filtering Visually

### 4.1. Correlation between MSE and PSNR

As we defined previously, the MSE and PSNR are related. For each image in the set68 evaluate the MSE and PSNR for Gaussian and Salt & Pepper noises. Plot __two__ scatterplots, where on the x-axis you will put the MSE and on the y-axis you will put the y-axis. Describe your results.

__Note.__ go beyond linear relationships.

### 4.2. Choosing $\sigma$ based on a dataset

For each image on Set 68, compute the PSNR between the ground-truth and the restored image for various values of $\sigma$. Compute: (1) the average PSNR, (2) the standard deviation over values of $\sigma$ for the whole dataset. Describe your acquired results. Is there a single $\sigma$ that works for all images?

__Challenge.__ If you're willing to push your analysis further, consider splitting the dataset into two sub-sets. The first, used to __fit__ $\sigma$, is composed of $80\%$ of the data. The second, composed of $20\%$ of the data, is used to evaluate the "goodness of fit" for $\hat{\sigma}$. Are you still able to find appropriate values for the test set?
