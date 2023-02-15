import mysql.connector as mysql
import datetime


class Database():
    """
        Classe que encapsula a conexão a um banco de dados e fornece métodos para executar operações no banco.

        Attributes
        ----------
        conexao : mysql.connector
        cursor : mysql.connector.cursor.MySQLCursor

        Methods
        -------
        cadastrar(self, usuario, numero, senha, nome, cpf, saldo = 0.0, limite = 1000.0)
            Cadastra um novo cliente na base de dados do banco.

        get_saldo(self, numero)
            Consulta o saldo e o limite de um usuário no banco de dados usando o número do usuário como parâmetro.

        set_saldo(self, numero, valor, flag = True)
            Atualiza o saldo de um cliente no banco de dados usando o número do cliente e um valor como parâmetros.

        enterAccount(self, usuario)
            Busca nome, saldo, numero de um cliente no banco de dados com base em seu nome de usuário.

        verificarUsuario(usuario, senha=None, UserPassword=True) 
            Verifica se um usuário existe no banco de dados.
        
        verificaSenha(senha, numero)
            Verifica se uma senha corresponde a um número de cliente no banco de dados.
        
        verificarCPF(cpf) 
            Verifica se um CPF existe no banco de dados.

        verificarNumero(numero) 
            Verifica se um número de cliente existe no banco de dados.

        get_historico(numero) 
            Retorna o histórico de transações para um número de cliente.

        set_historico(numero, his) 
            Atualiza o histórico de transações para um número de cliente.
    """

    
    def __init__(self, senha):
        """
            Construtor da classe que inicializa uma conexão com um banco de dados MySQL e cria um objeto cursor para executar consultas SQL.

            parameters
            ----------
            senha: str
                Senha para ter acesso ao banco de dados MySQL.
        """
        self.conexao = mysql.connect(host='localhost', db='conta', user='root', password=senha, autocommit=True)
        self.cursor = self.conexao.cursor()  #mysql.connector
    
    def cadastrar(self, usuario, numero, senha, nome, cpf, saldo = 0.0, limite = 1000.0):
        """
            Cadastra um novo cliente na base de dados do banco.

            parameters
            ----------
            usuario: str 
                O nome de usuário do cliente.
            numero: int 
                O número de conta do cliente.
            senha: str 
                A senha do cliente.
            nome: str 
                O nome do cliente.
            cpf: str 
                O CPF do cliente.
            saldo: float 
                O saldo inicial da conta do cliente (opcional, padrão = 0.0).
            limite: float 
                O limite de crédito da conta do cliente (opcional, padrão = 1000.0).

            returns
                None
        """ 
        # Obtém a data atual
        data = datetime.datetime.today().strftime("%d/%m/%y %H:%M")
        # Cria a query de inserção de dados na tabela "cliente"
        query = f'INSERT INTO cliente(cpf, nome, usuario, senha, numero, saldo, limite, historico) VALUES ("{cpf}", "{nome}", "{usuario}", "{senha}", {numero}, {saldo}, {limite}, "Data de de abertura: {data}\n\n")'
        # Executa a query no cursor da conexão com a base de dados
        self.cursor.execute(query)

    def get_saldo(self, numero):
        """
            Consulta o saldo e o limite de um usuário no banco de dados usando o número do usuário como parâmetro.

            parameters
            ----------
            numero: int
                Número da conta do usuário.

            returns
            -------
            Suecesso: Retorna uma string com o saldo e o limite do cliente formatados como duas casas decimais 
            separados por vírgula, por exemplo: "1000.00, 2000.00".
            Falha: Retorna False.
        """
    
        self.cursor.execute(f'select saldo, limite from cliente where numero = {numero}')
        flag = self.cursor.fetchall()
        valores = f'{flag[0][0]:.2f}, {flag[0][1]:.2f}'
        if flag:
            return valores
        else:
            return False
    
    def set_saldo(self, numero, valor, flag = True):
        """
            Atualiza o saldo de um cliente no banco de dados usando o número do cliente e um valor como parâmetros.

            parameters
            ----------
            numero: int 
                Número da conta do usuário.
            valor: float 
                Valor a ser adicionado ou subtraído do saldo do cliente. Se o parâmetro flag for True, o valor será adicionado ao saldo atual. Se o parâmetro flag for False, o valor será subtraído do saldo atual.
            flag: bool
                Se True (padrão), o valor será adicionado ao saldo atual. Se False, o valor será subtraído do saldo atual.
            
            returns
            -------
            Retorna None
        """
        saldo = self.get_saldo(numero).split(',')
        if flag: 
            valor += float(saldo[0])
        else:
            valor -= float(saldo[0])
        self.cursor.execute(f'update cliente set saldo = {valor} where numero = {numero}')
    
    def enterAccount(self, usuario):
        """
        Busca nome, saldo, numero de um cliente no banco de dados com base em seu nome de usuário.

        parameters
        ----------
        usuario: str
            Nome de usuário da conta.

        returns
        -------
        Retorna uma tupla com dois elementos. O primeiro elemento é True (indicando que a busca foi bem sucedida). 
        O segundo elemento é uma string com o nome do cliente, seu saldo e seu número de conta, separados por vírgulas
        e com duas casas decimais no saldo.

    """
        self.cursor.execute(f'select nome, saldo, numero from cliente where usuario = "{usuario}"')
        resul = self.cursor.fetchall()
        resul = f'{resul[0][0]}, {resul[0][1]}, {resul[0][2]}' 
        return True, resul
    
    def verificarUsuario(self, usuario, senha = None, UserPassword = True):
        """
            Verifica se um usuário existe no banco de dados de clientes.
            
            parameters
            ----------
            usuario: str 
                nome de usuário a ser verificado.
            senha: str 
                senha do usuário a ser verificada (opcional).
            UserPassword: bool 
                indica se a verificação inclui senha (padrão True).
            
            returns
            -------
            Sucesso: Retorna True se o usuário existe e a senha está correta e uma string.
            Falha: Retorna False e uma string.
        """
        if UserPassword:
            # verifica se o usuário existe no banco de dados (incluindo senha)
            self.cursor.execute(f'SELECT usuario FROM cliente WHERE usuario = "{usuario}"')
            exists = self.cursor.fetchall()
            if exists:
                return True    
            return False
        else:
            # verifica se o usuário existe no banco de dados (sem verificar senha)
            self.cursor.execute(f'SELECT usuario, senha FROM cliente WHERE usuario = "{usuario}" and senha = "{senha}"')
            exists = self.cursor.fetchall()
            if exists:
                return True, 'Exite.'
            return False, 'Usuário ou senha não encontrado.'
    
    def verificaSenha(self, senha, numero):
        """
            Verifica se a senha e o número de cliente correspondem aos registros no banco de dados.

            parameters
            ----------
            senha: str
                A senha a ser verificada.
            numero int
                O número de cliente a ser verificado.

            returns
            -------
            Sucesso: True.
            Falha: False.
        """
        self.cursor.execute(f'select senha, numero from cliente where senha = "{senha}" and numero = {numero}')
        flag = self.cursor.fetchall()
        if flag:
            return True
        return False

    def verificarCPF(self, cpf):
        """
            Verifica se o CPF está registrado no banco de dados de clientes.

            parameters
            ----------
            cpf: str
                O CPF a ser verificado.

            returns
            -------
            Sucesso: True.
            Falha: False.
        """
        self.cursor.execute(f'SELECT cpf FROM cliente WHERE cpf = "{cpf}"')
        exists = self.cursor.fetchall()
        if exists:
            return True
        else:
            return False
        
    def verificarNumero(self, numero):
        """
            Verifica se o número de cliente está registrado no banco de dados.

            parameters
            ----------
            numero: int
                O número de cliente a ser verificado.

            returns
            -------
            Sucesso: True.
            Falha: False.
        """
        self.cursor.execute(f'SELECT numero FROM cliente WHERE numero = "{numero}"')
        exists = self.cursor.fetchall()
        if exists:
            return True
        else:
            return False

    def get_historico(self, numero):
        """
            Retorna o histórico de transações para o número de cliente fornecido.

            parameters
            ----------
            numero: int
                O número de cliente cujo histórico de transações será retornado.

            returns
            -------
                Retorna uma string que contém o histórico de transações do número de cliente fornecido.
        """
        self.cursor.execute(f'select historico from cliente where numero = {numero}')
        flag = self.cursor.fetchone()
        return flag

    def set_historico(self, numero, his):
        """
            Atualiza o histórico de transações para o número de cliente fornecido.

            parameters
            ----------
            numero: int 
                O número de cliente cujo histórico de transações será atualizado.
            his: str 
                A transação a ser adicionada ao histórico de transações do número de cliente.

            returns
            -------
            Nenhum.
        """
        flag = self.get_historico(numero)
        flag = flag[0]
        if len(flag) >= 500:
            flag = flag[0:35:]
        his = flag + '\n' + his
        self.cursor.execute(f'update cliente set historico = "{his}" where numero = {numero}')