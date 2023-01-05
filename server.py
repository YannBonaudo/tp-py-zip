from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from ftplib import FTP

# Creation d'un serveur ftp
authorizer = DummyAuthorizer()
authorizer.add_user("user", "pass", "./", perm="elradfmw")

# with open('test.txt', 'w') as f:
#     f.write('Hello, World!\n')
#     f.write('This is a test file.\n')

handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()

Envoie d'un fichier sur le serveur
ftp = ftplib.FTP()
ftp.connect('127.0.0.1', port=21)
ftp.login(user='user', passwd='pass')
ftp.mkd('/files')
ftp.cwd('/files')
f = open('nom_du_fichier.txt', 'rb')
ftp.storbinary('STOR nom_du_fichier.txt', f)

fichiers = ftp.nlst()
print(fichiers)
if 'nom_du_fichier.txt' in fichiers:
    print("Le fichier existe sur le serveur FTP")
else:
    print("Le fichier n'existe pas sur le serveur FTP")
ftp.quit()
f.close()

# ftp = FTP('127.0.0.1' )  
# ftp.login("user", "pass")
# ftp.mkd('/files')
# ftp.cwd('/files')
# f = open('nom_du_fichier.txt', 'rb')
# ftp.storbinary('STOR nom_du_fichier.txt', f)
# f.close()
# ftp.quit()



