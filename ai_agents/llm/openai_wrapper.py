from ai_agents.llm.base import LLMClient, LLMRequest


class OpenAILLM(LLMClient):
    def __init__(self, api_key: str, model_name: str = "gpt-4o-mini") -> None:
        self.api_key = api_key
        self.model_name = model_name

    def generate(self, request: LLMRequest) -> str:
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise RuntimeError("openai package is not installed") from exc

        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")

        client = OpenAI(api_key=self.api_key)
        messages = []
        if request.system:
            messages.append({"role": "system", "content": request.system})
        messages.append({"role": "user", "content": request.prompt})

        response = client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )
        return response.choices[0].message.content or ""
