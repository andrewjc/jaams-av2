import json
import re

from runner.usertask import UserTask
from tools import AgentTool


class AgentTaskAssigner(AgentTool):
    def __init__(self):
        super().__init__()
        self.name = "Agent Task Assigner"
        self.description = "Use this tool to assign tasks to other agents, based on their capabilities and purpose"

    def get_instructions(self):
        return self.name + " - " + self.description + " - example: <tool name=\\\"Agent Task Assigner\\\" agent_id=\\\"agent_name\\\" task_description=\\\"{\\\"name\\\": \\\"task\\\", \\\"version\\\": \\\"1.0.0\\\", \\\"description\\\": \\\"JAAMS Task Definition File\\\", \\\"inputs\\\": [{\\\"type\\\": \\\"text\\\", \\\"description\\\": \\\"full details of the task that the agent will complete. be sure to include any and all information required to complete the task, as agents are stateless.\\\"}], \\\"outputs\\\": [{\\\"asset\\\": {\\\"type\\\": \\\"[text|files]\\\", \\\"description\\\": \\\"description of the output required by the agent. if the type is text, then the output is pure text and this should describe WHAT the agent should output as a result from the task. if the type is files, then the output should be the full path where the agent should save files\\\"}}, {\\\"asset\\\": {\\\"type\\\": \\\"[text|files]\\\", \\\"description\\\": \\\"the description for an optional second (or third) asset. agent's can output multiple assets.\\\"}}]}\\\" context=\\\"key-value pairs where agent can store information, eg lang=java;mode=web;parent-task=develop-twitter;author=andrew\\\" />"

    def match(self, response: str) -> bool:
        return "<tool name=\"Agent Task Assigner\"" in response

    def execute(self, response: str):
        # extract the tool line
        tool_line = re.search(r'<tool name="Agent Task Assigner".*?/>', response).group(0)

        # extract the arguments using regex
        agent_id = re.search(r'agent_id="([^"]+)"', tool_line).group(1)

        if 'agent' in agent_id.lower():
            agent_id = agent_id.replace('agent', '')

        agent_id = agent_id.strip()

        task_description = re.search(r'task_description="((?:[^"\\]|\\.)*)"', tool_line).group(1)
        context = re.search(r'context="([^"]+)"', tool_line).group(1)

        # parse the task_description JSON
        task_description = task_description.replace('\\"', '"')
        #task_description = json.loads(task_description)

        # assign the task to the agent
        all_agents = self.get_agent().get_store().get_agents()
        for agent in all_agents:
            if agent.name.lower() == agent_id.lower():
                agent.set_task(UserTask.from_json(task_description))
                return json.dumps({"status": "task assigned", "agent_id": agent_id})

        return json.dumps({"status": "fail", "agent_id": -1})
