from flask import Flask, render_template, request
import unittest
import pickle
import numpy as np
from keras.preprocessing.sequence import pad_sequences
import keras

app = Flask(__name__)

config = pickle.load(open('./config.pkl', 'rb'))
model = keras.models.load_model('./model_sentiment_v1.h5')


@app.route('/senti', methods=["GET", "POST"])
def predict_sentiment():
    config = pickle.load(open('./config.pkl', 'rb'))
    model = keras.models.load_model('./model_sentiment_v1.h5')
    if request.method == "POST":
       inp = request.form.get("inp")
       text = [inp] if type(inp) == np.str else inp
       tokenizer = config['tokenizer']['tokenizer']
       text = tokenizer.texts_to_sequences(text)
       text = pad_sequences(text, maxlen     = config['tokenizer']['token_maxlen'],
                               padding    = config['tokenizer']['padding_type'],
                               truncating = config['tokenizer']['truncating_type'],
                               value      = config['tokenizer']['padding_value'])
       sentiment = model.predict(text,batch_size=1,verbose = 0)[0]
       argmax_sent = np.argmax(sentiment)
       if  argmax_sent == 1:
           return render_template('home.html', message="Positive")
       if  argmax_sent == 0:
           return render_template('home.html', message="Neutre")
       if  argmax_sent != 1:
           return render_template('home.html', message="Negative")
       
       
       #sentiment_text  = 'Positive' if  argmax_sent == 1 ifElse 'Negative'
       #sentiment_score = sentiment[argmax_sent]
    #return((sentiment_text, sentiment_score)) 
    return render_template('home.html')    

if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = "8000")