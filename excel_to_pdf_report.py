import pandas as pd
from fpdf import FPDF


file_path = "D:/python/New folder/text.xlsx"
data = pd.read_excel(file_path, engine='openpyxl', header=1)


print("Original Data:")
print(data.head()) 
print("Columns:", data.columns)    


data_cleaned = data.loc[:, ~data.columns.str.contains('^Unnamed')].dropna(how='all')


data_cleaned.columns = data_cleaned.columns.str.strip()


print("Cleaned Data:")
print(data_cleaned.head())
print("Cleaned Columns:", data_cleaned.columns)


if 'id' in data_cleaned.columns:  
    if data_cleaned['id'].dtype == 'float64':  
        data_cleaned['id'] = data_cleaned['id'].astype(int)
else:
    print("Column 'id' not found in the DataFrame.")


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Data from Excel', 0, 1, 'C')  

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        for row in body:
            
            print('Row:', row) 
            self.cell(0, 10, ' '.join(map(str, row)), 0, 1)
        self.ln()


pdf = PDF()
pdf.add_page()


if not data_cleaned.empty: 
    pdf.chapter_title('Data from Excel')
    pdf.chapter_body(data_cleaned.values)
else:
    print("No data available to export to PDF.")


pdf_file_path = "D:/python/New folder/output.pdf"
pdf.output(pdf_file_path)

print(f"Data exported to PDF at {pdf_file_path}")
