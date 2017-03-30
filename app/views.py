from app import app
from urllib.parse import unquote
from flask import request
from flask import render_template
from app import lemmatizer
import json
import datetime
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
            content = str(callback) + '(' + str(f(*args,**kwargs)) + ')'
            return app.response_class(content, mimetype='application/json')
        else:
            return f(*args, **kwargs)
    return decorated_function

@app.route('/create_bubbles', methods=['GET'])
@support_jsonp
def create_bubbles():
    text = unquote(request.args.get("text"))
    print("{} -- {} -- {}".format(datetime.datetime.now(), request.remote_addr, text))
    lem_freq = lemmatizer.lemmatize(text)
    return json.dumps(lem_freq)

