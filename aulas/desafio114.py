import socket

confiaveis = ['www.pudim.com.br']

def check_host():
   global confiaveis
   for host in confiaveis:
     a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     a.settimeout(.5)
     try:
       b=a.connect_ex((host, 80))
       if b==0: #ok, conectado
         return True
     except:
       pass
     a.close()
   return False


print (check_host() and "Conexão Ativa" or "Conexão Inativa")