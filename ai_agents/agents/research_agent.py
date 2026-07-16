from ai_agents.agents.base_agent import BaseAgent
from ai_agents.llm.base import LLMRequest
from ai_agents.tools.web_search import WebSearchTool


class ResearchAgent(BaseAgent):
    def __init__(self, llm, web_search: WebSearchTool | None = None, name: str = "research-agent"):
        super().__init__(llm=llm, name=name)
        self.web_search = web_search or WebSearchTool()

    def run(self, task: str) -> str:
        results = self.web_search.search(task, max_results=5)
        compiled = "\n".join(
            f"- {r['title']} ({r['url']}): {r['snippet']}" for r in results
        )
        prompt = (
            "Create a concise research summary with key findings and references.\n"
            f"Topic: {task}\n\n"
            f"Search Results:\n{compiled}"
        )
        return self.llm.generate(LLMRequest(prompt=prompt, system="You are a research analyst."))
