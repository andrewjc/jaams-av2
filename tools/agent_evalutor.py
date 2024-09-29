from tools import AgentTool


class AgentEvaluator(AgentTool):
    def __init__(self):
        super().__init__()
        self.name = "Agent Evaluator"
        self.description = "Use this tool to evaluate capabilities and purpose of other agents, and to determine the best agent for a given task"

    def get_instructions(self):
        return self.name + " - " + self.description
