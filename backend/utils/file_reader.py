import pandas as pd
from io import BytesIO
from docx import Document
from io import BytesIO
import pdfplumber
from io import BytesIO
# import filetype


# attachments_data = []

# for key, file in request.files.items():
#     raw_bytes = file.read()
#     kind = filetype.guess(raw_bytes)
#     mime = kind.mime if kind else "unknown"

#     attachments_data.append({
#         "filename": file.filename,
#         "mime_type": mime,
#         "size_bytes": len(raw_bytes),
#         "raw_bytes": raw_bytes,
#     })



def extract_pdf_text(raw_bytes):
    text = ""
    with pdfplumber.open(BytesIO(raw_bytes)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def extract_docx(raw_bytes):
    doc = Document(BytesIO(raw_bytes))
    return "\n".join([p.text for p in doc.paragraphs])

def extract_excel(raw_bytes):
    df = pd.read_excel(BytesIO(raw_bytes))
    return df.to_string()