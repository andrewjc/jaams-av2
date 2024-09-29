from abc import ABC, abstractmethod


class AgentBackend(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def execute_task(self, model, task_prompt):
        pass


class DummyAgentBackend(AgentBackend, ABC):
    def __init__(self):
        super().__init__()

    def execute_task(self, model, task_prompt):
        print(task_prompt)

DEFAULT_AGENT_BACKEND = DummyAgentBackend()
