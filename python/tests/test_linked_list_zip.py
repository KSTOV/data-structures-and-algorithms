from code_challenges.link_list_insertions.linked_list import LinkedList

def test_linked_list_zip():
    list1 = LinkedList()
    list1.insert("1")
    list1.insert("2")
    list1.insert("3")

    list2 = LinkedList()
    list2.insert("a")
    list2.insert("b")
    list2.insert("c")

    res = list1.merge_list(list1, list2)
    actual = res.__str__()
    expected = "{ 3 } -> { c } -> { 2 } -> { b } -> { 1 } -> { a } -> NULL"
    assert actual == expected
