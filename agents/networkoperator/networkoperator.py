from agents import Agent


class NetworkOperator(Agent):
    def __init__(self):
        super().__init__()
        self.description = "NetworkOperator agent - responsible for performing operations over the network, such as connecting to servers, sending/receiving data, etc"
        self.name = "Network Operator"
        self.model = "Llama-3.2-90b-Text-Preview"
        self.version = "0.1"
        self.author = "Andrew Cranston"
        self.start()
