from code_challenges.trees.trees import Node
from code_challenges.trees.trees import BinaryTree
from code_challenges.trees.trees import BinarySearchTree

def test_binary_tree_empty():
    assert BinaryTree

def test_binary_tree_root():
    one = Node("1")
    tree = BinaryTree(one)
    assert tree.root.value == "1"

def test_binary_tree_left():
    one = Node("1")
    one.left = Node("2")
    tree = BinaryTree(one)
    assert tree.root.left.value == "2"

def test_binary_tree_right():
    one = Node("1")
    one.right = Node("3")
    tree = BinaryTree(one)
    assert tree.root.right.value == "3"

def test_binary_pre_order():
    one = Node("1")
    one.left = Node("2")
    one.right = Node("3")
    tree = BinaryTree(one)
    assert tree.pre_order() == ["1","2","3"]

def test_binary_in_order():
    one = Node("1")
    one.left = Node("2")
    one.right = Node("3")
    tree = BinaryTree(one)
    assert tree.in_order() == ["2","1","3"]

def test_binary_post_order():
    one = Node("1")
    one.left = Node("2")
    one.right = Node("3")
    tree = BinaryTree(one)
    assert tree.post_order() == ["2","3","1"]

def test_binary_search():
    bst = BinarySearchTree()
    assert isinstance(bst, BinaryTree)

def test_binary_search_empty():
    assert BinarySearchTree()

def test_binary_search_add():
    bst = BinarySearchTree()
    bst.add(1)
    assert bst.root.value == 1

def test_binary_search_contains_false():
    one = Node(1)
    one.left = Node(2)
    one.right = Node (3)
    bst = BinarySearchTree(one)
    assert bst.contains(4) == False

def test_binary_search_contains_true():
    one = Node(1)
    one.left = Node(2)
    one.right = Node (3)
    bst = BinarySearchTree(one)
    assert bst.contains(3) == True

def test_tree_max_empty():
    tree = BinaryTree()
    assert tree.max_value() is None

def test_tree_max():
    one = Node(1)
    one.left = Node(2)
    one.right = Node(3)
    tree = BinaryTree(one)
    assert tree.max_value() == 3

def test_tree_max_more_nodes():
    one = Node(1)
    one.left = Node(2)
    one.right = Node(3)
    one.left.left = Node(4)
    one.left.right = Node(5)
    one.right.left = Node(6)
    one.right.right = Node(7)
    tree = BinaryTree(one)
    assert tree.max_value() == 7

def test_tree_max_mix_numbers():
    one = Node(1)
    one.left = Node(20)
    one.right = Node(33)
    one.left.left = Node(4)
    one.left.right = Node(500)
    one.right.left = Node(49)
    one.right.right = Node(17)
    tree = BinaryTree(one)
    assert tree.max_value() == 500
