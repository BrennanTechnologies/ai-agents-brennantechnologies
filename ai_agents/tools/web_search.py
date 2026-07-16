class WebSearchTool:
    def search(self, query: str, max_results: int = 5) -> list[dict[str, str]]:
        try:
            from ddgs import DDGS
        except ImportError as exc:
            raise RuntimeError("ddgs package is not installed") from exc

        results: list[dict[str, str]] = []
        with DDGS() as ddgs:
            for item in ddgs.text(query, max_results=max_results):
                results.append(
                    {
                        "title": item.get("title", ""),
                        "url": item.get("href", ""),
                        "snippet": item.get("body", ""),
                    }
                )
        return results
