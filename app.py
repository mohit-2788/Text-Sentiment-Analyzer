from flask import Flask, render_template, request
from comprehend import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment_scores = None
    sentiment_type = None

    if request.method == 'POST':
        input_text = request.form.get("input_text")  # Use the correct form field name
        if input_text:
            sentiment_type, sentiment_scores = do_sentiment(input_text)

    return render_template("index.html", sentiment_type=sentiment_type, sentiment_scores=sentiment_scores)

app.run(host="0.0.0.0", port=80, debug=True)
