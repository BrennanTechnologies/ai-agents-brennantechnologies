from ai_agents.rag.retriever import Retriever
from ai_agents.rag.vector_store import InMemoryVectorStore


class VectorMemory:
    def __init__(self) -> None:
        self.store = InMemoryVectorStore()
        self.retriever = Retriever(self.store)
        self._counter = 0

    def add(self, text: str) -> str:
        item_id = f"mem-{self._counter}"
        self._counter += 1
        self.store.add(item_id, text)
        return item_id

    def search(self, query: str, top_k: int = 3) -> list[dict[str, str | float]]:
        return self.retriever.retrieve(query, top_k=top_k)
