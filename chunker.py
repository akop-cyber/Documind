class Chunker:
    def __init__(self, chunk_size=250, overlap=40):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunker(self, text):
        if self.overlap >= self.chunk_size:
            raise ValueError("Overlap must be smaller than chunk size.")

        chunks = []
        start = 0
        text_size = len(text)

        while start < text_size:
            end = start + self.chunk_size
            
            
            if end < text_size:
                last_space = text.rfind(' ', start, end)
                if last_space != -1:
                    end = last_space 
            

            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            
            
            start = end - self.overlap
            
        return chunks

        while start < text_size:
            end = start + self.chunk_size
            
            
            if end < text_size:
                last_space = clean_text.rfind(' ', start, end)
                if last_space != -1 and last_space > start:
                    end = last_space 
            

            chunk = clean_text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            
            
            start = end - self.overlap
            
        return chunks
