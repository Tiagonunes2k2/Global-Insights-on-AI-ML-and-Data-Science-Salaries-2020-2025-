-- Arquivo: create_tables.sql
-- Criando uma tabela exemplo para armazenar os dados do dataset
CREATE TABLE ai_ml_data_science_salary (
    id SERIAL PRIMARY KEY,
    work_year INT,
    experience_level VARCHAR(10),
    employment_type VARCHAR(10),
    job_title VARCHAR(255),
    salary INT,
    salary_currency VARCHAR(10),
    salary_in_usd INT,
    employee_residence VARCHAR(10),
    remote_ratio INT,
    company_location VARCHAR(10),
    company_size VARCHAR(10)
);

