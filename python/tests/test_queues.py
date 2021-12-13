import pytest
from code_challenges.stack_and_queue.stack_and_queues import Queue

def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(1)

    assert queue.peek() == 1

def test_queue_enqueue_multi():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.peek() == 1

def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)

    queue.dequeue()

    assert queue.peek() == 2

def test_queue_dequeue_multi():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    queue.dequeue()

    assert queue.peek() == 3


def test_queue_peek():
    queue = Queue()
    queue.enqueue(1)

    assert queue.peek() == 1

def test_queue_empty():
    queue = Queue()

    assert queue.is_empty() == True
