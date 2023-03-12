from flask import Flask
from flask_restful import Api
from resources.routes import *

app = Flask(__name__)
api = Api(app)

@app.route('/')
def main():
    return "Bem vindo à nossa API de criptografia!"

api.add_resource(paraOneHot, '/enygma/encrypt/onehot') 
api.add_resource(paraString, '/enygma/decrypt/string')
api.add_resource(Cifra, '/enygma/encrypt/cifra')
api.add_resource(deCifra, '/enygma/decrypt/de-cifra')
api.add_resource(Enigma, '/enygma/encrypt/enigma')
api.add_resource(deEnigma, '/enygma/decrypt/de-enigma')

if __name__ == '__main__':
    app.run(debug=True)