# from banco import *
# banco = Banco()
# teste = getattr(banco, 'get_saldo')
# print(teste)
# print(teste(688))
# valor = 3.3333
# print(f"{valor:.2f}")
# nome = "nome"
# cpf = "cpf"
# data_nascimento = "data_nascimento"
# senha = "senha"

# a = f'criar_conta*{nome}*{cpf}*{data_nascimento}*{senha}'
# print(a.split('*'))
# a = a.split('*')
# b = a.pop(0)
# print(b)

# lista = ['(True', " [('will'", ' 125.0', ' 592)])']
# (True, [('will', 125.0, 592)])
# c = str((True, [('will', 125.0, 592)]))
# d = c.replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace(",", "").replace("'", '').split()
# # e = d.split()
# d[0] = bool(d[0])
# print(d, type(d))

# def teste():
#     return False, 'a ta\nopa'

# def con(a):
#     b = ''
#     for i in range(1, len(a)):
#         b += a[i]
#     return b

# a = teste()
# print(a, type(a))

# a = con(a)
# print(a, type(a))
# import mysql.connector as mysql

# conexao = mysql.connect(host='localhost', db='conta', user='root', password='Tales of demons', autocommit=True)
# cursor = conexao.cursor()

# cursor.execute(f'select nome from cliente')
# resul = cursor.fetchall()
# print(resul)

# class b():
#     def __init__(self):
#         self.k = g()

# class g():

#     def c(self):
#         print('c')

# m = b()

# teste = getattr(m, 'c')

# print(teste)

import mysql.connector as mysql

conexao = mysql.connect(host='localhost', db='conta', user='root', password='Tales of demons', autocommit=True)
cursor = conexao.cursor()

query = 'SELECT historico FROM cliente WHERE usuario = "user2"'
cursor.execute(query)
a = cursor.fetchone()
b = a[0][0:35:]
print(b)