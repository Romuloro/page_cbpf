import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin

DIRETORIO = "/home/romulo/projetos_pessoais/page_cbpf_/back_end_python/output"

api = Flask(__name__)

#CORS(api, resources={r'/*': {"origins": 'http://localhost:4000'}})



@api.route("/arquivos", methods=["GET"])
def lista_arquivos():
    arquivos = []

    for nome_do_arquivo in os.listdir(DIRETORIO):
        endereco_do_arquivo = os.path.join(DIRETORIO, nome_do_arquivo)

        if(os.path.isfile(endereco_do_arquivo)):
            arquivos.append(nome_do_arquivo)

    return jsonify(arquivos)


@api.route("/arquivos/<nome_do_arquivo>",  methods=["GET"])
def get_arquivo(nome_do_arquivo):
    return send_from_directory(DIRETORIO, nome_do_arquivo, as_attachment=True)

@cross_origin()
@api.route("/arquivos", methods=["POST"])
def post_arquivo():
    arquivo = request.files.get("meuArquivo")

    print(arquivo, "aaaa")
    nome_do_arquivo = arquivo.filename
    arquivo.save(os.path.join(DIRETORIO, nome_do_arquivo))

    return '', 201


if __name__ == "__main__":
    api.run(debug=True, port=8080)