import json
from typing import List


class TaskInputType:
    def __init__(self, spec):
        self.input_type = spec['type']
        self.description = spec['description']

    def to_json(self):
        return {
            "type": self.input_type,
            "description": self.description
        }


class TaskOutputAsset:
    def __init__(self, spec):
        self.asset_type = spec['type']
        self.description = spec['description']


class TaskOutputType:
    def __init__(self, spec):
        self.asset = TaskOutputAsset(spec['asset'])

    def to_json(self):
        return {
            "asset": {
                "type": self.asset.asset_type,
                "description": self.asset.description
            }
        }


class UserTask:
    def __init__(self):
        self.task_source = None
        self.inputs: List[TaskInputType] = []
        self.outputs: List[TaskOutputType] = []

    @staticmethod
    def from_file(task_file):
        user_task = UserTask()
        user_task.parse_task_file(task_file)
        return user_task

    @staticmethod
    def from_json(json_string):
        user_task = UserTask()
        user_task.parse_task_json(json_string)
        return user_task

    def parse_task_file(self, task_file):
        with open(task_file) as f:
            self.task_source = json.load(f)
        self._parse_task_source()

    def parse_task_json(self, json_string):
        self.task_source = json.loads(json_string)
        self._parse_task_source()

    def _parse_task_source(self):
        assert self.task_source is not None
        assert self.task_source['version'] == '1.0.0'
        assert self.task_source['description'] == "JAAMS Task Definition File"
        assert len(self.task_source['inputs']) > 0
        assert len(self.task_source['outputs']) > 0
        self.inputs = [TaskInputType(src) for src in self.task_source['inputs']]
        self.outputs = [TaskOutputType(src) for src in self.task_source['outputs']]

    def to_json(self):
        struct = {
            "inputs": [inp.to_json() for inp in self.inputs],
            "outputs": [out.to_json() for out in self.outputs]
        }
        return json.dumps(struct)