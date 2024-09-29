import logging

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
        manager.set_task(self.active_user_task)

    def step(self):
        # for each agent in the agent store
        for agent in self.agent_store.agents:
            # if the agent has a task
            if agent.get_task():
                # execute the task
                task_status = agent.execute_task()

                if task_status == 'complete':
                    # remove the task
                    agent.remove_task()


                # persist the agent
                self.agent_store.persist()
                # return
                return

        # if no agents have tasks
        # check the active user task
        if self.active_user_task:
            # if the active user task is not complete
            if not self.active_user_task.is_complete():
                logging.error('Task is not complete')
                exit(-1)
            else:
                # set the active user task to None
                self.active_user_task = None
                # persist the agent store
                self.agent_store.persist()
        # if no agents have tasks and the active user task is None
        # do nothing
        return
