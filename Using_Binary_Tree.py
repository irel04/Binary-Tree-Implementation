from Binary_Tree_Class import BinarySearchTreeNode

# This is to make the Binary Class on action
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [15, 12, 7, 14, 27, 20, 23, 88]
    numbers_tree = build_tree(numbers)
    # print(numbers_tree.search(200))
    print(numbers_tree.in_order_traversal())
    # print(numbers_tree.find_min())
    # print(numbers_tree.find_max())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())