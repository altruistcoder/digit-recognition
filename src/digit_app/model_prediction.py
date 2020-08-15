import os
import cv2 as cv
import numpy as np
import tensorflow as tf
from digit_recognizer.settings import BASE_DIR


def digit_prediction(img):
    # Importing the trained model file
    model = tf.keras.models.load_model(os.path.join(BASE_DIR, "digit_app\my_mnist_model"))

    # Performing some transformations on the input image numpy array to provide better prediction
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    img_inverted = cv.bitwise_not(img_gray)
    img_resized = cv.resize(img_inverted, (28, 28))
    img_reshaped = img_resized.reshape((1, 28, 28))

    # Predicting the number present in the input image
    prediction = np.argmax(model.predict(img_reshaped))
    return prediction
