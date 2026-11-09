SIZE = 5
stack = [None] * SIZE
top = -1


def is_empty():
    return top == -1


def is_full():
    return top == SIZE - 1


def push(item):
    global top
    if is_full():
        print("Stack Overflow")
    else:
        top = top + 1
        stack[top] = item
        print(item, "pushed")


def pop():
    global top
    if is_empty():
        print("Stack Underflow")
    else:
        item = stack[top]
        stack[top] = None
        top = top - 1
        print(item, "popped")


def peek():
    if is_empty():
        print("Stack is empty")
    else:
        print("Top item:", stack[top])


def display():
    if is_empty():
        print("Stack is empty")
    else:
        for i in range(top, -1, -1):
            print(stack[i])


# Test
push(10)
push(20)
push(30)
display()
peek()
pop()
display()