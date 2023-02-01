from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Initialize the model
model = Sequential()

# Add a 2D Convolutional layer with 32 filters and a kernel size of 3x3
model.add(Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)))

# Add a Max Pooling layer with a pool size of 2x2
model.add(MaxPooling2D((2,2)))

# Flatten the feature maps to prepare for fully connected layer
model.add(Flatten())

# Add a fully connected layer with 128 units and ReLU activation
model.add(Dense(128, activation='relu'))

# Add a final output layer with 10 units and softmax activation for classification
model.add(Dense(10, activation='softmax'))

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(-1, 28, 28, 1) / 255.
x_test = x_test.reshape(-1, 28, 28, 1) / 255.

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)

# predictions = model.predict(x_test)


