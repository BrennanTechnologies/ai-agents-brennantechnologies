from ai_agents.agents.base_agent import BaseAgent
from ai_agents.llm.base import LLMRequest


class CodeReviewAgent(BaseAgent):
    def run(self, code: str) -> str:
        prompt = (
            "Review this code for bugs, edge cases, maintainability, and test gaps. "
            "Return findings ordered by severity with actionable suggestions.\n\n"
            f"Code:\n{code}"
        )
        return self.llm.generate(LLMRequest(prompt=prompt, system="You are a senior code reviewer."))
