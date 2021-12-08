from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle
app = Flask(__name__)
pickle_in = open('clf.pkl', 'rb')
classifier = pickle.load(pickle_in)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        var = request.form['v']
        skew = request.form['s']
        cur = request.form['c']
        ent = request.form['e']
        temp = [var,skew,cur,ent]
        temp = np.array(temp)
        temp = temp.reshape(1,-1)
        my_prediction = classifier.predict(temp)
        if my_prediction == 0:
            return render_template('predict.html', predict='The given Bank Note is Authentic')
        else:
            return render_template('predict.html', predict='The given Bank Note is Fake')


if __name__ == '__main__':
    app.run(debug=True)