from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Python Funnnciona :)"

@app.route("/barcelonaActiva")
def newEndPoint():
    return "/barcelonaActiva/Python Funnnciona :)"
