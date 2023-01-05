from kivy.app import App
from kivy.uix.button import Button
from ftplib import FTP
from zipfile import ZipFile

def lire_contenu_zip(): 
    print("lire lire lire lire")
    # Create a ZipFile Object and load sample.zip in it
    with ZipFile("temp_server_file.zip", 'r') as zipObj:
        # Get list of files names in zip
        listOfiles = zipObj.namelist()
        # Iterate over the list of file names in given list & print them
        for elem in listOfiles:
            print(elem)
            if elem == "fichier/lorem.txt" :
                print(zipObj.getinfo(elem))

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

    lire_contenu_zip()
    


class MonApplication(App):
    def build(self):
        bouton = Button(text='Télécharger le fichier')
        bouton.bind(on_release=telecharger_fichier)
        return bouton

MonApplication().run()

