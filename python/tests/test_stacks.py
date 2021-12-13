from code_challenges.stack_and_queue.stack_and_queues import Stack

def test_stack_push():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1

def test_stack_push_multi():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3

    stack.pop()
    assert stack.peek() == 2

    stack.pop()
    assert stack.peek() == 1

def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()

    assert stack.peek() == 1

def test_stack_pop_multi():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3

    stack.pop()
    stack.pop()
    assert stack.peek() == 1


def test_stack_empty():
    stack = Stack()
    assert stack.is_empty() == True

def test_stack_peek():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1
