from code_challenges.quick_sort.quick import quick_sort

def test_import():
    assert quick_sort

def test_quick_sort():
    list = [2,1,7,6,3]
    quick_sort(list, 0, len(list) - 1)
    assert list == [1,2,3,6,7]

def test_quick_sort2():
    list = [10,8,6,4,2,0]
    quick_sort(list, 0, len(list) - 1)
    assert list == [0,2,4,6,8,10]

def test_quick_sort3():
    list = [1,1,1,1,0,0,0,0,3,3,3,3,2,2,2,2]
    quick_sort(list, 0, len(list) - 1)
    assert list == [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]
