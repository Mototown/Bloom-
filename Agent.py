from dotenv import load_dotenv
from.generator import BloomGenerator

load_dotenv()

class BloomAgent:
    def __init__(self):
        self.generator = BloomGenerator()

    def run(self, business_question: str, record):
        print(f"[Bloom] Generating for: {business_question}")
        return self.generator.generate_model(business_question, record)
