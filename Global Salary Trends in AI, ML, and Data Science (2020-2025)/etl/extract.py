import psycopg2
import os  # 🇺🇸 For loading environment variables securely | 🇧🇷 Para carregar variáveis de ambiente de forma segura

# 🔐 🇺🇸 Database connection credentials using environment variables | 🇧🇷 Credenciais de conexão com o banco de dados usando variáveis de ambiente
user = os.getenv("DB_USER")  # 🇺🇸 Replace with your environment variable | 🇧🇷 Substitua pela sua variável de ambiente
password = os.getenv("DB_PASSWORD")  # 🇺🇸 Replace with your environment variable | 🇧🇷 Substitua pela sua variável de ambiente
host = os.getenv("DB_HOST")  # 🇺🇸 Replace with your environment variable | 🇧🇷 Substitua pela sua variável de ambiente
port = int(os.getenv("DB_PORT", 6543))  # 🇺🇸 Default to 6543 if not set | 🇧🇷 Padrão para 6543 se não configurado
database = os.getenv("DB_NAME")  # 🇺🇸 Replace with your environment variable | 🇧🇷 Substitua pela sua variável de ambiente

def execute_sql_query(query, host, database, user, password, port):
    """
    🇺🇸 Executes an SQL query on a PostgreSQL database.
    🇧🇷 Executa uma query SQL em um banco de dados PostgreSQL.
   
    Args:
        query (str): 🇺🇸 SQL code to be executed | 🇧🇷 Código SQL a ser executado
        host (str): 🇺🇸 Database server address | 🇧🇷 Endereço do servidor do banco de dados
        database (str): 🇺🇸 Name of the database | 🇧🇷 Nome do banco de dados
        user (str): 🇺🇸 Username for authentication | 🇧🇷 Nome de usuário para autenticação
        password (str): 🇺🇸 Password for authentication | 🇧🇷 Senha para autenticação
        port (int): 🇺🇸 Database server port | 🇧🇷 Porta do servidor de banco de dados
       
    Returns:
        list or None: 🇺🇸 Query results if available, otherwise None
                      🇧🇷 Resultados da consulta, se houver, ou None
    """
    connection = None  # 🇺🇸 Initializing the 'connection' variable | 🇧🇷 Inicializando a variável 'connection'
    try:
        # 🔗 🇺🇸 Connecting to the PostgreSQL database | 🇧🇷 Conectando ao banco de dados PostgreSQL
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )

        # 🎯 🇺🇸 Opening a cursor to execute database operations | 🇧🇷 Abrindo um cursor para realizar operações no banco de dados
        cursor = connection.cursor()

        # 📝 🇺🇸 Executing the SQL query | 🇧🇷 Executando o código SQL
        cursor.execute(query)

        # 💾 🇺🇸 Committing changes | 🇧🇷 Confirmando as alterações
        connection.commit()

        # 🔍 🇺🇸 Checking if the query returns data (SELECT statement) | 🇧🇷 Verificando se a consulta retorna dados (comando SELECT)
        if cursor.description:  
            results = cursor.fetchall()  # 🇺🇸 Fetch all results | 🇧🇷 Buscar todos os resultados
            return results
        else:
            print(f"🇺🇸 Command executed. Rows affected: {cursor.rowcount} | 🇧🇷 Comando executado. Linhas afetadas: {cursor.rowcount}")

    except (Exception, psycopg2.Error) as error:
        # ⚠️ 🇺🇸 Handling errors | 🇧🇷 Tratamento de erros
        print("🇺🇸 Error connecting or executing SQL code: | 🇧🇷 Erro ao conectar ou executar o código SQL:", error)
   
    finally:
        # 🔒 🇺🇸 Closing the connection and cursor | 🇧🇷 Fechando a conexão e o cursor
        if connection is not None:
            cursor.close()
            connection.close()
            print("🇺🇸 PostgreSQL connection closed. | 🇧🇷 Conexão ao PostgreSQL fechada.")

# 🔍 🇺🇸 Defining the query to retrieve data from the "population_data" table
# 🔍 🇧🇷 Definindo a consulta para recuperar dados da tabela "population_data"
query = "SELECT * FROM ai_ml_data_science_salary"

# 🚀 🇺🇸 Executing the query and storing the result | 🇧🇷 Executando a consulta e armazenando o resultado
resultado = execute_sql_query(query, host, database, user, password, port)

# 📋 🇺🇸 Printing the results | 🇧🇷 Exibindo os resultados
print(resultado)
