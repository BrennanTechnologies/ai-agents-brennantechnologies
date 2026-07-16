from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AppConfig:
    default_provider: str = os.getenv("DEFAULT_LLM_PROVIDER", "local")
    default_model_name: str = os.getenv("DEFAULT_MODEL_NAME", "local-echo-v1")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
