from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, Soy una aplicación Flask de prueba de Edmundo'