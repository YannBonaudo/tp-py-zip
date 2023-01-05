from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from ftplib import FTP

# Creation d'un serveur ftp
authorizer = DummyAuthorizer()
authorizer.add_user("user", "pass", "./", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
