import subprocess

import re

import pymongo
from pymongo.server_api import ServerApi


def call_banc(user):
    # saida_comando = subprocess.run(
    #     ['mongosh "mongodb+srv://cluster0.mxhpuxx.mongodb.net/myFirstDatabase" --apiVersion 1 --username vitinho --password Internacional8!'], capture_output=True).stdout.decode()
    client = pymongo.MongoClient(
        "mongodb+srv://vitinho:internacional8@cluster0.mxhpuxx.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
    db = client.Cluster0
    print(client.list_database_names())
    for info in user.props:
        db.password.insert_many([
            {
                "nome_pessoa": user.nome,
                "rede": {
                    "senha": info.senha,
                    "nome_rede": info.nome,
                }
            }
        ])
