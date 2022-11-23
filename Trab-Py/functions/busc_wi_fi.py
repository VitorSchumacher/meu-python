import subprocess

import re

from classes.senha_perfil import Senha_perfil

def Algo_Interesante():
    saida_do_comando = subprocess.run(
        ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

    nomes_do_perfil = (re.findall(
        "Todos os Perfis de Usuários: (.*)\r", saida_do_comando))
    lista_wifi = []
    if len(nomes_do_perfil) != 0:
        for nome in nomes_do_perfil:
            perfil_wifi = {}
            # no retorno
            informacao_perfil = subprocess.run(
                ["netsh", "wlan", "show", "profile", nome], capture_output=True).stdout.decode()
            if re.search("Chave de segurança           : Ausente", informacao_perfil):
                continue
            else:
                perfil_wifi["ssid"] = nome
                informacao_senha_perfil = subprocess.run(
                    ["netsh", "wlan", "show", "profile", nome, "key=clear"], capture_output=True).stdout.decode()
                senha = re.search(
                    "Conteúdo da Chave            : (.*)\r", informacao_senha_perfil)
                if senha == None:
                    perfil_wifi["password"] = None
                else:
                    perfil_wifi["password"] = senha[1]
                objPerfil = Senha_perfil(perfil_wifi["ssid"],perfil_wifi["password"])
                lista_wifi.append(objPerfil)

    # for x in range(len(lista_wifi)):
    #     print(lista_wifi[x].nome)

    return lista_wifi
