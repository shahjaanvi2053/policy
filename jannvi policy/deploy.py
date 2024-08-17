from flask import Flask, render_template, request
import pickle
import os
import sys
import tensorflow as tf
# from tensorflow.keras.preprocessing.text import Tokenizer
sys.modules['keras.preprocessing.text'] = tf.keras.preprocessing.text

import joblib

model = joblib.load('model/sentiment_model.pkl')


if isinstance(model, tf.keras.preprocessing.text.Tokenizer):
    print("Loaded model is a Tokenizer, not a trained model.")
else:
    print("Loaded model is a trained model.")
app = Flask(__name__)


# the sentiment analysis model
model_path = os.path.join('model', 'sentiment_model.pkl')
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        prediction = model.predict([review])
        
        if prediction == 1:
            sentiment = "Positive"
        else:
            sentiment = "Negative"
        
        return render_template('/template/index.html', prediction=sentiment, review=review)

if __name__ == '__main__':
    
    app.run(debug=True)
