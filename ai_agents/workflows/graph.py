from ai_agents.agents.orchestrator import MultiAgentOrchestrator
from ai_agents.rag.pipeline import RAGPipeline
from ai_agents.workflows.langgraph_style import WorkflowGraph


def build_default_workflow(
    orchestrator: MultiAgentOrchestrator,
    rag_pipeline: RAGPipeline,
) -> WorkflowGraph:
    graph = WorkflowGraph()

    def route_task(state):
        task = str(state.get("task", ""))
        state["agent_response"] = orchestrator.run(task)
        return state

    def enrich_with_rag(state):
        task = str(state.get("task", ""))
        if "knowledge" in task.lower() or "doc" in task.lower():
            state["rag_response"] = rag_pipeline.answer(task)
        else:
            state["rag_response"] = "RAG bypassed for this task"
        return state

    def compose_output(state):
        state["final"] = (
            f"Agent Output:\n{state.get('agent_response', '')}\n\n"
            f"RAG Output:\n{state.get('rag_response', '')}"
        )
        return state

    graph.add_node("route", route_task)
    graph.add_node("rag", enrich_with_rag)
    graph.add_node("compose", compose_output)

    graph.add_edge("route", "rag")
    graph.add_edge("rag", "compose")
    return graph
