from ai_agents.llm.base import LLMClient, LLMRequest
from ai_agents.rag.document_processor import DocumentProcessor
from ai_agents.rag.retriever import Retriever
from ai_agents.rag.vector_store import InMemoryVectorStore


class RAGPipeline:
    def __init__(self, llm: LLMClient, processor: DocumentProcessor | None = None) -> None:
        self.llm = llm
        self.processor = processor or DocumentProcessor()
        self.store = InMemoryVectorStore()
        self.retriever = Retriever(self.store)

    def index_texts(self, docs: dict[str, str]) -> None:
        for doc_id, text in docs.items():
            for chunk in self.processor.process_text(doc_id, text):
                chunk_id = f"{chunk.doc_id}-{len(self.store.all_items())}"
                self.store.add(chunk_id, chunk.text)

    def answer(self, question: str, top_k: int = 3) -> str:
        hits = self.retriever.retrieve(question, top_k=top_k)
        context = "\n".join(f"[{h['id']}] {h['text']}" for h in hits)
        prompt = (
            "Use the retrieved context to answer the question.\n"
            f"Context:\n{context}\n\n"
            f"Question: {question}\n"
            "Answer succinctly and cite chunk ids when relevant."
        )
        return self.llm.generate(LLMRequest(prompt=prompt, system="You are a RAG assistant."))
