from code_challenges.stack_and_queue.stack_and_queues import Stack

class Dog:
    pass

class Cat:
    pass

class Cow:
    pass

class AnimalShelter:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def enqueue(self, animal):
        if isinstance(animal,Dog) or isinstance(animal,Cat):
            self.stack_in.push(animal)
            return True
        else:
            return False

    def dequeue(self, pref):
        if isinstance(pref,Dog) or isinstance(pref,Cat):
            self.stack_out.push(pref)
            return True
        else:
            return False
