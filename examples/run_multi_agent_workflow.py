from ai_agents.agents.base_agent import BaseAgent
from ai_agents.agents.code_review_agent import CodeReviewAgent
from ai_agents.agents.orchestrator import MultiAgentOrchestrator
from ai_agents.agents.research_agent import ResearchAgent
from ai_agents.agents.tool_calling_agent import ToolCallingAgent
from ai_agents.llm.factory import create_llm_client
from ai_agents.rag.pipeline import RAGPipeline
from ai_agents.workflows.graph import build_default_workflow


if __name__ == "__main__":
    llm = create_llm_client(provider="local", model_name="local-echo-v1")

    orchestrator = MultiAgentOrchestrator(
        base_agent=BaseAgent(llm=llm, name="base-agent"),
        research_agent=ResearchAgent(llm=llm, name="research-agent"),
        code_review_agent=CodeReviewAgent(llm=llm, name="code-review-agent"),
        tool_calling_agent=ToolCallingAgent(llm=llm, name="tool-calling-agent"),
    )

    rag = RAGPipeline(llm=llm)
    rag.index_texts(
        {
            "design-doc": "Agent systems often use routing and memory to solve complex tasks.",
            "ops-doc": "A workflow graph can compose planning, tool use, and post-processing.",
        }
    )

    workflow = build_default_workflow(orchestrator=orchestrator, rag_pipeline=rag)
    state = workflow.run({"task": "Research modern RAG architectures using project knowledge."})
    print(state["final"])
