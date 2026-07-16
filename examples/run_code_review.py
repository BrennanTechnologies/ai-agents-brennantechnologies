from ai_agents.agents.code_review_agent import CodeReviewAgent
from ai_agents.llm.factory import create_llm_client


SAMPLE_CODE = '''
def divide(a, b):
    return a / b

print(divide(10, 0))
'''

if __name__ == "__main__":
    llm = create_llm_client(provider="local", model_name="local-echo-v1")
    reviewer = CodeReviewAgent(llm=llm)
    print(reviewer.run(SAMPLE_CODE))
