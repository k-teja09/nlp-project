from stanfordnlp.server import CoreNLPClient

class TextProcessor:
    def __init__(self):
        self.client = CoreNLPClient()

    def process_text(self, text):
        with self.client as client:
            ann = client.annotate(text)
            return ann

if __name__ == "__main__":
    text_processor = TextProcessor()
    result = text_processor.process_text("Your input text here.")
    print(result)
#     # You can access sentence splitting, tokenization, and POS tagging from the result.
