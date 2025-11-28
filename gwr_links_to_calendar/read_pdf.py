import pypdfium2 as pdfium

def read_pdf(path_to_pdf: str):
    with open(path_to_pdf, "rb") as f:
        pdf = pdfium.PdfDocument(f.read())

        # Create & fill object storing extracted text
        extracted_text = [""]*len(pdf)
        for i in range(len(pdf)):
            extracted_text[i] = pdf.get_page(i).get_textpage().get_text_range()
        
        return extracted_text