from skimage import feature, imread
from sklearn import svm
from sklearn.metrics import accuracy_score
import numpy as np

# extract hog features
def extract_hog_features(img):
    hog_features = feature.hog(img, orientations=9, pixels_per_cell=(16, 16),
                               cells_per_block=(2, 2), block_norm='L2-Hys',
                               transform_sqrt=True, feature_vector=True)
    return hog_features

# prepare data
X_train = []
y_train = []

for i in range(10):
    img = imread(f'path/to/train_img_{i}.jpg')
    hog_features = extract_hog_features(img)
    X_train.append(hog_features)
    y_train.append(i)

X_train = np.array(X_train)
y_train = np.array(y_train)

# fit the model
clf = svm.SVC(kernel='linear', C=1.0)
clf.fit(X_train, y_train)

# predict on test data
X_test = []
y_test = []

for i in range(10):
    img = imread(f'path/to/test_img_{i}.jpg')
    hog_features = extract_hog_features(img)
    X_test.append(hog_features)
    y_test.append(i)

X_test = np.array(X_test)
y_test = np.array(y_test)

y_pred = clf.predict(X_test)

# evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

# simple if-else condition for classification
for i, label in enumerate(y_pred):
    if label == 0:
        print(f'Image {i} is classified as class 0')
    elif label == 1:
        print(f'Image {i} is classified as class 1')
    # and so on for other classes
