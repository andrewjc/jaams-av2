import json

from tools import AgentTool


class AgentEvaluator(AgentTool):
    def __init__(self):
        super().__init__()
        self.name = "Agent Evaluator"
        self.description = "Use this tool to evaluate capabilities and purpose of other agents, and to determine the best agent for a given task"

    def get_instructions(self):
        return self.name + " - " + self.description + " - example: <tool name=\\\"Agent Evaluator\\\" argument1=\\\"all or agent-name\\\" />"

    def match(self, response: str) -> bool:
        return response.index("<tool name=\"Agent Evaluator\"") > -1

    def execute(self, response: str):
        # extract the tool line
        tool_line = response[response.index("<tool name=\"Agent Evaluator\""):response.index("/>")+2]

        # extract the arguments
        arguments = tool_line.split(" ")[1:]

        # extract the agent_id
        agent_id = None
        for argument in arguments:
            if "argument1" in argument:
                agent_id = argument.split("=")[1]
                break

        # strip the quotes
        agent_id = agent_id.replace("\"", "")

        # evaluate the agent
        evaluation_result = []

        if agent_id == "all":
            all_agents = self.get_agent().get_store().get_agents()
            for agent in all_agents:
                evaluation_result.append(agent.description)
        else:
            # evaluate the specific agent
            pass

        return json.dumps(evaluation_result)

