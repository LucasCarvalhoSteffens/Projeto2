from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


# caulcular Fatorial
@app.route('/fatorial/<int:numero>')
def calcularFatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    resultado = fatorial
    return f"O fatorial de {numero} é {resultado}"



# caulcular Super Fatorial
def superfatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero**numero * superfatorial(numero-1)

@app.route('/superfatorial/<int:numero>', methods=['GET'])
def calcularSuperfatorial(numero):
    resultado = superfatorial(numero)
    return f"O superfatorial de {numero} é {resultado}"

if __name__ == '__main__':
    app.run(debug=True)
