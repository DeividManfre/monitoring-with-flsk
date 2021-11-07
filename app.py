from flask import Flask, jsonify, request
from monitoring import Monitoring


app = Flask(__name__)


@app.route('/monitoring', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        ram = Monitoring().ram
        memory = Monitoring().memory
        return jsonify({'Ram': ram, 'Memory used' : memory })