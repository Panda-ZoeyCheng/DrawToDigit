import tensorflow as tf
import numpy as np
import boto3
import os

s3 = boto3.client("s3")

BUCKET_NAME = "zappa-drawtodigit"
MODEL_KEY = "models/mnist_model.h5"

LOCAL_MODEL_PATH = '/tmp/mnist_model.h5'

# model = tf.keras.models.load_model("mnist_model.h5")
# model.summary()

def load_model_from_s3():
    if not os.path.exists(LOCAL_MODEL_PATH):
        s3.download_file(BUCKET_NAME, MODEL_KEY, LOCAL_MODEL_PATH)


    model = tf.keras.models.load_model(LOCAL_MODEL_PATH)
    return model

model = load_model_from_s3()

def predict_digit(image):
    """
    input: preprocessed image data (28*28)
    output: predicted number (0-9)
    """
    predictions = model.predict(image)
    print(f"Model prediction: {predictions}")
    predicted_digit = np.argmax(predictions)
    return int(predicted_digit)