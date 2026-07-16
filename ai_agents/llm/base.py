from dataclasses import dataclass
from typing import Protocol


@dataclass
class LLMRequest:
    prompt: str
    system: str = ""
    temperature: float = 0.2
    max_tokens: int = 500


class LLMClient(Protocol):
    def generate(self, request: LLMRequest) -> str:
        ...
