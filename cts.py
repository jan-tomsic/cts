#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
