import socket
import sys
import _thread as thread


host = '192.168.0.196'
port = 5000

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
sock.bind((host, port))
# Listen for incoming connections
sock.listen(5)



print("Aguardando cenexão!")

def conectado(con, cliente):

    print('Conectado por ', cliente)

    while True:
        arquivos = open("arquivo.txt", "a")
        try:
            msg = con.recv(1024)
            if not msg: break
            print(msg.decode('ascii'))
            arquivos.write(msg.decode('ascii'))
        except:
            print('Finalizando conexao do cliente', cliente)
            con.close()
            arquivos.close()
            thread.exit()

while True:

    con, cliente = sock.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))

sock.close()
