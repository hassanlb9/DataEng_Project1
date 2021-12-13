from flask import Flask, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import unittest
nltk.download('vader_lexicon')
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        inp = request.form.get("inp")
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp)
        compound = round((1 + score['compound'])/2, 2)

        if score["compound"] <= -0.05:
            return render_template('home.html', final=compound, text1=score["neg"], text2=score["pos"], text3=score["neu"], message=" ☹ ☹ ☹ Negative")
        elif score["compound"] >= 0.05:
            return render_template('home.html', final=compound, text1=score["neg"], text2=score["pos"], text3=score["neu"], message=" 😀 😀 😀 Positive")
        else:
            return render_template('home.html', final=compound, text1=score["neg"], text2=score["pos"], text3=score["neu"],message=" 😐 😐 😐 Neutral")
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")