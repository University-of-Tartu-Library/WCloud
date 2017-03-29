from app import app
from flask import request
from flask import render_template
from app import lemmatizer
import json
#from estonian_wordcloud import lemm

@app.route("/")
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/lemmatize_form/', methods=['POST'])
def lemmatize_form():
    text = request.form['text']
    #print(text)
    lem_freq = lemmatizer.lemmatize(text)
    #return render_template('lemmatized.html', lem_text=lemmatizer.lemmatize(text))
    return json.dumps(lem_freq)

