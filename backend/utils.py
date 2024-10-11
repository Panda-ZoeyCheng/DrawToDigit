import base64
from io import BytesIO
from PIL import Image
import numpy as np

def preprocess_image(image_base64):
    image_data = base64.b64decode(image_base64.split(",")[1])
    image = Image.open(BytesIO(image_data)).convert("L")
    image = image.resize((28, 28))
    image_array = np.array(image)
    image_array = image_array.reshape(1, 28, 28, 1)
    return image_array