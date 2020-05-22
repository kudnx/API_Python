from flask import Flask, jsonify, request
import json
app = Flask(__name__)

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

@app.route('/waifu/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def waifu(id):
    if request.method == 'GET':
        try:
            response = waifus[id]
        except IndexError:
            mensagem = 'Waifu de ID {} não existe'.format(id)
            response = {'status' : 'erro', 'mensagem' : mensagem}
        except Exception:
            mensagem = 'Ero desconhecido. Procure o administrador da API'
            response = {'status' : 'erro' , 'mensagem' : mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        waifus[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        waifus.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registo excluido!!'})

@app.route('/waifus/', methods = ['POST', 'GET'])
def lista_waifus():
    if request.method == 'POST':
        dados = json.loads(request.data)
        waifus.append(dados)
        return jsonify({'status': 'Sucesso', 'mensagem' : 'Registro Inserido'})
    elif request.method == 'GET':
        return jsonify(waifus)

if __name__ == '__main__':
    app.run(debug=True)