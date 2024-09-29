from agents.agent import Agent


class Analyzer(Agent):
    def __init__(self):
        super().__init__()
        self.description = "Analyzer agent - responsible for analyzing the given task, generating requirements, constraints and specifications."
        self.name = "Analyzer"
        self.model = "Llama-3.2-90b-Text-Preview"
        self.version = "0.1"
        self.author = "Andrew Cranston"
        self.start()
