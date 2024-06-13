import os
import numpy as np
import pandas as pd
import flask
import pickle
from flask import Flask, redirect, url_for, request, render_template
from sklearn.preprocessing import OneHotEncoder
import umap

app = Flask(__name__, template_folder='templates')

@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

def ValuePredictor(to_predict_list):
    # Load necessary models
    loaded_umap = pickle.load(open("umap_model.pkl", "rb"))
    loaded_kmeans = pickle.load(open("kmeans_model.pkl", "rb"))
    ohe = pickle.load(open("ohe.pkl", "rb"))

    # Preprocess input
    df_input = pd.DataFrame([to_predict_list], columns=['shape', 'margin', 'density'])
    df_input['shape'] = df_input['shape'].astype('object')
    df_input['margin'] = df_input['margin'].astype('object')
    df_input['density'] = df_input['density'].astype('object')

    # One-hot encode categorical variables
    df_onehot_categorical = df_input.copy()
    encoder_categorical = ohe.transform(df_onehot_categorical)
    
    # Apply UMAP transformation
    umap_components = loaded_umap.transform(encoder_categorical)
    
    # Predict with KMeans
    result = loaded_kmeans.predict(umap_components)
    return result[0]

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.values()
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)

        if result == 0:
            group = 'Grupo 0'
            prediction = '< 20%'
        elif result == 1:
            group = 'Grupo 1'
            prediction = '> 75%'
        elif result == 2:
            group = 'Grupo 2'
            prediction = '> 50%'
        elif result == 3:
            group = 'Grupo 3'
            prediction = '> 75%'
        elif result == 4:
            group = 'Grupo 4'
            prediction = '< 20%'
        elif result == 5:
            group = 'Grupo 5'
            prediction = '> 75%'
        elif result == 6:
            group = 'Grupo 6'
            prediction = '0%'

        return render_template('result.html', group=group, prediction=prediction)

@app.route('/model_result')
def model_result():
    return render_template('model_result.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
