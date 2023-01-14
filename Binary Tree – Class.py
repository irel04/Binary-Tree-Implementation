class BinarySearchTreenode():
    # This part is used to create instance object
    # It basicall automatically creates properties that all object will take
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # This is a method for adding or reading a data 
    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            # Add data to the left subtree
            if self.left:
                self.left.add_child( data)
            else:
                self.left = BinarySearchTreenode(data)
        else:
            # Add data to the right subtree
            if self.right:
                self.right.add_child( data)
            else:
                self.right = BinarySearchTreenode(data)