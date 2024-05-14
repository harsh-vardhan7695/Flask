from flask import Flask,render_template,request,url_for,jsonify
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import base64


app = Flask(__name__)


@app.route('/Home',methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/read_csv_file',methods=['POST'])
def read_csv(csv):
    if file not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        df = pd.read_csv(file)
        return df.to_json(orient = 'records')

@app.route('/plot_csv_file',methods = ['POST'])
def plot_csv():
    file = request.files['file']
    if file:
        df = pd.read_csv(file)
        plt.figure()
        df.plot()
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        return f'<img src="data:image/png;base64,{plot_url}"/>'
    
if __name__ == '__main__':
    app.run(debug=True)