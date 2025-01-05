import pdfplumber
import csv
with pdfplumber.open("E:/bank-statement-analysis/hdfc-bank.pdf") as pdf:
    for page_num, page in enumerate(pdf.pages):
        table = page.extract_table()
        if table:
            with open("E:/bank-statement-analysis/hdfc-bank.csv", mode='a', newline="") as file:
                writer = csv.writer(file)
                for row in table:
                    writer.writerow(row)