from ai_agents.llm.base import LLMClient, LLMRequest


class BaseAgent:
    def __init__(self, llm: LLMClient, name: str = "base-agent") -> None:
        self.llm = llm
        self.name = name

    def run(self, task: str) -> str:
        prompt = f"Task: {task}\nReturn a practical response."
        return self.llm.generate(
            LLMRequest(prompt=prompt, system="You are a general purpose AI assistant.")
        )
