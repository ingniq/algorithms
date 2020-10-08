class Deque:
    """Simple deque."""

    HEAD_INDEX = 0

    def __init__(self):
        """Initialize queue."""
        self.queue = []

    def addFront(self, item):
        """Add to head."""
        self.queue.insert(self.HEAD_INDEX, item)

    def addTail(self, item):
        """Add to tail."""
        self.queue.append(item)

    def removeFront(self):
        """Remove from head."""
        return self.queue.pop(self.HEAD_INDEX) if self.size() else None

    def removeTail(self):
        """Remove from tail."""
        return self.queue.pop() if self.size() else None

    def size(self):
        """Get queue size."""
        return len(self.queue)
