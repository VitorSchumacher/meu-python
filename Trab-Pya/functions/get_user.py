import subprocess

import re


def get_user():
    saida_do_comando = subprocess.run(
        ["whoami"], capture_output=True).stdout.decode()
    nome_do_perfil = (re.findall(
        "desktop-sg9i15p\(.*)\r", saida_do_comando))
    print(nome_do_perfil)
