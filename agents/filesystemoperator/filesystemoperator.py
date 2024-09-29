from agents import Agent


class FileSystemOperator(Agent):
    def __init__(self):
        super().__init__()
        self.description = "FileSystemOperator agent - responsible for writing, reading, managing files, directories, permissions, etc."
        self.name = "File System Operator"
        self.model = "Llama-3.2-90b-Text-Preview"
        self.version = "0.1"
        self.author = "Andrew Cranston"
        self.start()
