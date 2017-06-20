from flask import Flask
from flask import render_template
from flask import request

import os
import string
from sklearn.externals import joblib

from collections import Counter

app = Flask(__name__)
MODEL = os.path.join('.','model')
vec = joblib.load(os.path.join(MODEL,'vetorizador.pkl.bz2'))
mdl = joblib.load(os.path.join(MODEL,'modelo.pkl.bz2'))
stopwords = joblib.load(os.path.join(MODEL,'stopwords.pkl.bz2'))

# TODO: pickel stopwords

def prepara_estrofes(frase, translator = str.maketrans('', '', string.punctuation)):
    # Remove pontuação
    frase = frase.translate(translator)
    
    # Garante que todas as palavras estão em caixa baixa
    palavras = frase.lower().split()
    
    # Lista de stopwords que usaremos
    stop_w = set(stopwords)
    
    # Retorna apenas as palavras que não são stopwords
    palavras_filtradas = [palavra for palavra in palavras if palavra not in stop_w]
    
    # Retorna a estrofe preparada
    return(" ".join(palavras_filtradas))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        letra_post = request.form['letra']
    else:
        letra_post = 'Digite a letra aqui'

    return render_template('index.html', letra=letra_post)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        letra_post = request.form['letra']
        
        # Gera lista de versos
        versos = letra_post.split('\n')

        # Prepara versos removendo pontuacao e stopwords
        versos = [prepara_estrofes(v) for v in versos]
        new_pred = vec.transform(versos).toarray()

        # Realiza predição por verso
        prediction = mdl.predict(new_pred)

        # Encontra classe mais comum
        count = Counter(prediction)
        pred_result = count.most_common(1)[0][0]
        
        return render_template('predict.html', letra=letra_post, pred=pred_result)
        

#@app.route('/hello/')
#@app.route('/hello/<name>')
#def hello(name=None):
#    return render_template('hello.html', name=name)