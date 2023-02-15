import socket
from banco import *
import threading
from netifaces import interfaces, ifaddresses, AF_INET
from database.senha import senha

class ClienteThread(threading.Thread):
    """
        Instancia um Thread para que a execução simultânea do banco
        aplicações seja possível.

        Attributes
        ---------
        clientSock : socket.socket
            Soquete de conexão para enviar e receber solicitações.
        clientAddress : str
            Endereço IP de conexão

        Methods
        -------
        run()
            inicializar a thread
    """

    def __init__(self, clientSock, clientAddress):
        """
            Construtor da classe ClienteThread.

            parameters
            ----------
            clientSock: socket.socket
                Soquete de conexão para enviar e receber solicitações.
            clientAddress : str
                Endereço IP de conexão.
        """
        threading.Thread.__init__(self)
        self.clientSock = clientSock
        self.clientAddress = clientAddress

    def run(self):
        """
            Inicia a execução da thread.

            A thread espera por solicitações do cliente e as processa de acordo com o método fornecido. 
            O método é chamado dinamicamente, usando reflexão. 
            O cliente é desconectado quando o método 'sair' é chamado. 

            parameters
            Nenhum.

            retorns:
            Nenhum.
        """
        try:
            while True:
                solicitaco = self.clientSock.recv(2048).decode().split("*") 
                # Buscando o método da requisição no banco
                if solicitaco:
                    metodo = solicitaco.pop(0)
                    if metodo == 'sair':
                        self.clientSock.close()
                        break
                    banco = Banco(senha)
                    func = getattr(banco, metodo)
                    # executando o método e passando todos os parametros que foram recebidos na requisição
                    retorno = func(*solicitaco)
                    self.clientSock.send(f'{retorno}'.encode('utf-8')) 
        except AttributeError:
            print('Algo deu errado')

class Servidor():

    """
        A Classe servidor espera por conexões e quando elas são feitas,
        os envia para a threads.

        Attributes
        ----------
        host : str
            localhost para fazer conexões.
        port : str
            Porta de acesso para fazer conexões
        server : socket.socket
            Soquete de conexão para enviar e receber solicitações.

        Methods
        -------
        start(self)
            Executa o servidor para que ele aguarde as conexões.

    """
    
    def __init__(self, host):
        """
            Construtor da classe Servidor.

            parameters
            ----------
            host : str
                localhost para fazer conexões.
        """
        self.host = host 
        self.port = 8005
        addr = (self.host, self.port)
        self.serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
        self.serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #reinicia o socket
        self.serv_socket.bind(addr) #define as portas e quais ips podem se conectar com o servidor
        self.serv_socket.listen(10) #define o limite de conexões

        
    def start(self):
        """
            Aguarda a conexão de um cliente, cria uma nova thread para lidar com suas solicitações e inicia essa thread.

            parameters
                Nenhum.

            retorna:
                Nenhum.
        """
        while True:
            print("aguardando conexão...\n\n")
            client_sock, client_address = self.serv_socket.accept() 
            print(f'Cliente {client_address[0]} conectado.\n\n')
            print("aguardando solicitação...\n\n")

            novaThread = ClienteThread(client_sock, client_address)

            print("Thread inciada\n\n")
            novaThread.start()

def obterIp():
    """
        Esta função tem como objetivo obter o endereço IP da máquina em que o código está sendo executado.

        parameters
            Nenhum.
        retorns:
            Retorna uma lista de strings contendo o endereço IP associado às interfaces de rede disponíveis no sistema.
    """
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )] # pega o ip da maquina
    return addresses
    
if __name__ == '__main__':
    ip = obterIp()
    print(f'Ip do servidor: {ip[0]}\n\n')
    c = Servidor(ip[0])
    c.start()