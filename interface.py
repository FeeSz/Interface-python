import customtkinter as ctk   

# Aparência da janela: modo escuro pra não queimar os olhos
ctk.set_appearance_mode('light')

# validação de login: pega os valores dos campos, limpa espaços e compara
def validar_login():
    user = user_area.get().strip().lower()
    password = password_area.get().strip().lower()

    # se bater com as credenciais esperadas, mostra sucesso, senão erro
    if user == 'felype' and password == '123456':
        resultado_login.configure(text='Login realizado com Sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Login incorreto', text_color='red')

# instancia principal do customtkinter
app = ctk.CTk()
# título e tamanho da janela do app
app.title('sistema de Login')
app.geometry('300x300')


# campos e botões da interface
# Label do usuário
user = ctk.CTkLabel(app, text='Usuário')
user.pack(pady=10)
user_area = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
user_area.pack(pady=10)

# Label da senha
password = ctk.CTkLabel(app, text='Senha')
password.pack(pady=10)
password_area = ctk.CTkEntry(app, placeholder_text='Insira sua senha')
password_area.pack(pady=10) 

# Botão de login: chama validar_login quando clicado
login_button = ctk.CTkButton(app, text='Login', command=validar_login)
login_button.pack(pady=10)

# Label que mostra o resultado da tentativa de login
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)


# inicia o loop da interface
app.mainloop()