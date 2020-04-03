import mysql.connector
import time


def _menu():
    print("Escolha uma opção:\n\n 1)Cadastrar\n 2)Listar cadastros\n 3)Buscar\n 4)Alterar\n 5)Excluir\n")


def cadastro():
    db_connection = mysql.connector.connect(host='localhost', user='lucas', password='147987', database='pythonbd')
    time.sleep(1)
    print("\nConexão com o banco realizada...\n")

    nID    = int(input("Codigo: "))
    nNome  = str(input("Nome:"))
    nIdade = int(input("Idade: "))
    nCpf   = str(input("CPF: "))
    nNasc  = str(input("Data de nascimento: "))


    cursor = db_connection.cursor()
    sql = "INSERT INTO cliente (id, nome, idade, cpf, dt_nasc) VALUES (%s, %s, %s, %s, %s)"
    values = (nID, nNome, nIdade, nCpf, nNasc)
    cursor.execute(sql, values)

    time.sleep(1)
    print('Dados inseridos, encerrando conexão...\n\n')
    time.sleep(2)

    cursor.close()
    db_connection.commit()
    db_connection.close()

    print('Conexão encerrada!\n\n\n')

    time.sleep(5)


def main():
    print("\n")

    while True:
        _menu()
        opcao = int(input('Opção: '))
        if opcao == 1:
            cadastro()
        else:
            print('Opção ainda não disponível')

main()