import socket
from threading import Thread
#
vetorid=[]
vetorcadastro=[]
##class user(object): 	
##
##    def __init__(self, nome, senha):
##        self.nome =nome
##        self.senha =senha


def cadastrodousuario(conn):	# funcao basica de login e cadastro (menu)
    global vetorid,vetorcadastro              #permitir que facamos mundacas na variavel
    nome_r=conn.recv(1024)
    if nome_r in vetorid:
        conn.sendall("not_ok")
    else:
        conn.sendall("ok")
    lista_cadastro=conn.recv(4096)
    vetorcadastro.append(lista_cadastro)
        
##    nome_r=conn.recv()    
##    sleep(0.1)
##    senha_r=conn.recv()
##    login=user (nome_r,senha_r)
##    lista.append(login)

def menu(conn):
    while True:
        fazer=conn.recv(256)
        if fazer=="1":
            cadastrodousuario(conn)
        #if fazer==2:
            #loginusuario(conn)
##def menu(conn):
##		dados = con.recv(4096)
##		recebidos = dados.split(',')
##		print recebidos
HOST=''  # Interface inicial padrao
PORT=60011
# Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind((HOST, PORT)) 
controle=0
##logados = {}
##dadosdeusuario = {}
##lista=[]
##registradordeitem=0
while controle==0:
    s.listen(1)  # espera chegar pacotes na porta especificada
    conn, addr = s.accept()  # Aceita uma conexao
    t = Thread(target=menu, args=(conn,))
    t.start()
