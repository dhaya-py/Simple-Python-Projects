import pandas as pd


file1 = "D:/python/New_folder/eng_data.xlsx"
file2 = "D:/python/New folder/data.xlsx"


df1 = pd.read_excel(file1, sheet_name='Sheet1') 
df2 = pd.read_excel(file2, sheet_name='Sheet1')


diff = pd.concat([df1, df2]).drop_duplicates(keep=False)


print(diff)


diff.to_excel("differences.xlsx", index=False)
