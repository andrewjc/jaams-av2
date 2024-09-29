# AV2 - Agent V2
# github.com/andrewjc/jaams-av2
# Just Another Agent Management System
# Andrew Cranston

import logging as log
from typing import List

from agents import Agent
from agents import Manager
from agents import Planner
from agents import Analyzer
from agents import CodeWriter
from agents import FileSystemOperator
from agents import NetworkOperator
from agents import SystemOperator


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
            print(agent)

            # get the agent specification as json

            agent_spec = agent.get_specification()
            print(agent_spec)

            # write the json to file
            with open(f'agents/save_state/{agent.get_name()}.json', 'w') as f:
                f.write(agent_spec)


class TaskRunner:
    def run(self, task_file):
        pass


def bootstrap():
    logger = log.getLogger()
    logger.setLevel(log.DEBUG)
    logger.addHandler(log.StreamHandler())
    logger.info('AV2 - Agent V2')
    logger.info('github.com/andrewjc/jaams-av2')
    logger.info('Just Another Agent Management System')
    logger.info("Initializing...")

    agent_store = AgentStore()
    agent_store.load_agents('agents.json')

    task_runner = TaskRunner()
    task_runner.run('task.json')

    logger.info("Running...")


if __name__ == '__main__':
    bootstrap()