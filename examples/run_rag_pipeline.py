from ai_agents.llm.factory import create_llm_client
from ai_agents.rag.pipeline import RAGPipeline


if __name__ == "__main__":
    llm = create_llm_client(provider="local", model_name="local-echo-v1")
    rag = RAGPipeline(llm=llm)
    rag.index_texts(
        {
            "doc-architecture": "RAG has ingestion, chunking, embedding, retrieval, and generation steps.",
            "doc-agents": "Multi-agent orchestration can route tasks to specialized agents.",
            "doc-eval": "Evaluation should track groundedness, latency, and answer quality.",
        }
    )
    print(rag.answer("What are the core steps of a RAG system?"))
