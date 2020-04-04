import mysql.connector
import time


def _menu():
    print("\nEscolha uma opção:\n\n 1)Cadastrar\n 2)Buscar\n 3)Alterar\n 4)Excluir\n")


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

def pesquisar():
    db_connection = mysql.connector.connect(host='localhost', user='lucas', password='147987', database='pythonbd')
    time.sleep(1)
    print("\nConexão com o banco realizada...\n")

    pesqID = str(input('Digite o nome a pesquisar: '))
    time.sleep(2)
    print("\n")

    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM cliente WHERE nome like '"+pesqID+"_%' ")

    resultado = cursor.fetchone() 
    
    #metodo fetchall() busca todas as linhas da última instrução executada.
    #metodo fetchone() é semelhante, porem retorna os dados linha por linha

    for x in resultado:
        print(x)


    cursor.close()
    db_connection.commit()
    db_connection.close()

def altera():
    db_connection = mysql.connector.connect(host='localhost', user='lucas', password='147987', database='pythonbd')
    time.sleep(1)
    print("\nConexão com o banco realizada...\n\n")

    alterNOME = str(input('Qual registro será alterado?\nDigite o nome: '))

    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM cliente WHERE nome like '"+alterNOME+"_%' ")

    resultado = cursor.fetchone() 
    
    #metodo fetchall() busca todas as linhas da última instrução executada.
    #metodo fetchone() é semelhante, porem retorna os dados linha por linha

    for x in resultado:
        print(x)

    print("\nRegistro(s) encontrado(s)!\nDigite 1 para confirmar ou 2 para cancelar\n")
    escolha = int(input(': '))
    
    if escolha == 1:
        print("Ok! Digite o ID desejado\n")
        id_enc = str(input(': '))

        print(f'Ok! id {id_enc} selecionado\n Agora, o que deseja alterar?\nMENU\n')
        print('1)Nome\n2)Idade\n3)CPF\n4)Data de nascimento\n\n')
        
        escolha2 = int(input('Opcao selecionada: '))
        if escolha2 == 1:
            novo_nome = str(input('Digite o novo nome: '))
            cursor = db_connection.cursor()
            cursor.execute("Update cliente set nome = '"+novo_nome+"' where id = '"+id_enc+"_%' ")
            time.sleep(3)
            print("Cliente atualizado! Voltando ao menu!\n...")
            time.sleep(5)

            cursor.close()
            db_connection.commit()
            db_connection.close()
            
            main()

        elif escolha2 == 2:
            nova_idade = str(input('Digite a idade: '))
            cursor = db_connection.cursor()
            cursor.execute("Update cliente set idade = '"+nova_idade+"' where id = '"+id_enc+"_%' ")
            time.sleep(3)
            print("Cliente atualizado! Voltando ao menu!\n...")
            time.sleep(5)

            cursor.close()
            db_connection.commit()
            db_connection.close()
            
            main()
        else:
            print("Continue assim!")


def main():
    print("\n")

    while True:
        _menu()
        opcao = int(input('Opção: '))
        if opcao == 1:
            cadastro()
        elif opcao == 2:
            pesquisar()
        elif opcao == 3:
            altera()
        else:
            print('Opção ainda não disponível')

main()