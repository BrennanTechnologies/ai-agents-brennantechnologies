from ai_agents.agents.base_agent import BaseAgent
from ai_agents.tools.code_executor import CodeExecutor
from ai_agents.tools.memory_store import MemoryStore
from ai_agents.tools.web_search import WebSearchTool


class ToolCallingAgent(BaseAgent):
    def __init__(
        self,
        llm,
        web_search: WebSearchTool | None = None,
        code_executor: CodeExecutor | None = None,
        memory_store: MemoryStore | None = None,
        name: str = "tool-calling-agent",
    ) -> None:
        super().__init__(llm=llm, name=name)
        self.web_search = web_search or WebSearchTool()
        self.code_executor = code_executor or CodeExecutor()
        self.memory_store = memory_store or MemoryStore()

    def run(self, task: str) -> str:
        lowered = task.lower()
        if lowered.startswith("remember:"):
            payload = task.split(":", 1)[1].strip()
            self.memory_store.put("last_note", payload)
            return f"Stored memory: {payload}"

        if "search" in lowered or "research" in lowered:
            query = task.replace("search", "").replace("research", "").strip() or task
            results = self.web_search.search(query)
            return "\n".join(f"- {r['title']}: {r['url']}" for r in results)

        if "run code" in lowered:
            code = task.split("run code", 1)[1].strip()
            result = self.code_executor.run_python(code)
            return str(result)

        last_note = self.memory_store.get("last_note", "<none>")
        response = super().run(task)
        return f"{response}\n\nMemory[last_note]={last_note}"
