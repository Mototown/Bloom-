from.generator import BloomGenerator
from.decision_record import DecisionRecord

class BloomAgent:
    def __init__(self):
        self.generator = BloomGenerator()

    def run(self, business_question: str, record: DecisionRecord):
        return self.generator.generate_model(business_question, record)
