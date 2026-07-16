from ai_agents.agents.base_agent import BaseAgent
from ai_agents.llm.factory import create_llm_client


if __name__ == "__main__":
    llm = create_llm_client(provider="local", model_name="local-echo-v1")
    agent = BaseAgent(llm)
    result = agent.run("Create a launch plan for an AI feature in three bullets.")
    print(result)
