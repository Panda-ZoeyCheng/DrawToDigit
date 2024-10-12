import base64
from io import BytesIO
from PIL import Image
import numpy as np
import os

def preprocess_image(image_data):

    try:
        print("Current working directory:", os.getcwd())

        image_data = image_data.split(",")[1] 
        image_bytes = base64.b64decode(image_data)

        image = Image.open(BytesIO(image_bytes))
        print("Image successfully decoded.")

        image.convert('RGB').save('received_image.jpg', 'JPEG')
        print("Image saved as 'received_image.jpg'.")

        image = image.convert("L").resize((28, 28)) 

        image = 255 - np.array(image)
        Image.fromarray(image).convert('RGB').save('processed_image.jpg', 'JPEG')
        print("Processed image saved as 'processed_image.jpg'.")

        image = image / 255.0

        image = image.reshape(1, 28, 28, 1)

        print(f"Preprocessed image data: {image}")
        return image
    
    except Exception as e:
        print("Error in preprocess_image: ", str(e))
        return None