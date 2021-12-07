from linked_list.linked_list import Node, LinkedList

def test_node():
    node = Node(1)
    actual = node.value
    expected = 1
    assert actual == expected
    assert node.next is None

def test_linked_list_head():
    list = LinkedList()
    actual = list.head
    expected = None
    assert actual == expected

def test_linked_list_insert_empty():
    list = LinkedList()
    list.insert(1)
    actual = list.head.value
    expected = 1
    assert actual == expected

def test_linked_list_insert_not_empty():
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    assert list.head.value == 2
    assert list.head.next.value == 1


def test_linked_list_includes():
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    assert list.includes(1) is True
    assert list.includes(3) is False

def test_linked_list_to_string():
    list = LinkedList()
    list.insert("1")
    list.insert("2")
    list.insert("3")
    assert str(list) == "{ 3 } -> { 2 } -> { 1 } -> NULL"
