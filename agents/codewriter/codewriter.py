from agents import Agent


class CodeWriter(Agent):
    def __init__(self):
        super().__init__()
        self.description = "CodeWriter agent - responsible for generating code, scripts, configuration files, etc. based on the given task."
        self.name = "Code Writer"
        self.model = "Llama-3.2-90b-Text-Preview"
        self.version = "0.1"
        self.author = "Andrew Cranston"
        self.start()
