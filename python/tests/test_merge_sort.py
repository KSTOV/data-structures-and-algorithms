from code_challenges.merge_sort.merge import merge_sort

def test_import():
    assert merge_sort

def test_merge_sort():
    list = [2,7,4,6,1]
    merge_sort(list)
    assert list == [1,2,4,6,7]

def test_merge_sort2():
    list = [10,8,6,4,2,0]
    merge_sort(list)
    assert list == [0,2,4,6,8,10]

def test_merge_sort3():
    list = [1,1,1,1,0,0,0,0,3,3,3,3,2,2,2,2]
    merge_sort(list)
    assert list == [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]
