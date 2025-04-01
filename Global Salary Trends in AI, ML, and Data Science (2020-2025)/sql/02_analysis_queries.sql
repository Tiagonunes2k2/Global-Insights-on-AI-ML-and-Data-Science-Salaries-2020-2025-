-- Arquivo: queries.sql
-- Consultas SQL para análise dos dados

-- Selecionar todos os dados da tabela
SELECT * FROM ai_ml_data_science_salary;

-- Média salarial por nível de experiência
SELECT experience_level, AVG(salary_in_usd) AS avg_salary
FROM ai_ml_data_science_salary
GROUP BY experience_level
ORDER BY avg_salary DESC;

-- Contagem de empregos por título
SELECT job_title, COUNT(*) AS job_count
FROM ai_ml_data_science_salary
GROUP BY job_title
ORDER BY job_count DESC
LIMIT 10;