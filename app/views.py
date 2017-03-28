from app import app
from math import cos
from flask import request
from flask import render_template
from estnltk import Text


@app.route("/")
@app.route("/index")
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route("/cos")
def app_cos():
    value = float(request.args.get("v"))
    shift = float(request.args.get("shift"))
    return "The cos of {} is {:.3f}".format(value, cos(value) + float(shift))


def lemmatize(text):
    """
    Parameters
    ----------
    text : string
        Text to lemmatize


    Output
    ------
    return : string
        Lemmatized text
    """
    words = []
    for word in list(Text(text).get.lemmas.postags.as_zip):
        if "|" in word[0] and "V" in word[1]:
            for ambig in word[0].split("|"):
                if ambig.endswith("ma"):
                    words.append(ambig)
                    break # sest ma-ga lõppevaid lemmasid võib samal sõnal olla mitu, võta ainult esimene
        elif "|" in word[0]:
            words.append(word[0].split("|")[0])
        elif "Z" not in word[1]:
            words.append(word[0])
    return " ".join(words)


@app.route('/lemmatize_form/', methods=['POST'])
def lemmatize_form():
    text = request.form['text']
    print(text)
    return render_template('lemmatized.html', lem_text=lemmatize(text))

