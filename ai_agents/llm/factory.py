from ai_agents.config import AppConfig
from ai_agents.llm.anthropic_wrapper import AnthropicLLM
from ai_agents.llm.base import LLMClient
from ai_agents.llm.local_wrapper import LocalEchoLLM
from ai_agents.llm.openai_wrapper import OpenAILLM


def create_llm_client(
    provider: str | None = None,
    model_name: str | None = None,
    config: AppConfig | None = None,
) -> LLMClient:
    cfg = config or AppConfig()
    selected_provider = (provider or cfg.default_provider).lower()
    selected_model = model_name or cfg.default_model_name

    if selected_provider == "openai":
        return OpenAILLM(api_key=cfg.openai_api_key, model_name=selected_model)
    if selected_provider == "anthropic":
        return AnthropicLLM(api_key=cfg.anthropic_api_key, model_name=selected_model)
    return LocalEchoLLM(model_name=selected_model)
