import tensorflow as tf
import numpy as np


model = tf.keras.models.load_model("mnist_model.h5")
model.summary()

def predict_digit(image):
    """
    input: preprocessed image data (28*28)
    output: predicted number (0-9)
    """
    predictions = model.predict(image)
    print(f"Model prediction: {predictions}")
    predicted_digit = np.argmax(predictions)
    return int(predicted_digit)