# -*- coding: utf-8 -*-
"""Theokleiao_NER.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lvqafmcThfkUpZ8LFTaAZ9DPzjoANhJH
"""

import re
from collections import Counter
from bs4 import BeautifulSoup
import requests
from spacy import displacy
import en_core_web_sm

NLP = en_core_web_sm.load()

DOC = NLP('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
print([(X.text, X.label_) for X in DOC.ents])

print([(X, X.ent_iob_, X.ent_type_) for X in DOC])

def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))
NY_BB = url_to_string('https://en.wikipedia.org/wiki/Australia')
ARTICLE = NLP(NY_BB)
len(ARTICLE.ents)

LABELS = [x.label_ for x in ARTICLE.ents]
Counter(LABELS)

ITEMS = [x.text for x in ARTICLE.ents]
Counter(ITEMS).most_common(3)

SENTENCES = [x for x in ARTICLE.sents]
print(SENTENCES[20])

displacy.render(NLP(str(SENTENCES[17])), jupyter=True, style='ent')

displacy.render(NLP(str(SENTENCES[19])), style='dep', jupyter=True, options={'distance': 90})

[(x.orth_, x.pos_, x.lemma_) for x in [y for y in NLP(str(SENTENCES[17])) if not y.is_stop and y.pos_ != 'PUNCT']]

dict([(str(x), x.label_) for x in NLP(str(SENTENCES[17])).ents])

print([(x, x.ent_iob_, x.ent_type_) for x in SENTENCES[17]])

displacy.render(NLP(str(SENTENCES)), jupyter=True, style='ent')