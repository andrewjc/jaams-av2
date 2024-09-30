import logging
import os
import pickle
import hashlib
from abc import ABC

from backend.agent_backend import AgentBackend
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

class GroqBackend(AgentBackend, ABC):
    def __init__(self, cache_dir='cache'):
        super().__init__()
        self.cache_dir = cache_dir
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def _generate_cache_key(self, model, task_prompt):
        key = f"{model}_{task_prompt}"
        return hashlib.md5(key.encode()).hexdigest()

    def _load_from_cache(self, cache_key):
        cache_path = os.path.join(self.cache_dir, cache_key)
        if os.path.exists(cache_path):
            with open(cache_path, 'rb') as cache_file:
                return pickle.load(cache_file)
        return None

    def _save_to_cache(self, cache_key, response):
        cache_path = os.path.join(self.cache_dir, cache_key)
        with open(cache_path, 'wb') as cache_file:
            pickle.dump(response, cache_file)

    def execute_task(self, model, task_prompt):
        cache_key = self._generate_cache_key(model, task_prompt)
        cached_response = self._load_from_cache(cache_key)
        if cached_response is not None:
            logging.debug(f"Groq cached response: {cached_response}")
            return cached_response

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": task_prompt,
                }
            ],
            model=model,
        )
        groq_response = chat_completion.choices[0].message.content
        logging.debug(f"Groq response: {groq_response}")

        self._save_to_cache(cache_key, groq_response)
        return groq_response