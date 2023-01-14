from Binary_Tree_Class import BinarySearchTreeNode

# This is to make the Binary Class on action
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print("\nThere is 200 in the list: ", numbers_tree.search(200))
    print("Minimum value: ", numbers_tree.find_min())
    print("Maximum value: ", numbers_tree.find_max())
    print("In order traversal: ", numbers_tree.in_order_traversal())
    print("Pre-order traversal: ", numbers_tree.pre_order_traversal())
    print("Post-order traversal: ", numbers_tree.post_order_traversal())