from app import app
from flask import request
from flask import render_template
from app import lemmatizer
import json
from functools import wraps
#from estonian_wordcloud import lemm

#@app.route("/")
#def index():
#    return render_template('index.html',
#                           title='Home')


def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            resp = func(*args, **kwargs)
            resp.set_data('{}({})'.format(
                str(callback),
                resp.get_data(as_text=True)
            ))
        else:
            return f(*args, **kwargs)
    return decorated_function

@app.route('/create_bubbles', methods=['POST'])
@support_jsonp
def create_bubbles():
    text = request.json['text']
    lem_freq = lemmatizer.lemmatize(text)
    #return render_template('lemmatized.html', lem_text=lemmatizer.lemmatize(text))
    print(lem_freq)
    return json.dumps(lem_freq)

