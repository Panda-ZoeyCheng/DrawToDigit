from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predict_digit
from utils import preprocess_image

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        image_data = data.get("image")

        if not image_data:
            return jsonify({"error": "No image provided"}), 400
        
        processed_image = preprocess_image(image_data)
        prediction = predict_digit(processed_image)

        return jsonify({"prediction": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)