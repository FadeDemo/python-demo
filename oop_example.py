class DocumentProcessor:
    def __init__(self, text):
        self.text = text

    def clean_text(self):
        return self.text.lower()


doc = DocumentProcessor("This is a Test Document for RAG.")
cleaned = doc.clean_text()
print(cleaned)  # 输出: this is a test document for rag.
