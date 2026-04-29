import sys
from PyPDF2 import PdfReader

try:
    reader = PdfReader('assets/the-digital-amr-hashim-DPIZ8VHu.pdf')
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n--- PAGE BREAK ---\n"
    print(text)
except Exception as e:
    print("Error:", e)
