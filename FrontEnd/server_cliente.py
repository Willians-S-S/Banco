import socket 

def server_cliente(ip, port):
    ip = ip             # '192.168.186.160' 
    port = port
    addr = (ip, port) 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect(addr)
    return client_socket
        

    # def solicitacao(self, solicit):
    #     print(solicit)
    #     self.client_socket.connect(self.addr)
    #     self.client_socket.send(solicit.encode()) #envia a mensagem
    #     print("Mensagem enviada.")
    #     print(self.client_socket.recv(2048).decode()) #)
    
    # def close(self): 
    #     self.client_socket.close()