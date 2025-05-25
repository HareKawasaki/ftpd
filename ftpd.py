from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from threading import Timer,Thread
import os
def getmessage():
    print('Use this script will share files without authentication')
    address=input('File Address:')
    if address=='':        
        address=os.getcwd()
    port=input('Port:')
    if port=='':
        port=2121
    else:
        port=int(port)
    stop_time=input('How many minutes do you want the program to stop:')
    if stop_time=='':
        stop_time=0
    else:
        stop_time=float(stop_time)*60
    return (address,port,stop_time)
def create_server(address,port,stop):
    users=DummyAuthorizer()
    users.add_anonymous(address,perm="elr")
    handler = FTPHandler
    handler.authorizer = users
    server = FTPServer(('0.0.0.0', port), handler)
    if stop!=0:
        time=Timer(stop,server.close_all)
        print('FTP Server will exit in {} second'.format(stop))
        time.start()
    server.serve_forever()
#Work:
address,port,stop=getmessage()
create_server(address,port,stop)