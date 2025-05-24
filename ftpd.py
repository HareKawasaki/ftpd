from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
def getmessage():
    print('Use this script will share files without authentication')
    address=input('File Address:')
    port=int(input('Port:'))
    return (address,port)
def create_server(address,port):
    users=DummyAuthorizer()
    users.add_anonymous(address,perm="elradfmw")
    handler = FTPHandler
    handler.authorizer = users
    server = FTPServer(('0.0.0.0', port), handler)
    server.serve_forever()
address,port=getmessage()
create_server(address,port)


