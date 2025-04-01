# Data Analysis Project Documentation

## Overview
This data analysis project aims to develop a complete ETL (Extract, Transform, Load) solution, data analysis, and visualization. Through an end-to-end pipeline, the data processing steps will be demonstrated using Python, SQL, and Power BI. The ultimate goal is to present detailed information about salaries in different technology fields, focusing on analyses such as average salaries, yearly trends, and experience-based salary distributions over time.

## Project Structure
The project is divided into the following sections:

- **/data**: Contains raw, processed, and ready-to-visualize files.
- **/etl**: Scripts for data extraction, transformation, and loading.
- **/sql**: SQL queries for data modeling and manipulation.
- **/powerbi**: Power BI visualization files.
- **/docs**: Detailed project documentation.
- **README.md**: General project description.

## Technologies Used
- **Python**: Used for the ETL process, including libraries like `pandas`, `numpy`, `psycopg2`, and `supabase`.
- **SQL**: Queries and data modeling in the database.
- **Power BI**: Tool for creating dashboards and interactive visualizations.

## Project Requirements
- Python 3.x
- Python dependencies (specified in the `requirements.txt`)
- Power BI Desktop
- SQL Database (MySQL, PostgreSQL, or other)

## Running the Project
1. Clone the repository to your local machine.
2. Install the dependencies listed in the `requirements.txt`.
3. Set up the database following the instructions in the `sql/create_tables.sql` file.
4. Run the ETL scripts in the following order:
   - `etl/extract.py`: Extracts data from the PostgreSQL database.
   - `etl/transform.py`: Performs data transformations, such as value conversions and new column creation.
   - `etl/load.py`: Loads the processed data into Supabase.
5. Open the `.pbix` file in Power BI to view the dashboards.

## Script Explanations

### **`extract.py`**:
This script is responsible for extracting data from the PostgreSQL database. It connects to the database using credentials defined in environment variables and executes an SQL query to retrieve the data. In this case, the query fetches all data from the `ai_ml_data_science_salary` table. The script then prints the results to the console.

### **`transform.py`**:
The transformation script cleans and prepares the data for analysis. It starts by loading data from a CSV file, converts the `salary_in_usd` column to numeric format, and creates a new column `monthly_salary` by dividing the annual salary by 12. After transformation, the file is saved as `salaries_cleaned.csv`, ready to be loaded into a database or visualization.

### **`load.py`**:
This script is responsible for loading the transformed data into the Supabase database. The `salaries_cleaned.csv` file is read, and the data is converted to a suitable format before being inserted into the `ai_ml_data_science_salary` table in Supabase.

## Power BI Visualization
The Power BI visualization focuses on presenting salary information across different experience levels and company locations. The analysis is divided into three main metrics:
- **Average Salary by Job Title**: Shows the average salaries by various technology roles.
- **Average Salary by Year**: Displays the yearly salary progression.
- **Percentage by Experience**: Shows salary distribution based on experience levels over the years.

These insights are crucial for understanding salary trends in the job market and can be used for strategic decisions in human resources or career planning.

## Contributing
If you would like to contribute to this project, fork this repository, create a branch for your feature or bug fix, and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Data Sources

The data used in this project was sourced from Kaggle. Below are the dataset details:

- **Dataset Name**: [The AI, ML, Data Science Salary (2020-2025)](https://www.kaggle.com/datasets/samithsachidanandan/the-global-ai-ml-data-science-salary-for-2025/data)
- **Author**: [Samith Chimminiyan](https://www.kaggle.com)
- **Kaggle Dataset Link**: [Access Dataset on Kaggle](https://www.kaggle.com/datasets/samithsachidanandan/the-global-ai-ml-data-science-salary-for-2025/data)
- **Description**: This dataset contains information on global salaries for AI, ML, and Data Science professionals between 2020 and 2025.

Thanks to the author of the dataset for making it available to the community and allowing me to use it in this project.