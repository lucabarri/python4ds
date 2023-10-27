# Document Classification

## TF-IDF

So far, you did a k-NN with a Term-Frequency term. You can enrich this feature space with the Inverse of Document Frequencies, i.e., IDF. Henceforth, you will consider the following,

$$\text{tfidf}(w\_{j},d\_{i},\mathcal{D}) = \text{tf}(w\_{j},d\_{i})\cdot \text{idf}(w\_{j},\mathcal{D})$$

the IDF term weights the features by how often the word $w\_{j}$ occurs in the corpus $\mathcal{D}$. In the following we will consider,

$$x_{ij} = p_{ij} \cdot \log \frac{N}{N_{j}}$$

where $p_{ij} = f_{ij} / \sum_{j=1}^{n}f_{ij}$, $N_{j} = |w\_{j} \in D:D \in \mathcal{D}|$, i.e., the number of documents in which word $w\_{j}$ appears.

Compare the BoW model with the TF-IDF representation in the case of the Euclidean distance and the Cosine Dissimilarity (see practical session 5).