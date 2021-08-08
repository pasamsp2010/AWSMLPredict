import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(_name_)
model = pickel.load(open('model.pk1', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    ''' For rendering results on HTML GUI'''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='Employee Salary should be ${}'.formate(output))

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)
