from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/eeg')
def eeg():
    data = [random.randint(0, 100) for _ in range(10)]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)