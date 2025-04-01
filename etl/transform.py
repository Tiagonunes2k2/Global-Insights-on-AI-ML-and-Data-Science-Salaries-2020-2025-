import pandas as pd

# 🔍 🇺🇸 Reading the CSV file | 🇧🇷 Lendo o arquivo CSV
# 🇺🇸 Specify the full path to the file in a secure manner (avoid hardcoding the path in production).
# 🇧🇷 Especifique o caminho completo do arquivo de forma segura (evite codificar o caminho no código de produção).
df = pd.read_csv(r"C:\Users\GAMERX\Documents\Projeto_01\salaries.csv", encoding="utf-8")

# 🔄 🇺🇸 Converting "salary_in_usd" column to float, removing commas if present
# 🔄 🇧🇷 Convertendo a coluna "salary_in_usd" para float, removendo vírgulas se houver
df["salary_in_usd"] = df["salary_in_usd"].astype(str).str.replace(",", "").astype(float)

# 💰 🇺🇸 Creating a new column "monthly_salary" by dividing the annual salary by 12
# 💰 🇧🇷 Criando uma nova coluna "monthly_salary" dividindo o salário anual por 12
df["monthly_salary"] = (df["salary_in_usd"] / 12).round(2)  # 🔹 🇺🇸 Rounding to 2 decimal places | 🇧🇷 Arredondando para 2 casas decimais

# 💾 🇺🇸 Saving the cleaned dataset to a new CSV file without extreme values
# 💾 🇧🇷 Salvando o conjunto de dados limpo em um novo arquivo CSV sem valores exagerados
df.to_csv("salaries_cleaned.csv", index=False, decimal=".")

# 📊 🇺🇸 Displaying the first 10 rows of "salary_in_usd" and "monthly_salary"
# 📊 🇧🇷 Exibindo as 10 primeiras linhas de "salary_in_usd" e "monthly_salary"
print(df[["salary_in_usd", "monthly_salary"]].head(10))

# 📋 🇺🇸 Displaying the first few rows of the dataset | 🇧🇷 Exibindo as primeiras linhas do conjunto de dados
print(df.head())

# ❓ 🇺🇸 Checking for missing values | 🇧🇷 Verificando valores ausentes
print(df.isnull().sum())

# ℹ️ 🇺🇸 Displaying dataset information | 🇧🇷 Exibindo informações do conjunto de dados
print(df.info())

# 📈 🇺🇸 Displaying statistical summary | 🇧🇷 Exibindo resumo estatístico
print(df.describe())

# 🔝 🇺🇸 Sorting by "salary_in_usd" in descending order and displaying the top 10
# 🔝 🇧🇷 Ordenando por "salary_in_usd" em ordem decrescente e exibindo os 10 primeiros
print(df[['salary_in_usd', 'experience_level', 'company_location']].sort_values(by="salary_in_usd", ascending=False).head(10))

# 🌍 🇺🇸 Counting occurrences of each "company_location"
# 🌍 🇧🇷 Contando ocorrências de cada "company_location"
print(df["company_location"].value_counts())

# 🔎 🇺🇸 Checking data types of salary columns | 🇧🇷 Verificando os tipos de dados das colunas de salário
print(df["salary_in_usd"].dtype)  # 🇺🇸 Should show float64 | 🇧🇷 Deve mostrar float64
print(df["monthly_salary"].dtype)  # 🇺🇸 Should show float64 | 🇧🇷 Deve mostrar float64

# 💾 🇺🇸 Saving the cleaned dataset again to ensure consistency
# 💾 🇧🇷 Salvando o conjunto de dados limpo novamente para garantir consistência
df.to_csv("salaries_cleaned.csv", index=False)
