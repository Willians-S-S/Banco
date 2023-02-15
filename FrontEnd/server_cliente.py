import socket 

def server_cliente(ip, port):
    '''
    A função server_cliente é responsável por criar e retornar um objeto de socket para o cliente
    se conectar a um servidor com o endereço IP e a porta especificados. 
    A função recebe dois parâmetros: ip e port, que são respectivamente o endereço IP e a porta do servidor. 
    O endereço é definido pela tupla (ip, port). É criado um objeto de socket client_socket com o tipo de endereço IPv4
    e o protocolo de transporte TCP. 
    Em seguida, o cliente se conecta ao endereço especificado com o método connect(). 
    Por fim, o objeto de socket é retornado.

    Parameters
        ----------
        ip: Str

        port: Str

        Returns
        -------
        client_socket
    '''
    ip = ip
    port = port
    addr = (ip, port) 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect(addr)
    return client_socket
