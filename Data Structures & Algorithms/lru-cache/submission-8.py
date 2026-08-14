class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # Map key to node for O(1) lookups

        # Dummy head and tail nodes to eliminate edge cases for boundary insertions/deletions
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        # Detach an existing node from its current position in the doubly linked list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        # Insert a node right before the tail (marking it as most recently used)
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed node to the most recently used position (end of the list)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove the old node so we can update and re-insert it
            self.remove(self.cache[key])

        # Create/overwrite the node and place it at the most recently used position
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If capacity is exceeded, evict the least recently used node (the one right after head)
        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
