# -*- coding: utf-8 -*-

from estnltk import Text
from collections import Counter

stopwords = ["aga", "ehk", "ei", "et", "iga", "ikka", "ise", "ja", "ju", "ka", "kas", \
"keegi", "kes", "kui", "kuidas", "kõik", "mina", "mis", "miski", "nii", "olema", "oma", \
"pidama", "saama", "sama", "seal", "see", "siis", "sina", "tema", "tulema", "vaid", "veel", \
"võima", "välja", "ära", "üks", "üle", "ning", "ega", "nagu", "sest", "minema", "tulema", \
"tegema", "teine", "või"]

def lemmatize(text, limit=None):
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
    for word in list(Text(text).get.lemmas.postags.as_zip): # get all lemmas of input words and and their POS-s
        if "|" in word[0] and "V" in word[1]: # for dambigious verbs
            for ambig in word[0].split("|"):
                if ambig.endswith("ma"):
                    words.append(ambig)
                    break # because several lemmas can end with "ma", choose only the first one
        elif "|" in word[0]: # all other ambigious words
            words.append(word[0].split("|")[0])
        elif "Z" not in word[1]: # exclude punctuation
            words.append(word[0])
    stopwords_removed = [w for w in words if w not in stopwords]
    if limit:
        return Counter(stopwords_removed).most_common(limit)
    else:
        return Counter(stopwords_removed)

