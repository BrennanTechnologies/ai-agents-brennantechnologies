from ai_agents.agents.research_agent import ResearchAgent
from ai_agents.llm.factory import create_llm_client
from ai_agents.tools.web_search import WebSearchTool


if __name__ == "__main__":
    llm = create_llm_client(provider="local", model_name="local-echo-v1")
    agent = ResearchAgent(llm=llm, web_search=WebSearchTool())
    topic = "latest trends in retrieval augmented generation"
    print(agent.run(topic))
