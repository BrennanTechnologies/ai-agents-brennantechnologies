from ai_agents.agents.base_agent import BaseAgent
from ai_agents.llm.factory import create_llm_client


def main() -> None:
    llm = create_llm_client()
    agent = BaseAgent(llm)
    print(agent.run("Summarize the purpose of this repository."))


if __name__ == "__main__":
    main()
