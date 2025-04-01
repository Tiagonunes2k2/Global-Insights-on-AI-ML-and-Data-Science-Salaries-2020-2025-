# Documentação do Projeto de Análise de Dados

## Visão Geral
Este projeto de análise de dados busca desenvolver uma solução completa de ETL (Extração, Transformação e Carga), análise e visualização de dados. Através de um pipeline de ponta a ponta, serão demonstradas as etapas de processamento de dados utilizando Python, SQL e Power BI. O objetivo final é apresentar informações detalhadas sobre salários em diferentes áreas de tecnologia, com foco em análises como médias salariais, evolução por ano e porcentagens por experiência ao longo do tempo.

## Estrutura do Projeto
O projeto é dividido nas seguintes seções:

- **/data**: Contém os arquivos brutos, tratados e prontos para visualização.
- **/etl**: Scripts de extração, transformação e carga dos dados.
- **/sql**: Consultas SQL para modelagem e manipulação de dados.
- **/powerbi**: Arquivos de visualização no Power BI.
- **/docs**: Documentação detalhada do projeto.
- **README.md**: Descrição geral do projeto.

## Tecnologias Usadas
- **Python**: Utilizado para o processo de ETL, incluindo bibliotecas como `pandas`, `numpy`, `psycopg2` e `supabase`.
- **SQL**: Consultas e modelagem de dados no banco de dados.
- **Power BI**: Ferramenta para criação de dashboards e visualizações interativas.

## Requisitos do Projeto
- Python 3.x
- Dependências Python (especificadas no `requirements.txt`)
- Power BI Desktop
- Banco de Dados SQL (MySQL, PostgreSQL, ou outro)

## Como Rodar o Projeto
1. Clone o repositório para sua máquina local.
2. Instale as dependências listadas no `requirements.txt`.
3. Configure o banco de dados conforme as instruções no arquivo `sql/create_tables.sql`.
4. Execute os scripts de ETL na ordem:
   - `etl/extract.py`: Extrai dados do banco de dados PostgreSQL.
   - `etl/transform.py`: Realiza transformações nos dados, como conversão de valores e criação de novas colunas.
   - `etl/load.py`: Carrega os dados processados para o Supabase.
5. Abra o arquivo `.pbix` no Power BI para visualizar os dashboards.

## Explicação dos Scripts

### **`extract.py`**:
Este script é responsável pela extração dos dados do banco de dados PostgreSQL. Ele se conecta ao banco usando credenciais definidas em variáveis de ambiente e executa uma consulta SQL para obter os dados. A consulta neste caso recupera todos os dados da tabela `ai_ml_data_science_salary`. O script então imprime os resultados na tela.

### **`transform.py`**:
O script de transformação limpa e prepara os dados para análise. Ele começa carregando os dados de um arquivo CSV, converte a coluna `salary_in_usd` para formato numérico e cria uma nova coluna `monthly_salary` dividindo o salário anual por 12. Após a transformação, o arquivo é salvo como `salaries_cleaned.csv`, pronto para ser carregado em um banco de dados ou visualização.

### **`load.py`**:
Esse script é responsável por carregar os dados transformados para o banco de dados Supabase. O arquivo `salaries_cleaned.csv` é lido e os dados são convertidos para um formato adequado antes de serem inseridos na tabela `ai_ml_data_science_salary` no Supabase.

## Visualização no Power BI
A visualização no Power BI foca em apresentar informações sobre os salários em diferentes níveis de experiência e localizações de empresas. A análise está dividida em três principais métricas:
- **Média Salarial por Cargo**: Apresenta as médias salariais por diferentes cargos na área de tecnologia.
- **Média Salarial por Ano**: Exibe a evolução salarial anual.
- **Porcentagem por Experiência**: Mostra a distribuição de salários com base no nível de experiência ao longo dos anos.

Essas informações são cruciais para entender tendências salariais no mercado de trabalho e podem ser utilizadas para decisões estratégicas em recursos humanos ou planejamento de carreira.

## Contribuições
Se deseja contribuir para este projeto, faça um fork deste repositório, crie uma branch para sua feature ou correção e submeta um pull request.

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Fontes de Dados

Os dados utilizados neste projeto foram extraídos do Kaggle. Abaixo estão os detalhes do dataset:

- **Nome do Dataset**: [The AI, ML, Data Science Salary (2020-2025)](https://www.kaggle.com/datasets/samithsachidanandan/the-global-ai-ml-data-science-salary-for-2025/data)
- **Autor**: [Samith Chimminiyan](https://www.kaggle.com)
- **Link para o Kaggle**: [Acessar Dataset no Kaggle](https://www.kaggle.com/datasets/samithsachidanandan/the-global-ai-ml-data-science-salary-for-2025/data)
- **Descrição**: Este dataset contém informações sobre os salários globais de profissionais de IA, ML e Ciência de Dados entre 2020 e 2025.

Agradeço ao autor do dataset por disponibilizá-lo para a comunidade e permitir que eu o utilize neste projeto.