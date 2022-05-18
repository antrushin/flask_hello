from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(1+2)
    return '<h1>Hello, MY very best friend!!!</h1>'