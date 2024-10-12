# DrawToDigit Backend

The backend is built using the Flask framework, responsible for receiving handwritten digit image data sent from the frontend, using a pre-trained deep learning model to make predictions, and returning the results to the frontend.

## Main Files

- `app.py`: Main Flask server file, defines routes like `/predict` and `/save-image`
- `model.py`: Logic for loading and making predictions with the model
- `utils.py`: Contains image preprocessing functions
- `model_training.ipynb`: Jupyter Notebook used for training the model
- `mnist_model.h5`: Pre-trained model file

## How to Run

1. Create env:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

   ```

2. Install Dependency:

   ```bash
   pip install -r requirements.txt

   ```

3. Start:
   ```bash
   python app.pu --port=5001
   ```
