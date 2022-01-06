from code_challenges.insertion_sort.insertion import insertion_sort

def test_import():
    assert insertion_sort

def test_insertion_sort():
    list = [2,1,7,6,3]
    assert insertion_sort(list) == [1,2,3,6,7]

def test_insertion_sort2():
    list = [10,8,6,4,2,0]
    assert insertion_sort(list) == [0,2,4,6,8,10]

def test_insertion_sort3():
    list = [1,1,1,1,0,0,0,0,3,3,3,3,2,2,2,2]
    assert insertion_sort(list) == [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]
