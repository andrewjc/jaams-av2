from tools import AgentTool


class AgentTaskAssigner(AgentTool):
    def __init__(self):
        super().__init__()
        self.name = "Agent Task Assigner"
        self.description = "Use this tool to assign tasks to other agents, based on their capabilities and purpose"

    def get_instructions(self):
        return self.name + " - " + self.description
