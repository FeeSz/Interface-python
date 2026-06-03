#Biblioteca da interface
from PySimpleGUI import PySimpleGUI as sg

#Tema da interface
sg.theme('Reddit')

#Layout da interface com: Input de usuário, senha, caixa de seleção e botão
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salavar o Login')],
    [sg.Button('Entrar')]
] 

#Janela (pop-up) a ser exibido
janela = sg.Window('Tela de login',layout)

#Condicional (caso as informações coincidam, retorna "Bem-vindo")
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'felype' and valores ['senha'] == '123456':
            print('Bem-vindo ao FelyDev')
            
        
