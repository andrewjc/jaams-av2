from abc import abstractmethod, ABC

class AgentTool(ABC):
    def __init__(self):
        self.name = None
        self.description = None
        self.__agent = None

    @abstractmethod
    def get_instructions(self):
        pass

    @abstractmethod
    def match(self, response: str) -> bool:
        pass

    @abstractmethod
    def execute(self, response: str):
        pass

    def get_agent(self):
        return self.__agent

    def set_agent(self, owner_agent):
        self.__agent = owner_agent
