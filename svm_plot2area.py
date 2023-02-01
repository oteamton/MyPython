import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm

# Load a two-class dataset, such as the breast cancer dataset
breast_cancer = datasets.load_breast_cancer()
X = breast_cancer["data"][:, :2]  # only use the first two features for visualization
y = breast_cancer["target"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the SVM model using a linear kernel
clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

subsample_size = 50  # number of samples to subsample
subsample_indices = np.random.choice(X.shape[0], subsample_size, replace=False)
X_subsample = X[subsample_indices]
y_subsample = y[subsample_indices]

x_min, x_max = X_subsample[:, 0].min() - 1, X_subsample[:, 0].max() + 1
y_min, y_max = X_subsample[:, 1].min() - 1, X_subsample[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100,
            linewidth=1, facecolors='none', edgecolors='k')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("SVM Decision Boundary and Support Vectors")
plt.show()



# Blue dots represent data points of one class.

# Red dots represent data points of another class.

# The black circles around some of the blue dots indicate that these points are the "support vectors". The support vectors are the data points that are closest to the decision boundary and have the most impact on defining the boundary.

# So, a blue dot with a black circle in a red area means that this blue point is a support vector but it has been misclassified into the red class. On the other hand, a blue dot in a red area without a black circle indicates that the point has been misclassified but it is not a support vector.