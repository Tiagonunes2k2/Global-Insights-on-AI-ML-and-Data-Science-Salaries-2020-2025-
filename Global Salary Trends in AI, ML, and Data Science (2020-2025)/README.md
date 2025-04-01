# Data Analysis Project

This project aims to build a complete data analysis pipeline, from extraction to final visualization. Using Python for ETL, SQL for queries, and Power BI for interactive dashboards, the project focuses on automating and optimizing processes to transform raw data into valuable insights.

## Objectives
- **ETL**: Extract data from various sources, transform it according to the analysis needs, and load it into a database.
- **SQL**: Query and manipulate the data for analysis and visualization.
- **Power BI**: Create interactive visualizations and dashboards to aid decision-making.

## Technologies Used
- **Python**: supabase, numpy, pandas, and psycopg2.
- **SQL**: MySQL, PostgreSQL
- **Power BI**

## Project Structure
- **/data**: Raw, processed, and ready-to-visualize files.
- **/etl**: ETL scripts.
- **/sql**: SQL queries.
- **/powerbi**: Visualization files.
- **/notebooks**: Exploratory analysis.
- **/docs**: Detailed documentation.
- **requirements.txt**: Project dependencies.

## How to Run
1. Clone this repository.
2. Install the Python dependencies with `pip install -r requirements.txt`.
3. Set up the database and create the tables using the `sql/create_tables.sql` script.
4. Run the ETL scripts to load and process the data:
   - `etl/extract.py`
   - `etl/transform.py`
   - `etl/load.py`
5. Open the `.pbix` file in Power BI to visualize the information.

## Contributions
Submit a pull request with your contributions. For more information, refer to the [documentation](docs/index.md).

## License
This project is licensed under the MIT License.

## Data Sources

The data used in this project was extracted from Kaggle. Below are the dataset details:

- **Dataset Name**: [The AI, ML, Data Science Salary (2020-2025)](https://www.kaggle.com/datasets/samithsachidanandan/the-global-ai-ml-data-science-salary-for-2025/data)
- **Author**: [Samith Chimminiyan](https://www.kaggle.com)
- **Kaggle Link**: [Access Dataset on Kaggle](https://www.kaggle.com/datasets/samithsachidanandan/the-global-ai-ml-data-science-salary-for-2025/data)
- **Description**: This dataset contains information about global salaries for AI, ML, and Data Science professionals from 2020 to 2025.

I thank the dataset author for making it available to the community and allowing me to use it in this project.

------------------------------------------------------------------------------------------------------------------------------------

# Projeto de Análise de Dados

Este projeto visa construir um pipeline completo de análise de dados, desde a extração até a visualização final. Utilizando Python para ETL, SQL para consultas e Power BI para dashboards interativos, o projeto foca na automação e otimização de processos para transformar dados brutos em insights valiosos.

## Objetivos
- **ETL**: Extrair dados de diversas fontes, transformá-los conforme as necessidades de análise e carregá-los em um banco de dados.
- **SQL**: Consultar e manipular os dados para análise e visualização.
- **Power BI**: Criar visualizações interativas e dashboards para facilitar a tomada de decisões.

## Tecnologias Utilizadas
- **Python**: supabase, numpy, pandas e psycopg2.
- **SQL**: MySQL, PostgreSQL
- **Power BI**

## Estrutura do Projeto
- **/data**: Arquivos brutos, tratados e prontos para visualização.
- **/etl**: Scripts de ETL.
- **/sql**: Consultas SQL.
- **/powerbi**: Arquivos de visualização.
- **/docs**: Documentação detalhada.
- **requirements.txt**: Dependências do projeto.

## Como Executar
1. Clone este repositório.
2. Instale as dependências do Python com `pip install -r requirements.txt`.
3. Configure o banco de dados e crie as tabelas com o script `sql/create_tables.sql`.
4. Execute os scripts de ETL para carregar e processar os dados:
   - `etl/extract.py`
   - `etl/transform.py`
   - `etl/load.py`
5. Abra o arquivo `.pbix` no Power BI para visualizar as informações.

## Contribuições
Envie um pull request com suas contribuições. Para mais informações, consulte a [documentação](docs/index.md).

## Licença
Este projeto está licenciado sob a Licença MIT.

## Fontes de Dados

Os dados utilizados neste projeto foram extraídos do Kaggle. Abaixo estão os detalhes do dataset:

- **Nome do Dataset**: [The AI, ML, Data Science Salary (2020-2025)](https://www.kaggle.com/datasets/samithsachidanandan/the-global-ai-ml-data-science-salary-for-2025/data)
- **Autor**: [Samith Chimminiyan](https://www.kaggle.com)
- **Link para o Kaggle**: [Acessar Dataset no Kaggle](https://www.kaggle.com/datasets/samithsachidanandan/the-global-ai-ml-data-science-salary-for-2025/data)
- **Descrição**: Este dataset contém informações sobre os salários globais de profissionais de IA, ML e Ciência de Dados entre 2020 e 2025.

Agradeço ao autor do dataset por disponibilizá-lo para a comunidade e permitir que eu o utilize neste projeto.
