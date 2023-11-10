import pandas as pd

file = 'example.xlsx'
# Загружаем в объект pandas
xl = pd.ExcelFile(file)
# Печатаем название листов в данном файле
print(xl.sheet_names)
# Загрузить лист в DataFrame
df1 = xl.parse('data')
print(df1)