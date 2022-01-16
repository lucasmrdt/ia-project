import heapq
from dataclasses import dataclass, field
from typing import Any


class MinPriorityQueue:
    @dataclass(order=True)
    class PrioritizedItem:
        priority: int
        item: Any = field(compare=False)

    def __init__(self) -> None:
        self.queue = []

    def push(self, item: Any, priority: int):
        heapq.heappush(self.queue,  (self.PrioritizedItem(priority, item)))

    def pop(self):
        return heapq.heappop(self.queue).item
