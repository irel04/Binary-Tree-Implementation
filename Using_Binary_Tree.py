from Binary_Tree_Class import BinarySearchTreeNode

# This is to make the Binary Class on action
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [23, 56, 45, 200, 123, 20, 6]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.search(200))
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())