from flask import Flask, request, jsonify
from model import predict_digit
from utils import preprocess_image

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    image_data = data.get("image")

    if not image_data:
        return jsonify({"error": "No image provided"}), 400
    
    processed_image = preprocess_image(image_data)
    prediction = predict_digit(processed_image)

    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)