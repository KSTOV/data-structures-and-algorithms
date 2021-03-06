class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self, next=None):
        self.head = None
        self.next = next

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        current = self.head
        if current:
            while current.next != None:
                current = current.next
            current.next = Node(value)
        else:
            self.head = Node(value, self.head)

    def insert_before(self, value, position):
        new = Node(value)
        pointer = self.head
        counter = 1
        if position == 0:
            new.next = self.head
            self.head = new
            return self.head
        while pointer.next is not None:
            if counter == position:
                new.next = pointer.next
                pointer.next = new
                break
            counter += 1
            pointer = pointer.next
        return self.head

    def insert_after(self, value, position):
        new = Node()
        pointer = self.head
        counter = 1
        if position == 0:
            new.next = self.head
            self.head = new
            return self.head
        while pointer.next is not None:
            if counter == position:
                new.next = pointer.next
                pointer.next = new
                break
            counter += 1
            pointer = pointer.next
        return self.head

    def __str__(self):
        current = self.head
        output = ""

        while current:
            output += "{ " + current.value + " } -> "
            current = current.next

        output += "NULL"
        return output

    def kth_from_end(self, k):
        if k < 0:
            raise ValueError

        for _ in range(k):
            if self.head.next is None:
                raise ValueError
            self.head = self.head.next

        while self.head.next is not None:
            self.head = self.head.next

        return self.head.value

    def merge_list(self, a, b):
        a_curr = a.head
        b_curr = b.head

        while a_curr and b_curr:

            a_next = a_curr.next
            a_curr.next = b_curr
            a_curr = a_next

            b_next = b_curr.next
            b_curr.next = a_curr
            b_curr = b_next

            if a_curr.next is None:
                a_curr.next = b_curr
                return a
        return a
