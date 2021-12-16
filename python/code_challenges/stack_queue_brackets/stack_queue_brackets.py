from code_challenges.stack_and_queue.stack_and_queues import Stack

def validate_brackets(string):
    stack = Stack()

    for i in string:
        if i in "[{(" or ")}]":
            stack.push(i)
            return True
        else:
            return False
