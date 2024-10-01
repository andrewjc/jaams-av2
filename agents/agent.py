import json
import logging
from typing import List

from backend import AgentBackend
from backend import DEFAULT_AGENT_BACKEND
from runner.tool_processor import ToolProcessor
from runner.usertask import UserTask
from tools import AgentTool

def load_prompt(agent_name):
    with open(f'agents/{agent_name}/{agent_name}.json') as f:
        return json.load(f)

class Agent:
    def __init__(self):
        self.__backend: AgentBackend = DEFAULT_AGENT_BACKEND
        self.__tool_processor: ToolProcessor | None = ToolProcessor()
        self.__store = None

        self.model = None
        self.name = None
        self.active_task: UserTask | None = None
        self.status = "stopped"
        self.result = None

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
        # assemble the prompt and the task
        task_prompt = self.__assemble_task_prompt()

        response = None
        is_complete = False
        backend_input = task_prompt
        while not is_complete:
            response = self.__backend.execute_task(self.model, backend_input)
            if self.__tool_processor(response):
                backend_input = task_prompt + response + self.__tool_processor.get_last_tool_result()
            else:
                is_complete = True

        self.result = response
        return 'complete'

    def get_task_queue(self):
        pass

    def get_task(self):
        return self.active_task

    def set_task(self, task):
        self.active_task = task

    def remove_task(self):
        self.active_task = None

    def get_task_status(self):
        pass

    def get_task_result(self):
        pass

    def get_specification(self):
        # serialize the agent to json
        spec = {k: v for k, v in self.__dict__.items() if not k.startswith('_Agent__')}
        return json.dumps(spec)

    def add_tool(self, tool: AgentTool):
        tool.set_agent(self)
        self.__tool_processor.add_tool(tool)

    def __assemble_system_prompt(self):
        logging.debug(f'Loading prompt for {self.name.replace(' ', '').lower()} agent')
        generic_prompt = load_prompt('base')
        agent_prompt = load_prompt(f'{self.name.replace(' ', '').lower()}')
        tool_prompt = self.__assemble_tool_prompt()

        # merge the 'instructions' from the generic prompt with the agent prompt
        self.instructions = generic_prompt['instructions'] + agent_prompt['instructions'] + tool_prompt['instructions']
        self.responsibilities = agent_prompt['responsibilities']

    def __assemble_task_prompt(self):
        task_prompt = {
            'instructions': self.instructions,
            'task': [
                'The user task is as follows:',
                self.active_task.to_json(),
                'Delegate or complete the task using the tools available to you.'
            ]
        }

        return json.dumps(task_prompt)

    def __assemble_tool_prompt(self):
        return {
            'instructions':
                [
                    'Invoke a tool using <tool name="Tool Name" argument1="value" argument2="value" ... argumentn="value" />'
                    'You have the following tools available to complete the task:',
                ] + [tool.get_instructions() for tool in self.__tool_processor.get_tools()] + [
                    "You may only invoke one tool at a time.",
                    "After invoking a tool, you must wait for the result before invoking another tool."
                ]
        }

    def set_backend(self, backend: AgentBackend):
        self.__backend = backend

    def __getstate__(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_Agent__')}

    def get_store(self):
        return self.__store

    def set_store(self, agent_store):
        self.__store = agent_store

