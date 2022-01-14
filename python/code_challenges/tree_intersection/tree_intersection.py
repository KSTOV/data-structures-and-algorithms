def tree_intersection(tree_1, tree_2):
    tree_1_set = set(tree_1.pre_order())
    intersection = tree_1_set.intersection(tree_2.pre_order())
    intersection_list = list(intersection)
    return intersection_list
