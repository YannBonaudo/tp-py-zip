from kivy.app import App
from kivy.uix.button import Button
from ftplib import FTP
from zipfile import ZipFile

# connexion au serveur ftp
# ftp = FTP('127.0.0.1' )  
# ftp.login("user", "pass")
# ftp.cwd('/')

# def telecharger_fichier(self):
#     # copie temporaire du zip sur le serveur ftp 
#     with open("temp_server_file.zip", "wb") as file:
#         ftp.retrbinary("RETR fichier.zip", file.write)

# def deziper_fichier(): 
#     # dezip le fichier temporaire recupere sur le serveur
#     with ZipFile("temp_server_file.zip", 'r') as zip_content:
#         file_list = zip_content.extractall()

def handle_click(self):
    # connexion au serveur ftp
    ftp = FTP('127.0.0.1' )  
    ftp.login("user", "pass")
    ftp.cwd('/')

    # copie temporaire du zip sur le serveur ftp 
    with open("temp_server_file.zip", "wb") as file:
        ftp.retrbinary("RETR fichier.zip", file.write)
    
    # dezip le fichier temporaire sur le serveur
    with ZipFile("temp_server_file.zip", 'r') as zip_content:
        file_list = zip_content.extractall()
    
    ftp.quit()

class MonApplication(App):
    def build(self):
        bouton = Button(text='Recupere le fichier, l encypter et le renvoyer')
        bouton.bind(on_release=handle_click)
        return bouton

MonApplication().run()

