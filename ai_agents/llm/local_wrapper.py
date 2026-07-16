from ai_agents.llm.base import LLMClient, LLMRequest


class LocalEchoLLM(LLMClient):
    """Deterministic local fallback for demos/tests without external APIs."""

    def __init__(self, model_name: str = "local-echo-v1") -> None:
        self.model_name = model_name

    def generate(self, request: LLMRequest) -> str:
        header = f"[local:{self.model_name}]"
        if request.system:
            return f"{header} system={request.system}\n{request.prompt}"
        return f"{header} {request.prompt}"
