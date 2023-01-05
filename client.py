from kivy.app import App
from kivy.uix.button import Button
from ftplib import FTP


def telecharger_fichier(self):
    # connexion au serveur ftp
    ftp = FTP('127.0.0.1' )  
    ftp.login("user", "pass")
    ftp.cwd('/')
    # copie temporaire du zip sur le serveur ftp 
    ftp.cwd("/")
    with open("temp_server_file.zip", "wb") as file:
        ftp.retrbinary("RETR fichier.zip", file.write)
    ftp.quit()

class MonApplication(App):
    def build(self):
        bouton = Button(text='Télécharger le fichier')
        bouton.bind(on_release=telecharger_fichier)
        return bouton

MonApplication().run()

