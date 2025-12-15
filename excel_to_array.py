import pandas as pd

file_path = "D:/python/New folder/text.xlsx"


data = pd.read_excel(file_path, engine='openpyxl', header=1)


data_cleaned = data.dropna(how='all')


array_data = data_cleaned.values


print(array_data)
