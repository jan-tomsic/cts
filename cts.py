from flask import Flask

cts = Flask(__name__)

@cts.route('/ping')
def ping():
    return 'OK'

@cts.route('/foo')
def foo():
    return 'bar'

