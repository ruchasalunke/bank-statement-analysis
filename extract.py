import PyPDF2
pdf = PyPDF2.PdfReader('hdfc-bank.pdf')
def extract_text(pdf):
    str = ""
    length = len(pdf.pages)
    for i in range(0,length):
        str += pdf.pages[i].extract_text().lower()
    #extracting text in a file called extract.txt
    with open("extract.txt","w",encoding='utf-8') as f:
        f.write(str)  
    return str        
         
def classify_bank(text):
    hdfc = ['hdfc bank']
    yes = ['yesb','yes']
    for keyword in hdfc:
        if keyword in text:
            return 'HDFC Bank'
        
    for keyword in yes:
        if keyword in text:
            return 'YES Bank' 

def get_ifsc(text):
    ifsc = text.find('ifsc')
    new_text = text[ifsc+7:ifsc+18]
    return new_text

def get_acc_no(text):
    no = text.find('account no')
    new_text = text[no+11:no+25]
    return new_text

def get_name(text):
    title = ['mr','mrs','ms','miss','dr']
    for i in title:
        if i in text:
            name = text.find(i)
            new_text = text[name:name+20]
            return new_text
    
def main():
    text = extract_text(pdf)
    bank = classify_bank(text)
    ifsc = get_ifsc(text)
    acc_no = get_acc_no(text)
    name = get_name(text)
    print(f'Bank           : {bank}')
    print(f'IFSC           : {ifsc}')
    print(f'Account number {acc_no}')
    print(f'Name           : {name}')

if __name__ == "__main__":
    main()