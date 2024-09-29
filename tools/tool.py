from abc import abstractmethod, ABC


class AgentTool(ABC):
    def __init__(self):
        self.name = None
        self.description = None

    @abstractmethod
    def get_instructions(self):
        pass
