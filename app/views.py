from app import app
from flask import request
from flask import render_template
from app import lemmatizer
import json
#from estonian_wordcloud import lemm

#@app.route("/")
#def index():
#    return render_template('index.html',
#                           title='Home')

@app.route('/create_bubbles', methods=['POST'])
def create_bubbles():
    text = request.json['text']
    lem_freq = lemmatizer.lemmatize(text)
    #return render_template('lemmatized.html', lem_text=lemmatizer.lemmatize(text))
    print(lem_freq)
    return json.dumps(lem_freq)

