import fitz


class Loader:
    """
    loads the text from the pdf files
    """
    def __init__(self,file_path):
        self.file = file_path

    def load(self):
        text_chunks = []
    
    
        doc = fitz.open(pdf_path)
    
        for page in doc:
        
            page_text = page.get_text("text")
        
        
            page_text = "\n".join([line.strip() for line in page_text.split("\n") if line.strip()])
        
            text_chunks.append(page_text)
        
        doc.close()
        return "\n\n".join(text_chunks)

        return text
