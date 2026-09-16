import pdfplumber


def extract_text_from_pdf(file_path):
    """
    Extract text from a PDF CV.
    """

    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception as error:
        print("PDF reading error:", error)
        return ""

    return text.strip()