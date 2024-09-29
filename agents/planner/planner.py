from agents.agent import Agent


class Planner(Agent):
    def __init__(self):
        super().__init__()
        self.description = "Planner agent - responsible for breaking down the given task, prioritizing and planning the task execution for other agents."
        self.name = "Planner"
        self.model = "Llama-3.2-90b-Text-Preview"
        self.version = "0.1"
        self.author = "Andrew Cranston"
        self.start()
