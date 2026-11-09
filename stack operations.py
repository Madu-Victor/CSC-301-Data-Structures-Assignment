class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            return "Stack Underflow: stack is empty"
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        """True if the stack has no items."""
        return len(self.items) == 0

    def size(self):
        """Number of items in the stack."""
        return len(self.items)

    def display(self):
        """Show the stack from bottom to top."""
        print("Stack (bottom -> top):", self.items)


s = Stack()

print("Is empty?", s.is_empty())
print("Pop on empty:", s.pop())

s.push(10)
s.push(20)
s.push(30)
s.display()

print("Peek:", s.peek())
print("Size:", s.size())

print("Pop:", s.pop())
s.display()

print("Pop:", s.pop())
print("Pop:", s.pop())
print("Is empty?", s.is_empty())
print("Pop on empty:", s.pop())