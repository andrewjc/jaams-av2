from typing import List

from tools import AgentTool


class ToolProcessor:
    def __init__(self):
        self.__tools: List[AgentTool] = []
        self.last_tool_result = None

    def add_tool(self, tool: AgentTool):
        self.__tools.append(tool)

    def get_tools(self):
        return self.__tools

    def process(self, response: str) -> bool:
        for tool in self.__tools:
            if tool.match(response):
                tool_result = tool.execute(response)
                if tool_result:
                    self.set_last_tool_result(tool_result)
                    return True
        return False

    def __call__(self, response: str) -> bool:
        return self.process(response)

    def get_last_tool_result(self):
        return self.last_tool_result

    def set_last_tool_result(self, tool_result):
        self.last_tool_result = tool_result