from ai_agents.llm.base import LLMClient, LLMRequest


class AnthropicLLM(LLMClient):
    def __init__(self, api_key: str, model_name: str = "claude-3-5-sonnet-latest") -> None:
        self.api_key = api_key
        self.model_name = model_name

    def generate(self, request: LLMRequest) -> str:
        try:
            import anthropic
        except ImportError as exc:
            raise RuntimeError("anthropic package is not installed") from exc

        if not self.api_key:
            raise RuntimeError("ANTHROPIC_API_KEY is not set")

        client = anthropic.Anthropic(api_key=self.api_key)
        message = client.messages.create(
            model=self.model_name,
            system=request.system or None,
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            messages=[{"role": "user", "content": request.prompt}],
        )
        chunks = []
        for block in message.content:
            text = getattr(block, "text", None)
            if text:
                chunks.append(text)
        return "\n".join(chunks)
