import os
from abc import ABC

from backend.agent_backend import AgentBackend
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

class GroqBackend(AgentBackend, ABC):
    def __init__(self):
        super().__init__()

    def execute_task(self, model, task_prompt):
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": task_prompt,
                }
            ],
            model=model,
        )
        print(chat_completion.choices[0].message.content)