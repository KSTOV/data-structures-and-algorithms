from code_challenges.tree_intersection.tree_intersection import tree_intersection
from code_challenges.trees.trees import Node
from code_challenges.trees.trees import BinaryTree

def test_import():
    assert tree_intersection

def test_tree_intersection():

    one = Node(1)
    one.left = Node(2)
    one.right = Node(3)
    one.left.left = Node(4)
    one.left.right = Node(5)


    two = Node(1)
    two.left = Node(2)
    two.right = Node(3)
    two.left.left = Node(4)
    two.left.right = Node(5)

    tree_1 = BinaryTree(one)
    tree_2 = BinaryTree(two)

    assert tree_intersection(tree_1,tree_2) == [1,2,3,4,5]

def test_tree_intersection_2():

    one = Node(1)
    one.left = Node(2)
    one.right = Node(3)
    one.left.left = Node(6)
    one.left.right = Node(5)

    two = Node(1)
    two.left = Node(2)
    two.right = Node(3)
    two.left.left = Node(4)
    two.left.right = Node(7)

    tree_1 = BinaryTree(one)
    tree_2 = BinaryTree(two)

    assert tree_intersection(tree_1,tree_2) == [1,2,3]

def test_tree_intersection_3():

    one = Node(1)
    one.left = Node(4)
    one.right = Node(3)
    one.left.right = Node(5)

    two = Node(1)
    two.left = Node(2)
    two.right = Node(3)
    two.left.left = Node(6)

    tree_1 = BinaryTree(one)
    tree_2 = BinaryTree(two)

    assert tree_intersection(tree_1,tree_2) == [1,3]
