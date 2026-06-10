import re
class Chunker:
    def __init__(self, chunk_size=250, overlap=40):
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.patterns =  r"\|.+\|.*?\n\| *[-:]+ *\|.*?\n(?:\|.+\|.*?\n?)*"

    def chunker(self, text):
        if self.overlap >= self.chunk_size:
            raise ValueError("Overlap must be smaller than chunk size.")
        
        clean_text = text

        chunks = []
        tables = []
        start = 0
        #text_size = len(text)
        matches = re.finditer(self.patterns,text)
        table_intervals = [(m.start(),m.end()) for m in matches]
        table_intervals.sort(reverse=True)

        for start_indx , end_indx in table_intervals:
            tab = text[start_indx:end_indx]
            if tab:
                clean_text = clean_text[:start_indx] + clean_text[end_indx:]
                tables.append(tab)
        text_size = len(clean_text)


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
            
        return chunks, tables
