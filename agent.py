from.generator import BloomGenerator
class BloomAgent:
    def __init__(self):
        self.generator = BloomGenerator()
    def run(self, business_question: str, record):
        return self.generator.generate_model(business_question, record)
