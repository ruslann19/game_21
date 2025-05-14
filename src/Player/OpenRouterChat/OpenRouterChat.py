from typing import Dict, List

import requests


class OpenRouterChat:
    def __init__(
        self,
        api_key: str,
        model: str = "meta-llama/llama-3-8b-instruct",
        system_prompt: str = None,
    ):
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        self.model = model
        self.messages: List[Dict] = []

        if system_prompt:
            self.messages.append({"role": "system", "content": system_prompt})

    def ask(self, user_message: str) -> str:
        self.messages.append({"role": "user", "content": user_message})

        data = {"model": self.model, "messages": self.messages, "temperature": 0.7}

        response = requests.post(self.api_url, json=data, headers=self.headers)
        assistant_reply = response.json()["choices"][0]["message"]["content"]

        self.messages.append({"role": "assistant", "content": assistant_reply})

        return assistant_reply
