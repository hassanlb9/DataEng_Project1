from flask import Flask, render_template, request
import unittest
import pickle
import numpy as np
from keras.preprocessing.sequence import pad_sequences
import keras
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

with open('finalized_model.pkl', 'rb') as fid:
    model = pickle.load(fid)


@app.route('/sent', methods=["GET", "POST"])
def predict_sentiment():
    with open('vocab.pkl', 'rb') as fid:
        vocab = pickle.load(fid)
        
    with open('finalized_model.pkl', 'rb') as fid:
        model = pickle.load(fid)
    if request.method == "POST":
       inp = request.form.get("inp")
       inp = [inp] if type(inp) == np.str else inp
       
       vector = vocab.transform(inp)
       pred=model.predict(vector)
       pred1 = float(pred)
       
       if  pred1 == 1:
           return render_template('home.html', message="Positive")
       
       if  pred1 == 0:
           return render_template('home.html', message="Neutral")
       
       if  pred1 == -1:
           return render_template('home.html', message="Negative")
     
       
       #sentiment_text  = 'Positive' if  argmax_sent == 1 ifElse 'Negative'
       #sentiment_score = sentiment[argmax_sent]
    #return((sentiment_text, sentiment_score)) 
    return render_template('home.html')    

if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = "1000")