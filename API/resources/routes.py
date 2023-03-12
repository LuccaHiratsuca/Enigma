from flask_restful import Resource
from flask import request, jsonify, render_template, redirect, url_for, make_response
from models.model import *

alfabeto_cifrado = "bcdefghijkl mnopqrstuvwxyza"
cifrador_auxiliar = "ijkl mnopqrstuvwxyzabcdefgh"

class paraString(Resource):
    def post(self):
        body = request.get_json( force=True )
        string = para_string(np.array(body['key']))
        return {'Resultado de mensagem para String:': string}, 200
    
class paraOneHot(Resource):
    def post(self):
        body = request.get_json( force=True )
        resultado = para_one_hot(body['key'])
        return {'Resultado de String para OneHot:': resultado.tolist()}, 200

class Cifra(Resource):
    def post(self):
        body = request.get_json( force=True )
        msg = body['msg']
        P = para_one_hot(alfabeto_cifrado)
        resultado = cifra(msg,P)
        return {'Resultado da mensagem criptografada (Cifrar)': resultado}, 200
    
class deCifra(Resource):
    def post(self):
        body = request.get_json( force=True )
        msg = body['msg']
        P = para_one_hot(alfabeto_cifrado)
        resultado = de_cifra(msg,P)
        return {'Resultado da mensagem descriptografada (de_Cifrar)': resultado}, 200
    
class Enigma(Resource):
    def post(self):
        body = request.get_json( force=True )
        msg = body['msg']
        P = para_one_hot(alfabeto_cifrado)
        E = para_one_hot(cifrador_auxiliar)
        resultado = enigma(msg,P,E)
        return {'Resultado da mensagem criptografada': resultado}, 200
    
class deEnigma(Resource):
    def post(self):
        body = request.get_json( force=True )
        msg = body['msg']
        P = para_one_hot(alfabeto_cifrado)
        E = para_one_hot(cifrador_auxiliar)
        resultado = de_enigma(msg,P,E)
        return {'Resultado da mensagem descriptografada': resultado}, 200