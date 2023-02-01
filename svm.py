from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm

# Load the iris dataset
iris = datasets.load_iris()
X = iris["data"]
y = iris["target"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the SVM model using a linear kernel
clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

# Evaluate the model on the test set
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)
