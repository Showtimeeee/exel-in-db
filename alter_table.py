import sqlite3
import pandas as pd

excel_data = pd.read_excel('example.xlsx', sheet_name='data')
# изменяем колонку
with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('ALTER TABLE projects ADD COLUMN games_for_relax TEXT')
    cursor.execute("UPDATE projects SET games_for_relax = 'sims'")
    print("Изменения данных выполнены")

