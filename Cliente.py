import socket
from threading import Thread
dentrodafuncao=False
def cadastrodousuario(s):	# Registra o usuario no servidor
    global dentrodafuncao
    teste=True
    while teste==True:
        nome = raw_input('Digite seu nome:') # cadastro de nome do usuario
        s.sendall(nome)		# verificar se ha possibilidade de enviar um por um ou todos ao mesmo tempo -> porque?
        teste2=s.recv(1024)
        if teste2=="ok":    #nao existe cliente com este id ja cadastrado
            teste=False
        else:
            print "usuario ja cadastrado"              
    telefone = raw_input('Digite seu telefone') # cadastro de telefone
   # s.sendall(telefone)		
    endereco = raw_input("Digite seu endereco")
   # s.sendall = raw_input(endereco) 
    email = raw_input("Digite seu email")
   # s.sendall(endereco)	
    senha = raw_input("Digite sua senha")
   # s.sendall(senha)	
    s.sendall("Adicionar_Usuario/"+nome+'/'+telefone+'/'+endereco+'/'+email+'/'+senha)
    dentrodafuncao==False
    return
	
	#listadeenvio = [nome,telefone,endereco,email,senha]	# lista de envio de parametros 
##    x = cadastrodousuario
##    s.sendall(x)
##    return listadeenvio
def menu(s):
    global dentrodafuncao
    while True:
        if dentrodafuncao==False:
            print " digite 1 para cadastro  /n"
            print " digite 2 para login    /n "
            fazer=raw_input("digite algum numero:")
            s.sendall(fazer)
            dentrodafuncao=True
            if fazer=="1":
                cadastrodousuario(s)
  #         if fazer=="2":
#				cadastrodousuario(s)
##                ...
            
            


HOST = '127.0.0.1'    # The remote host
PORT = 60012           # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4,tipo de socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((HOST, PORT))  #Abre uma conexao com IP e porta especificados

####Mostrar menu

####Se o usuario escolheu cadastro
##cadastrodousuario()
menu(s)

print "Conectou"
