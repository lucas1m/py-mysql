# py-mysql
Contribuindo com códigos de estudos em integração com Python+Mysql Workbench 8.0 !

Primeiro código desenvolvido, simples, mas com muito aprendizado :D

Realiza a conexão com o banco de dados, passando os parâmetros necessários. Atualmente utilizo XAMP servers para usar um serviço 
MySql ativo e realizo uma conexão gráfica com o Mysql Workbench 8.0.
Partindo dessa premissa, é possível realizar diversos testes em bases controladas dentro do seu próprio servidor MySQL !

HOW TO ? 

Bom, tendo em vista que já possui o Python instalado em sua máquina, para realizar uma conexão ao Mysql, primeiramente você precisa
utilizar um conector nativo do MySql. 

Abra o CMD como administrador e cole o seguinte comando (sem as aspas) -> "pip install mysql-connector-python"
Utilize um editor de sua preferência e go to code! 

Preferencialmente, utilizo o VsCode com a extensão para Py -> ms-python.python

Feito isso, dentro de seu code, utilize a sintaxe:
import mysql.connector #importa a biblioteca responsável pela conexão

caso nenhuma alteração tenha sido feita no banco de dados, ou conexão XAMP, a sintaxe a seguir é exatamente essa, apenas 
passando o banco criado :)

db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='SEU_BANCO_CRIADO_NO_MYSQL') #realiza sua conexão :) !

Pronto! Você acaba de criar uma instância entre Python e MySQL.

Upei um código exemplo simples, mas que ajuda muito a iniciar os estudos na área! Divirta-se. 


Lets go study guys ;D

