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
        max_value = float("-inf")

        # While we can traverse right
        while current_node:
            # Compare current node value with current max value
            if current_node.value > max_value:
                max_value = current_node.value
            # Check if we can go right
            if current_node.right != None:
                # Set current_node pointer to right node for next iteration
                current_node = current_node.right
            else:
                # Break out of loop
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
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
