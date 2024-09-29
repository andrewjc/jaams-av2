from typing import List

from agents import Agent, Manager, Planner, Analyzer, CodeWriter, FileSystemOperator, NetworkOperator, SystemOperator
from backend import AgentBackend

class AgentStore:
    def __init__(self, backend: AgentBackend):
        self.backend = backend
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
        agent.set_backend(self.backend)
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
            with open(f'agents/save_state/{agent.get_name().replace(' ', '').lower()}.json', 'w') as f:
                f.write(agent_spec)

    def find(self, agent_name):
        for agent in self.agents:
            if agent.get_name() == agent_name:
                return agent
        return None
