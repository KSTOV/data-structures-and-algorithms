from code_challenges.trees.trees import Node
from code_challenges.trees.trees import BinaryTree
from code_challenges.tree_breadth_first.breadth_first import breadth_first

def test_breadth_first():
    tree = BinaryTree()
    assert breadth_first(tree) == []

def test_breadth_first_root():
    one = Node(1)
    tree = BinaryTree(one)
    assert breadth_first(tree) == [1]

def test_breadth_first_left():
    one = Node(1)
    one.left = Node(2)
    tree = BinaryTree(one)
    assert breadth_first(tree) == [1,2]

def test_breadth_first_right():
    one = Node(1)
    one.right = Node(3)
    tree = BinaryTree(one)
    assert breadth_first(tree) == [1,3]

def test_breadth_first():
    one = Node(1)
    one.left = Node(2)
    one.right = Node(3)
    tree = BinaryTree(one)
    assert breadth_first(tree) == [1,2,3]

def test_breadth_first_more():
    one = Node(1)
    one.left = Node(2)
    one.right = Node(3)
    one.left.left = Node(4)
    one.left.right = Node(5)
    one.right.left = Node(6)
    one.right.right = Node(7)
    tree = BinaryTree(one)
    assert breadth_first(tree) == [1,2,3,4,5,6,7]

def test_breadth_first_more_different_order():
    one = Node(1)
    one.left = Node(7)
    one.right = Node(5)
    one.left.left = Node(4)
    one.left.right = Node(3)
    one.right.left = Node(2)
    one.right.right = Node(6)
    tree = BinaryTree(one)
    assert breadth_first(tree) == [1,7,5,4,3,2,6]
