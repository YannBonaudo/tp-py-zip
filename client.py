from kivy.app import App
from kivy.uix.button import Button
from ftplib import FTP


def telecharger_fichier(self):
    ftp = FTP('127.0.0.1' )  
    ftp.login("user", "pass")
    ftp.cwd('/files')
    ftp.retrbinary('RETR nom_du_fichier.txt', contenu_du_fichier)
    ftp.quit()

class MonApplication(App):
    def build(self):
        bouton = Button(text='Télécharger le fichier')
        bouton.bind(on_release=telecharger_fichier)
        return bouton

MonApplication().run()

