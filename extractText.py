import re
from pdfminer.high_level import extract_pages, extract_text

text = extract_text("./merged.pdf")

with open("./output/text.txt", "w") as f:
    print(text, file=f)