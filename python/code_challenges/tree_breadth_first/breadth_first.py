from code_challenges.stack_and_queue.stack_and_queues import Queue

def breadth_first(tree):
    list = []
    queue = Queue()

    if tree.root is None:
        return list

    queue.enqueue(tree.root)

    while not queue.is_empty():
        dequeue = queue.dequeue()
        list.append(dequeue.value)
        if dequeue.left:
            queue.enqueue(dequeue.left)
        if dequeue.right:
            queue.enqueue(dequeue.right)

    return list
