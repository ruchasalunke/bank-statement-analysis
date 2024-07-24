import PyPDF2
pdf_one = PyPDF2.PdfReader('hdfc-bank.pdf')
pdf_two = PyPDF2.PdfReader('yes-bank.pdf')
def extract_text():
    str1 = ""
    str2 = ""
    length_one = len(pdf_one.pages)
    length_two = len(pdf_two.pages)
    for i in range(1,length_one):
        str1 += pdf_one.pages[i].extract_text().lower()
    for i in range(1,length_two):
        str2 += pdf_two.pages[i].extract_text().lower()
    #extracting text in a file called output.txt
    with open("output-1.txt","w",encoding='utf-8') as f1:
        f1.write(str1)
    with open("output-2.txt","w",encoding='utf-8') as f2:
        f2.write(str2)           
extract_text()