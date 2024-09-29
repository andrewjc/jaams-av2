from tools import AgentTool


class AgentTaskAssigner(AgentTool):
    def __init__(self):
        super().__init__()
        self.name = "Agent Task Assigner"
        self.description = "Use this tool to assign tasks to other agents, based on their capabilities and purpose"

    def get_instructions(self):
        return self.name + " - " + self.description + " - example: <tool name=\\\"Agent Task Assigner\\\" agent_id=\\\"agent_name\\\" task_description=\\\"json payload representing the task to be completed by the agent\\\" context=\\\"ongoing context for persisting key-value pairs\\\" />"
