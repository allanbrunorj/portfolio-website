from flask import Flask, render_template, request, redirect, url_for, jsonify
from pyscripts.jsonparser_airbnb import check_conditions, get_prediction
# from joblib import load
app = Flask(__name__)

#NEXT STEP: PREPARAR TODOS OS DADOS DA ARRAY(JÁ COM COORDENADAS E CHECADAS)
#2- VER SE É POSSIVEL EXTRAIR SÓ O LABEL ENCODER PRA FAZER FIT NA COLUNA PROPERTY TYPE
#3- TESTAR SE O MODELO ACEITA UMA NP ARRAY E RETORNA O VALOR DA PREDIÇÃO
#4-  IMPORTAR LABEL ENCODER, ENCODAR, IMPORTAR MODELO, FAZER PREDIÇÃO, ENVIAR PREDIÇÃO PRO ROUTES.PY E ESTÁ PRONTO :)


@app.route('/')
def home_page():
    return render_template('index.html')
   
    
@app.route('/airbnb', methods=['POST'])
def airbnb():
    # data = json.load(request.data.decode("utf-8"))
    data = request.json
    conditions, coords = check_conditions(data)
    if not conditions:
        return jsonify(prediction = 'Some input is in the wrong format! check again ;)')
    else:
        prediction_ = get_prediction(data, coords)
        return jsonify(prediction = round(prediction_[0], 1))

# @app.route('/map.html')
# def map_airbnb():
#     return render_template('map.html')


if __name__ == "__main__": 
        app.run(debug=True)     

# @app.route('/<name>_<surname>')
# def name_page(address=''):
#     return render_template('name.html', address=address)
# # get the data for the requested query

###todo list:
#1- base html jinja 
#2- cnsertar inputs

###