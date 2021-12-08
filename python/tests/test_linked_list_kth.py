from code_challenges.link_list_insertions.linked_list import LinkedList
import pytest

def test_kth_greater_than():
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    with pytest.raises(ValueError):
        list.kth_from_end(4)

def test_kth_same_length():
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    with pytest.raises(ValueError):
        list.kth_from_end(3)

def test_kth_not_positive():
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    with pytest.raises(ValueError):
        list.kth_from_end(-1)

def test_list_size():
    list = LinkedList()
    list.insert(1)
    assert list.kth_from_end(0) == 1

