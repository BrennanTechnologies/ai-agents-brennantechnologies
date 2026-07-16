import subprocess
import tempfile
from pathlib import Path


class CodeExecutor:
    def run_python(self, code: str, timeout_seconds: int = 8) -> dict[str, str | int]:
        with tempfile.TemporaryDirectory() as tmp:
            script_path = Path(tmp) / "snippet.py"
            script_path.write_text(code, encoding="utf-8")
            proc = subprocess.run(
                ["python", str(script_path)],
                capture_output=True,
                text=True,
                timeout=timeout_seconds,
            )
            return {
                "returncode": proc.returncode,
                "stdout": proc.stdout,
                "stderr": proc.stderr,
            }
