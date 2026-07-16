from collections.abc import Callable


State = dict[str, object]
NodeFn = Callable[[State], State]


class WorkflowGraph:
    def __init__(self) -> None:
        self._nodes: dict[str, NodeFn] = {}
        self._edges: dict[str, str] = {}
        self._start: str | None = None

    def add_node(self, name: str, fn: NodeFn) -> None:
        self._nodes[name] = fn
        if self._start is None:
            self._start = name

    def add_edge(self, source: str, target: str) -> None:
        self._edges[source] = target

    def run(self, state: State) -> State:
        if not self._start:
            raise RuntimeError("WorkflowGraph has no start node")

        current = self._start
        output = dict(state)
        while current:
            if current not in self._nodes:
                raise RuntimeError(f"Unknown node: {current}")
            output = self._nodes[current](output)
            current = self._edges.get(current, "")
        return output
