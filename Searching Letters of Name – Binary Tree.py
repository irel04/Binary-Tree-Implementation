from Binary_Tree_Class import BinarySearchTreeNode

# This is to make the Binary Class on action
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = ['I', 'R', 'E', 'L', 'K', 'I', 'A', 'N', 'C','B', 'A', 'C', 'O', 'L','O','D']
    my_name = build_tree(numbers)
    print(my_name.search('R'))
    print(my_name.in_order_traversal())
    print(my_name.find_min())
    print(my_name.find_max())
    print(my_name.pre_order_traversal())