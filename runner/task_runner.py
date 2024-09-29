from runner.agentstore import AgentStore
from runner.usertask import UserTask


class TaskRunner:
    def __init__(self, agent_store: AgentStore):
        self.active_user_task = None
        self.agent_store = agent_store

    def run(self, task_file):
        self.active_user_task = UserTask(task_file)

        # give the task to the manager
        manager = self.agent_store.find('Manager')
        manager.add_task(self.active_user_task)
