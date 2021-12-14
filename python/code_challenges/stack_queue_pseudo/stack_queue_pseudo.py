from code_challenges.stack_and_queue.stack_and_queues import Stack

class PseudoQueue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def enqueue(self, value):
        while not self.stack_out.is_empty():
            self.stack_in.push(self.stack_out.pop())
        self.stack_in.push(value)

    def dequeue(self):
        while not self.stack_in.is_empty():
            self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()
