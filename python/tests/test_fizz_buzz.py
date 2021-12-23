from code_challenges.trees.trees import KaryTree
from code_challenges.tree_fizz_buzz.fizz_buzz import fizz_buzz

def test_kary_tree():
    assert KaryTree()

def test_fizz_buzz():
    assert fizz_buzz

def test_k_fizz_buzz():
    tree = KaryTree()
    tree.add(1)
    assert tree.root.value == 1

def test_k_fizz_buzz_fizz():
    tree = KaryTree()
    tree.add(3)
    assert fizz_buzz(tree).root.value == 'fizz'

def test_k_fizz_buzz_fizz2():
    tree = KaryTree()
    tree.add(6)
    assert fizz_buzz(tree).root.value == 'fizz'

def test_k_fizz_buzz_fizz3():
    tree = KaryTree()
    tree.add(9)
    assert fizz_buzz(tree).root.value == 'fizz'

def test_k_fizz_buzz_buzz():
    tree = KaryTree()
    tree.add(5)
    assert fizz_buzz(tree).root.value == 'buzz'

def test_k_fizz_buzz_buzz2():
    tree = KaryTree()
    tree.add(10)
    assert fizz_buzz(tree).root.value == 'buzz'

def test_k_fizz_buzz_buzz3():
    tree = KaryTree()
    tree.add(20)
    assert fizz_buzz(tree).root.value == 'buzz'

def test_k_fizz_buzz_fizz_buzz():
    tree = KaryTree()
    tree.add(15)
    assert fizz_buzz(tree).root.value == 'fizzbuzz'

def test_k_fizz_buzz_fizz_buzz2():
    tree = KaryTree()
    tree.add(30)
    assert fizz_buzz(tree).root.value == 'fizzbuzz'

def test_k_fizz_buzz_fizz_buzz3():
    tree = KaryTree()
    tree.add(45)
    assert fizz_buzz(tree).root.value == 'fizzbuzz'
