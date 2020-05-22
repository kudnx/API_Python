from flask import Flask, request
from flask_restful import Resource, Api
import json
from API.habilidades import habilidades

waifus = [
    {
        'nome' : 'Grea',
        'anime' : 'Manaria Friends'
    },
    {
        'nome' : 'Ikaros',
        'anime' : 'Sora no Otoshimono'
    },
    {
        'nome' : 'Kyouhime',
        'anime' : 'Fate Grand Order'
    },
    {
        'nome' : 'You Watanabe',
        'anime' : 'Love Live Sunshine'
    }
]

app  =  Flask(__name__)
api = Api(app)

class Waifu(Resource):
    def get(self, id):
        try:
            response = waifus[id]
        except IndexError:
            mensagem = 'Waifu de ID {} não existe'.format(id)
            response = {'status' : 'erro', 'mensagem' : mensagem}
        except Exception:
            mensagem = 'Ero desconhecido. Procure o administrador da API'
            response = {'status' : 'erro' , 'mensagem' : mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        waifus[id] = dados
        return dados

    def delete(self, id):
        waifus.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registo excluido!!'}

class listaWaifus(Resource):
    def get(self):
        return waifus

    def post(self):
        dados = json.loads(request.data)
        waifus.append(dados)
        return {'status': 'Sucesso', 'mensagem' : 'Registro Inserido'}

api.add_resource(Waifu, '/waifu/<int:id>/')
api.add_resource(listaWaifus, '/waifus/')
api.add_resource(habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)