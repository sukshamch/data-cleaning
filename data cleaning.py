import pandas as pd

file_path = "C:/Users/HPJMU/Documents/suksham011.xlsx"
df = pd.read_excel(file_path, names=['EMPLOYEES', 'SALARY', 'POSITION', 'EMP. ID', 'FIRST 4 CHAR', 'LAST 4 CHAR', 'MIDDLE 4 CHAR', 'Column1'])

print(df)

