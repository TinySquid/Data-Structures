import sys

sys.path.append("../queue_and_stack")
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Create a node
        node = BinarySearchTree(value)

        # Check value vs self to determine which direction to go
        if node.value >= self.value:
            if self.right != None:
                # Travel right
                self.right.insert(value)
            else:
                self.right = node
        else:
            if self.left != None:
                # Travel left
                self.left.insert(value)
            else:
                self.left = node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Base case
        if self.value == target:
            return True
        elif self.value > target:
            if self.left != None:
                return self.left.contains(target)
        elif self.value < target:
            if self.right != None:
                return self.right.contains(target)

        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # Self ref
        current_node = self

        # Max value tracker
        max_value = current_node.value

        # While we can traverse right
        while current_node:
            # Check if we can go right
            if current_node.right != None:
                # Set current_node pointer to right node for next iteration
                current_node = current_node.right
            else:
                # Break out of loop
                max_value = current_node.value
                current_node = None

        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # In-Order -> LEFT NODE | NODE | RIGHT NODE
        if node.left != None:  # L
            self.in_order_print(node.left)

        print(node.value)  # N

        if node.right != None:  # R
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue.len() > 0:
            current_node = queue.dequeue()
            print(current_node.value)

            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.len() > 0:
            current_node = stack.pop()
            print(current_node.value)

            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # Pre-Order -> NODE | LEFT NODE | RIGHT NODE
        print(node.value)  # N

        if node.left != None:  # L
            self.pre_order_dft(node.left)

        if node.right != None:  # R
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # Post-Order -> LEFT NODE | RIGHT NODE | NODE
        if node.left != None:  # L
            self.post_order_dft(node.left)

        if node.right != None:  # R
            self.post_order_dft(node.right)

        print(node.value)  # N
