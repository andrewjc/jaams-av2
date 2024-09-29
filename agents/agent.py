import json
import logging
from typing import List

from tools import AgentTool


def load_prompt(filename):
    logging.debug(f'Loading prompt: {filename}')
    with open(f'prompts/{filename}') as f:
        return json.load(f)


class Agent:
    def __init__(self):
        self.name = None
        self.task_queue = []
        self.status = "stopped"
        self.result = None
        self.__tools: List[AgentTool] = []

    def start(self):
        self.__assemble_system_prompt()

    def stop(self):
        pass

    def restart(self):
        pass

    def get_name(self):
        return self.name

    def status(self):
        pass

    def execute_task(self):
        pass

    def get_task_queue(self):
        pass

    def get_task(self):
        pass

    def add_task(self, task):
        pass

    def remove_task(self):
        pass

    def get_task_status(self):
        pass

    def get_task_result(self):
        pass

    def get_specification(self):
        # serialize the agent to json
        spec = {k: v for k, v in self.__dict__.items() if not k.startswith('_Agent__')}
        return json.dumps(spec)

    def add_tool(self, tool: AgentTool):
        self.__tools.append(tool)

    def __assemble_system_prompt(self):
        generic_prompt = load_prompt('generic.json')
        agent_prompt = load_prompt(f'{self.name.replace(' ', '').lower()}.json')
        tool_prompt = self.__assemble_tool_prompt()

        # merge the 'instructions' from the generic prompt with the agent prompt
        self.instructions = generic_prompt['instructions'] + agent_prompt['instructions'] + tool_prompt['instructions']
        self.responsibilities = agent_prompt['responsibilities']

    def __assemble_task_prompt(self):
        pass

    def __assemble_tool_prompt(self):
        return {
            'instructions':
                [
                    'Invoke a tool using <tool name="Tool Name" argument1="value" argument2="value" ... argumentn="value" />'
                    'You have the following tools available to complete the task:',
                ] + [tool.get_instructions() for tool in self.__tools]
        }
