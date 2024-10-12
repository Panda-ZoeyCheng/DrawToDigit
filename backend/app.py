from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predict_digit
from utils import preprocess_image

from PIL import Image
from io import BytesIO
import base64
import os

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        image_data = data.get("image")
        print("Received image data:", image_data[:100])

        if not image_data:
            return jsonify({"error": "No image provided"}), 400
        
        processed_image = preprocess_image(image_data)
        prediction = predict_digit(processed_image)

        return jsonify({"prediction": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/save-image', methods=['POST'])
def save_image():
    try:
        data = request.json
        image_data = data.get('image')

        image_data = image_data.split(",")[1]
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))

        save_dir = 'saved_images'
        os.makedirs(save_dir, exist_ok=True)
        image_name = f'{save_dir}/digit_{len(os.listdir(save_dir))}.jpg'

        image = image.convert('RGB') 
        image.save(image_name)
        print(f"Image saved as {image_name}")

        return jsonify({'message': 'Image saved successfully', 'filename': image_name}), 200
    except Exception as e:
        print("Error saving image:", str(e))
        return jsonify({'error': 'Failed to save image'}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)