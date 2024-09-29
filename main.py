# AV2 - Agent V2
# github.com/andrewjc/jaams-av2
# Just Another Agent Management System
# Andrew Cranston

import logging as log
import time
from colorama import init

from backend import GroqBackend

from runner.agentstore import AgentStore
from runner.task_runner import TaskRunner
from utils import CustomFormatter

# Initialize colorama
init(autoreset=True)

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

    backend = GroqBackend()

    agent_store = AgentStore(backend)
    agent_store.load_agents('agents.json')

    task_runner = TaskRunner(agent_store)
    task_runner.run('task.json')

    logger.info("Running...")
    while True:
        task_runner.step()


        time.sleep(1)


if __name__ == '__main__':
    bootstrap()