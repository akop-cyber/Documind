import pymupdf4llm


class Loader:
    """
    loads the text from the pdf files
    """
    def __init__(self,file_path):
        self.file = file_path

    def load(self):
        pymupdf4llm.use_layout(False)
        text = pymupdf4llm.to_markdown(self.file)

        return text
