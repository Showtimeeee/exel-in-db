import pandas as pd
import sqlite3

# Загружаем в объект pandas
excel_data = pd.read_excel('example.xlsx', sheet_name='data')

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создание таблицы в базе данных, если её еще не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
        project_code INTEGER PRIMARY KEY,
        project_name TEXT NOT NULL,
        plan_date DATE,
        plan_value REAL,
        fact_date DATE,
        fact_value REAL
    )
''')

# Запись данных в таблицу
excel_data.to_sql('projects', conn, if_exists='replace', index=False)

conn.close()
print('create database.db')