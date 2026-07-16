from ai_agents.agents.base_agent import BaseAgent
from ai_agents.agents.code_review_agent import CodeReviewAgent
from ai_agents.agents.research_agent import ResearchAgent
from ai_agents.agents.tool_calling_agent import ToolCallingAgent


class MultiAgentOrchestrator:
    def __init__(
        self,
        base_agent: BaseAgent,
        research_agent: ResearchAgent,
        code_review_agent: CodeReviewAgent,
        tool_calling_agent: ToolCallingAgent,
    ) -> None:
        self.base_agent = base_agent
        self.research_agent = research_agent
        self.code_review_agent = code_review_agent
        self.tool_calling_agent = tool_calling_agent

    def route(self, task: str):
        lowered = task.lower()
        if "review" in lowered and "code" in lowered:
            return self.code_review_agent
        if "research" in lowered or "latest" in lowered:
            return self.research_agent
        if any(word in lowered for word in ["search", "run code", "remember:"]):
            return self.tool_calling_agent
        return self.base_agent

    def run(self, task: str) -> str:
        agent = self.route(task)
        return f"[{agent.name}]\n" + agent.run(task)
