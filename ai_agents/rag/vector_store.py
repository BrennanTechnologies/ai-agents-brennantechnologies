from collections import Counter
from dataclasses import dataclass
import math
import re


TOKEN_PATTERN = re.compile(r"[a-zA-Z0-9_]+")


def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN_PATTERN.findall(text)]


@dataclass
class StoredVector:
    item_id: str
    text: str
    vector: Counter


class InMemoryVectorStore:
    def __init__(self) -> None:
        self._items: list[StoredVector] = []

    def add(self, item_id: str, text: str) -> None:
        vec = Counter(tokenize(text))
        self._items.append(StoredVector(item_id=item_id, text=text, vector=vec))

    def all_items(self) -> list[StoredVector]:
        return list(self._items)

    @staticmethod
    def cosine_similarity(a: Counter, b: Counter) -> float:
        if not a or not b:
            return 0.0
        dot = sum(a[token] * b[token] for token in a.keys() & b.keys())
        mag_a = math.sqrt(sum(v * v for v in a.values()))
        mag_b = math.sqrt(sum(v * v for v in b.values()))
        if mag_a == 0 or mag_b == 0:
            return 0.0
        return dot / (mag_a * mag_b)
