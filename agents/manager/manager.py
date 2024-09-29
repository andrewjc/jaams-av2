from agents.agent import Agent
from tools import AgentEvaluator
from tools import AgentTaskAssigner


class Manager(Agent):
    def __init__(self):
        super().__init__()
        self.description = "Manager agent - responsible for managing other agents, delegating tasks, monitoring and reporting"
        self.name = "Manager"
        self.model = "Llama-3.2-90b-Text-Preview"
        self.version = "0.1"
        self.author = "Andrew Cranston"

        # Add tools to this agent
        self.add_tool(AgentEvaluator())
        self.add_tool(AgentTaskAssigner())

        self.start()
