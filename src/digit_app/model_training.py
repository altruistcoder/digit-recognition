import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


# Import the MNIST Dataset:

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


# Printing the shapes of both Training & Testing Datasets as well as their Labels:

print("Shape of Training Dataset:", x_train.shape)
print("Shape of Training Dataset Labels:", y_train.shape)
print("Shape of Test Dataset:", x_test.shape)
print("Shape of Test Dataset Labels:", y_test.shape)


# Print the labels of the first 5 digits present in the Taining dataset:

nb_images = 5
print(y_train[:nb_images])


# Also, Let's see the images of first 5 digits present in the Taining dataset:

train_images = np.hstack(x_train[:nb_images])
plt.imshow(train_images, cmap='Greys')


# Now, we will create a Neural Network model and define the layers of our model:

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10),
  tf.keras.layers.Softmax()
])


# Print the summary of the model:

print(model.summary())


# Defining of Loss Function for our model:

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)


# Compile our model:

model.compile(optimizer='adam', loss=loss_fn, metrics=['accuracy'])


# Training of our model:

hist = model.fit(x_train, y_train, epochs=10, shuffle=True, batch_size=256, validation_split=0.20)


# Plotting of the graphs of Loss & Accuracy of both the Training as well as Validation:

plt.figure(0)
plt.plot(hist.history['loss'], 'g')
plt.plot(hist.history['val_loss'], 'b')
plt.plot(hist.history['accuracy'], 'r')
plt.plot(hist.history['val_accuracy'], 'black')
plt.show()


# Checking the model's performance on the Test Dataset:

model.evaluate(x_test,  y_test, verbose=2)


# Saving the model:

model.save('my_mnist_model')
