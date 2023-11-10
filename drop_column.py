import sqlite3
import os

# удаляем колонку, проверяем путь
if os.path.exists('database.db'):
    conn = sqlite3.connect('database.db')
    conn.execute('ALTER TABLE projects DROP COLUMN games_for_relax')
    conn.commit()
    conn.close()
    print("удаление games_for_relax")
else:
    print("Не найдено")