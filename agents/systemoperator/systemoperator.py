from agents import Agent


class SystemOperator(Agent):
    def __init__(self):
        super().__init__()
        self.description = "SystemOperator agent - responsible for performing system operations, such as starting/stopping services, managing processes, etc."
        self.name = "System Operator"
        self.model = "Llama-3.2-90b-Text-Preview"
        self.version = "0.1"
        self.author = "Andrew Cranston"
        self.start()
