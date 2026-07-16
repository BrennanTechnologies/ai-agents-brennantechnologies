
# Module: agents-ai-brennantechnologies.py
# Author: Chris Brennan - chris@brennantechnologies.com
# Company: Brennan Technologies, LLC


from ai_agents.rag.vector_store import InMemoryVectorStore, tokenize


class Retriever:
    def __init__(self, store: InMemoryVectorStore) -> None:
        self.store = store

    def retrieve(self, query: str, top_k: int = 3) -> list[dict[str, str | float]]:
        query_vec = self._to_counter(query)
        scored = []
        for item in self.store.all_items():
            score = self.store.cosine_similarity(query_vec, item.vector)
            scored.append({"id": item.item_id, "text": item.text, "score": score})
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]

    @staticmethod
    def _to_counter(text: str):
        from collections import Counter

        return Counter(tokenize(text))
