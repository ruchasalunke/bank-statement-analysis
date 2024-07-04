from PIL import Image
import pytesseract
import pdf2image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
pdf_file = 'Account Statement.pdf'
# Convert PDF to list of images (one image per page)
images = pdf2image.convert_from_path(pdf_file)
# Initialize empty text variable to store extracted text
extracted_text = ''
# Loop through each page/image and extract text
for img in images:
    text = pytesseract.image_to_string(img, lang='eng')  # You can specify language if needed
    extracted_text += text + '\n'  # Append extracted text with a newline between pages
print(extracted_text)