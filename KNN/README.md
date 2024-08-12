# KNN 

k-Nearest Neighbors (k-NN) is a non-parametric, lazy learning algorithm used for both classification and regression. It works by finding the k-nearest data points to a query point in the feature space and making predictions based on the majority class or average of these neighbors.


![image](https://github.com/user-attachments/assets/c50da9fa-1320-40de-8c3e-55fbda57a8f1)


In k-Nearest Neighbors (k-NN) classification or regression, Euclidean distance is a common method for measuring the distance between data points. It’s used to find the k closest neighbors to a given data point.


![image](https://github.com/user-attachments/assets/17da367d-2f6e-4561-8757-72f606b6853d)


### Nearest Neighbors (k-NN) classification, while useful in many contexts, has several drawbacks:

Computational Complexity:

- Training Phase: k-NN has no explicit training phase, but during prediction, it requires computing the distance between the query point and all points in the dataset. This can be computationally expensive, especially with large datasets.

- Prediction Phase: The time complexity for a single prediction is O(n⋅d), where 𝑛 is the number of samples and d is the number of dimensions (features). This can become slow as the dataset grows.

Memory Intensive:

- k-NN requires storing the entire dataset in memory, which can be a limitation for very large datasets.

Curse of Dimensionality:

- In high-dimensional spaces, the distance between points becomes less distinguishable, and k-NN may suffer from the "curse of dimensionality." This means that as the number of features increases, the concept of "nearness" becomes less meaningful, which can negatively impact the model’s performance.

Choice of k:

- The performance of k-NN depends on the choice of 𝑘. A small k can make the model sensitive to noise, while a large 𝑘 can smooth out the decision boundary too much, potentially leading to underfitting. Selecting an optimal k often requires cross-validation.
