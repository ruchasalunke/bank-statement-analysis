from PIL import Image
import pytesseract
import pdf2image  # Install using pip install pdf2image

# Path to your PDF file
pdf_file = 'path_to_your_pdf.pdf'

# Convert PDF to list of images (one image per page)
images = pdf2image.convert_from_path(pdf_file)

# Initialize empty text variable to store extracted text
extracted_text = ''

# Loop through each page/image and extract text
for img in images:
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img, lang='eng')  # You can specify language if needed
    extracted_text += text + '\n'  # Append extracted text with a newline between pages

# Print or save the extracted text as needed
print(extracted_text)