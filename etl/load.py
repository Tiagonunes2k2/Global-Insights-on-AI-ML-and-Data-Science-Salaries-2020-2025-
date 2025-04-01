import os
from supabase import create_client, Client
import pandas as pd

# 🔧 🇺🇸 Supabase Configuration (Defines the URL and access key for the Supabase database)
# 🇧🇷 Configuração do Supabase (Define a URL e a chave de acesso ao banco de dados Supabase)

# Carregar as variáveis de ambiente para obter valores sensíveis de maneira segura
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# 🇺🇸 Creating the Supabase client to interact with the database
# 🇧🇷 Criando o cliente Supabase para interagir com o banco de dados
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# 🔍 🇺🇸 Reading the CSV file and loading data into a pandas DataFrame
# 🔍 🇧🇷 Lendo o arquivo CSV e carregando os dados em um DataFrame do pandas
df = pd.read_csv("salaries_cleaned.csv")

# 🔄 🇺🇸 Converting DataFrame data to a dictionary in list of records format
# 🔄 🇧🇷 Convertendo os dados do DataFrame para um dicionário no formato de lista de registros
dados = df.to_dict(orient="records")

try:
    # 🇺🇸 Inserting data into the "ai_ml_data_science_salary" table in Supabase
    # 🇧🇷 Inserindo os dados na tabela "ai_ml_data_science_salary" do Supabase
    response = supabase.table("ai_ml_data_science_salary").insert(dados).execute()
    print("🇺🇸 Data inserted successfully! | 🇧🇷 Dados inseridos com sucesso!")  # Success message if data is inserted correctly
except Exception as e:
    # 🇺🇸 Capturing and displaying any errors that occur during data insertion
    # 🇧🇷 Capturando e exibindo qualquer erro que ocorra durante a inserção dos dados
    print("🇺🇸 Error inserting data: | 🇧🇷 Erro ao inserir:", e)
