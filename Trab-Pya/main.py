from functions.busc_wi_fi import Algo_Interesante

from classes.conteudo import Conteudo

from functions.call_banc import call_banc

import PySimpleGUI as sg

# from get_user import get_user


if __name__ == '__main__':

    sg.theme('Black')   # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Bem Vindo ao explorador de senhas em Python', font='Courier 12', text_color="green")],
              [sg.Text('Seu nome', font='Courier 12', text_color="green"), sg.InputText("",
                                                                                        font='Courier 12', background_color='black', text_color="green")],
              [sg.Text(size=(40, 1), key='-OUTPUT-')],
              [sg.Button('Ok'), sg.Button('Sair')]]
    layoutdois = [[sg.Text('Senhas Salvas', font='Courier 12')],
                  [sg.Text('Senhas Salvas', font='Courier 12', text_color="green")]]

    window = sg.Window('Explorador de senhas Wi-Fi',
                       layout, element_justification='c')

    while True:
        event, values = window.read()
        try:
            nome = values[0]
        except TypeError: 
            print("Mano, deu erro aq, me desculpe")
        if nome != '' and event == 'Ok':
            print(nome)
            obj = Algo_Interesante()
            user = Conteudo(nome, obj)
            window['-OUTPUT-'].update('Senhas Salvas! ', text_color='yellow')
            sg.popup("Senhas salvas!")
            call_banc(user)


        elif event == sg.WIN_CLOSED or event == 'Sair':  # if user closes window or clicks cancel
            break
        else:
            sg.popup('Digite seu nome!')
            # window.close()

    # print("Olá Bem-Vindo...")
    # print("")
    # obj = Algo_Interesante()
    # user = Conteudo(input("Seu nome:"), obj)


    # for info in user.props:
    #     print("nome do wi-fi: %s" % info.nome)
    #     print("senha: %s" % info.senha)



    # get_user()
