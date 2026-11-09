class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the rear (back) of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            return "Queue Underflow: queue is empty"
        return self.items.pop(0)

    def front(self):
        """Return the front item without removing it."""
        if self.is_empty():
            return "Queue is empty"
        return self.items[0]

    def rear(self):
        """Return the last item without removing it."""
        if self.is_empty():
            return "Queue is empty"
        return self.items[-1]

    def is_empty(self):
        """True if the queue has no items."""
        return len(self.items) == 0

    def size(self):
        """Number of items in the queue."""
        return len(self.items)

    def display(self):
        """Show the queue from front to rear."""
        print("Queue (front -> rear):", self.items)

        
q = Queue()

print("Is empty?", q.is_empty())
print("Dequeue on empty:", q.dequeue())

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.display()

print("Front:", q.front())
print("Rear:", q.rear())
print("Size:", q.size())

print("Dequeue:", q.dequeue())
q.display()

print("Dequeue:", q.dequeue())
print("Dequeue:", q.dequeue())
print("Is empty?", q.is_empty())
print("Dequeue on empty:", q.dequeue())