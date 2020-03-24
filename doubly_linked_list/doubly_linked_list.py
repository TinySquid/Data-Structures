"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_from_head(self):
        if self.head:
            value = self.head.value
            self.delete(self.head)
            return value
        else:
            return None

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    def move_to_front(self, node):
        if node is self.head:
            return

        value = node.value
        self.delete(node)
        self.add_to_head(value)

    def move_to_end(self, node):
        if node is self.tail:
            return

        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    def exists(self, value):
        node = self.head

        while node:
            if node.value == value:
                return True
            node = node.next

        return False

    def find(self, value):
        node = self.head

        while node:
            if node.value == value:
                return node
            node = node.next

        return None

    def delete(self, node):
        # TODO: Catch errors if list is empty or node is not in list
        # For now assumine node is in list
        self.length -= 1

        # Node is the only item in list
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # Node is head
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        # Node is tail
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        # Node is between head and tail
        else:
            node.delete()

    def __str__(self):
        node = self.head
        values = ""
        while node is not None:
            values += str(node.value) + " "
            node = node.next
        return values
