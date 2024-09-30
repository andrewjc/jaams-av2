from tools import AgentTool


class AgentTaskAssigner(AgentTool):
    def __init__(self):
        super().__init__()
        self.name = "Agent Task Assigner"
        self.description = "Use this tool to assign tasks to other agents, based on their capabilities and purpose"

    def get_instructions(self):
        return self.name + " - " + self.description + " - example: <tool name=\\\"Agent Task Assigner\\\" agent_id=\\\"agent_name\\\" task_description=\\\"json payload representing the task to be completed by the agent\\\" context=\\\"ongoing context for persisting key-value pairs\\\" />"


    def match(self, response: str) -> bool:
        return response.index("<tool name=\"Agent Task Assigner\"") > -1

    def execute(self, response: str):
        # extract the tool line
        tool_line = response[response.index("<tool name=\"Agent Task Assigner\""):response.index("/>")+2]

        # extract the arguments
        arguments = tool_line.split(" ")[1:]

        # extract the agent_id
        agent_id = None
        for argument in arguments:
            if "agent_id" in argument:
                agent_id = argument.split("=")[1]
                break

        # extract the task_description
        task_description = None
        for argument in arguments:
            if "task_description" in argument:
                task_description = argument.split("=")[1]
                break

        # extract the context
        context = None
        for argument in arguments:
            if "context" in argument:
                context = argument.split("=")[1]
                break

        # assign the task to the agent
        pass

        return True
