class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):

        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def __str__(self):
        current = self.head
        output = ""

        while current:
            output += "{ " + current.value + " } -> "
            current = current.next

        output += "NULL"
        return output
