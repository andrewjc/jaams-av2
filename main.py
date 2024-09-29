# AV2 - Agent V2
# github.com/andrewjc/jaams-av2
# Just Another Agent Management System
# Andrew Cranston
import json
import logging as log
import time
from typing import List
from colorama import Fore, Style, init

from agents import Agent
from agents import Manager
from agents import Planner
from agents import Analyzer
from agents import CodeWriter
from agents import FileSystemOperator
from agents import NetworkOperator
from agents import SystemOperator

# Initialize colorama
init(autoreset=True)
start_time = time.time()

class CustomFormatter(log.Formatter):
    format = "[%(levelname)-6s] " + Style.RESET_ALL + " " + Fore.WHITE + "%(message)s" + Style.RESET_ALL
    FORMATS = {
        log.DEBUG: Fore.BLUE + format + Style.RESET_ALL,
        log.INFO: Fore.GREEN + format + Style.RESET_ALL,
        log.WARNING: Fore.YELLOW + format + Style.RESET_ALL,
        log.ERROR: Fore.RED + format + Style.RESET_ALL,
        log.CRITICAL: Fore.RED + Style.BRIGHT + format + Style.RESET_ALL
    }

    def format(self, record):
        # Calculate the elapsed time in ticks
        record.ticks = int((time.time() - start_time) * 1000)
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = log.Formatter(log_fmt)
        return formatter.format(record)

class AgentStore:
    def __init__(self):
        self.agents: List[Agent] = []

        self.add_agent(Manager())
        self.add_agent(Planner())
        self.add_agent(Analyzer())
        self.add_agent(CodeWriter())
        self.add_agent(FileSystemOperator())
        self.add_agent(NetworkOperator())
        self.add_agent(SystemOperator())

        self.persist()


    def add_agent(self, agent: Agent):
        self.agents.append(agent)

    def load_agents(self, agent_file):
        pass

    def persist(self):
        # Save agents to file

        # for each agent in agents
        for agent in self.agents:

            # get the agent specification as json
            agent_spec = agent.get_specification()

            # write the json to file
            with open(f'agents/save_state/{agent.get_name()}.json', 'w') as f:
                f.write(agent_spec)

    def find(self, agent_name):
        for agent in self.agents:
            if agent.get_name() == agent_name:
                return agent
        return None


class TaskInputType:
    pass


class TaskOutputType:
    pass


class UserTask:
    def __init__(self, task_file):
        self.task_source = None
        self.inputs: List[TaskInputType] = []
        self.outputs: List[TaskOutputType] = []
        self.parse_task_file(task_file)

    def parse_task_file(self, task_file):
        # open the task_file and parse json to objects
        with open(task_file) as f:
            self.task_source = json.load(f)

        # santity check
        assert self.task_source is not None
        assert self.task_source['version'] == '1.0.0'
        assert self.task_source['name'] == 'task'
        assert self.task_source['description'] == "JAAMS Task Definition File"
        assert len(self.task_source['inputs']) > 0
        assert len(self.task_source['outputs']) > 0
        self.inputs = self.task_source['inputs']
        self.outputs = self.task_source['outputs']


class TaskRunner:
    def __init__(self, agent_store: AgentStore):
        self.active_user_task = None
        self.agent_store = agent_store

    def run(self, task_file):
        self.active_user_task = UserTask(task_file)

        # give the task to the manager
        manager = self.agent_store.find('Manager')
        manager.add_task(self.active_user_task)


def bootstrap():
    logger = log.getLogger()
    logger.setLevel(log.DEBUG)
    handler = log.StreamHandler()
    handler.setFormatter(CustomFormatter())
    logger.addHandler(handler)


    logger.info('AV2 - Agent V2')
    logger.info('github.com/andrewjc/jaams-av2')
    logger.info('Just Another Agent Management System')
    logger.info("Initializing...")

    agent_store = AgentStore()
    agent_store.load_agents('agents.json')

    task_runner = TaskRunner(agent_store)
    task_runner.run('task.json')

    logger.info("Running...")


if __name__ == '__main__':
    bootstrap()