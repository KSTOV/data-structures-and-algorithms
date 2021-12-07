from linked_list.linked_list import LinkedList

def test_append_end():
    list = LinkedList()
    list.insert("1")
    list.append("2")
    assert str(list) == "{ 1 } -> { 2 } -> NULL"


def test_append_multi_end():
    list = LinkedList()
    list.append("1")
    list.append("2")
    list.append("3")
    assert str(list) == "{ 1 } -> { 2 } -> { 3 } -> NULL"

def test_insert_before():
    list = LinkedList()
    list.insert("1")
    list.insert("3")
    list.insert("4")
    list.insert("5")
    list.insert_before("2",3)
    assert str(list) == "{ 5 } -> { 4 } -> { 3 } -> { 2 } -> { 1 } -> NULL"

def test_insert_after():
    list = LinkedList()
    list.insert("1")
    list.insert("2")
    list.insert("4")
    list.insert("5")
    list.insert_before("3",2)
    assert str(list) == "{ 5 } -> { 4 } -> { 3 } -> { 2 } -> { 1 } -> NULL"
