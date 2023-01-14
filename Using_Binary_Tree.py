from Binary_Tree_Class import BinarySearchTreeNode

# This is to make the Binary Class on action
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(elements):
        root.add_child(elements[i])


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]

