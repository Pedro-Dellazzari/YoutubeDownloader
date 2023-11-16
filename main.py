#Importando as bibliotecas 
import customtkinter
import os
from tkinter import scrolledtext
import subprocess

#Setando aparência do programa
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


########### FUNÇÕES ########################
# Janela de Setup para instalar as libs
def Setup_Window():
    setupW = customtkinter.CTkToplevel(window)
    
    #setupW.geometry("450x150")
    setupW.title("Setup")

    #Criando o texto 
    setup_text = customtkinter.CTkLabel(setupW, text='Make sure to install all the packages inside requirements.txt')
    setup_text.grid(row=0, column=0, padx=5, pady=5)

    setup_text_2 = customtkinter.CTkLabel(setupW, text='If download private videos, make sure to be logged in chrome browser')
    setup_text_2.grid(row=1, column=0, padx=5, pady=5)

    #Falando da biblioteca usada 
    setup_text_3 = customtkinter.CTkLabel(setupW, text='This program uses the library yt-dlp to download videos')
    setup_text_3.grid(row=2, column=0, padx=5, pady=5)

    setupW.attributes('-topmost', True)

# Função de download de vídeos do youtube
def Download():
    #Limpando o texto
    cmd_text.delete(1.0, customtkinter.END)

    #Pegando a url que o usuário deu de input 
    url = input_url.get()

    #Pegando o valor setado no espaço de privado ou público 
    privado = Private_Choice.get()


    #Checando se o vídeo é privado 
    if privado == 'Private':

        #Passando o comando para usar no cmd
        comando = f'yt-dlp --cookies-from-browser chrome -P /videos {url}'

        os.system(comando)

        resultado = subprocess.run(comando, capture_output=True, text=True)

        cmd_text.insert(customtkinter.END, resultado.stdout)
        cmd_text.insert(customtkinter.END, resultado.stderr)

    
    elif privado == 'Public':

        #Passando o comando para usar no cmd
        comando = f'yt-dlp -P /videos {url}'

        os.system(comando)

        resultado = subprocess.run(comando, capture_output=True, text=True)

        cmd_text.insert(customtkinter.END, resultado.stdout)
        cmd_text.insert(customtkinter.END, resultado.stderr)

#Criando a janela 
window = customtkinter.CTk()
window.geometry("450x350")
window.title("Youtube Downloader")

#Criando o input para o link do youtube
input_url = customtkinter.CTkEntry(window, width=150, placeholder_text='Youtube Link')
input_url.grid(row=0, column=0, padx=5, pady=5)

#Criando a opção para selecionar se o vídeo é privado ou não 
user_options = ['Private','Public']

#Criando o Combobox
Private_Choice = customtkinter.CTkComboBox(window, values=user_options)
Private_Choice.grid(row=0, column=1)

#Fazendo botão para fazer download
download_button = customtkinter.CTkButton(window, text='Download', command=Download)
download_button.grid(row=1, column=0, padx=5, pady=5)

#Fazendo um texto com o link para outra janela mostrando o setup
setup_link = customtkinter.CTkButton(window, text='Setup', command=Setup_Window)
setup_link.grid(row=1, column=1, padx=5, pady=5)


#Criando uma área de texto para info de privado 
private_info = customtkinter.CTkLabel(window, text='You must be logged in Chrome in Youtube to download private videos')
private_info.grid(row=2, column=0, columnspan=3, padx=10, pady=2)

#Criando uma área de texto para info de onde os arquivos ficaram disponiveís 
file_info = customtkinter.CTkLabel(window, text='Files downloaded in "videos" folder inside the app dir ;)')
file_info.grid(row=3, column=0, columnspan=3)

cmd_text = scrolledtext.ScrolledText(window, width=50, height=10)
cmd_text.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

cmd_text.insert(customtkinter.END, 'This will show the output of the library yt-dlp')


#Fazendo mainloop
window.mainloop()