from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class ProcessedChunk:
    doc_id: str
    text: str


class DocumentProcessor:
    def __init__(self, chunk_size: int = 500) -> None:
        self.chunk_size = chunk_size

    def _chunk_text(self, text: str) -> list[str]:
        clean = " ".join(text.split())
        return [clean[i : i + self.chunk_size] for i in range(0, len(clean), self.chunk_size)]

    def process_text(self, doc_id: str, text: str) -> list[ProcessedChunk]:
        return [ProcessedChunk(doc_id=doc_id, text=chunk) for chunk in self._chunk_text(text)]

    def process_files(self, paths: Iterable[str]) -> list[ProcessedChunk]:
        chunks: list[ProcessedChunk] = []
        for path in paths:
            file_path = Path(path)
            text = file_path.read_text(encoding="utf-8")
            chunks.extend(self.process_text(file_path.name, text))
        return chunks
