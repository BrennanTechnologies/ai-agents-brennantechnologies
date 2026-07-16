import json
from pathlib import Path


class MemoryStore:
    def __init__(self, path: str = ".agent_memory.json") -> None:
        self.path = Path(path)
        if not self.path.exists():
            self.path.write_text("{}", encoding="utf-8")

    def _read(self) -> dict[str, str]:
        return json.loads(self.path.read_text(encoding="utf-8"))

    def _write(self, data: dict[str, str]) -> None:
        self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def put(self, key: str, value: str) -> None:
        data = self._read()
        data[key] = value
        self._write(data)

    def get(self, key: str, default: str = "") -> str:
        return self._read().get(key, default)
