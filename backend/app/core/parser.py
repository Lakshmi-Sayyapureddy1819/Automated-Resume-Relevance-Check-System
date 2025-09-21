import pdfplumber
from io import BytesIO

async def extract_text_from_pdf(file) -> str:
    # file is UploadFile, read bytes asynchronously
    contents = await file.read()
    with pdfplumber.open(BytesIO(contents)) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    return text
