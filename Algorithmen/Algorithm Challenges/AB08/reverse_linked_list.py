class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next_node = None  # indicates the end of the list

    def __str__(self):
        return str(self.value)

    def reverse_linked_list(self):
        previous = None  # the tail will have no next mode
        current = self  # the starting point of the original list

        while current is not None:
            next_node = current.next_node  # to keep track of the original order
            current.next_node = previous  # reversing the link
            previous = current  # advancing previous one step forward
            current = next_node  # advancing current one step forward in the original order
        return previous  # the new head of the reversed list


# function to print the list
def print_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next_node
    print("None")


# linked lists and adding nodes
head = LinkedList(1)
head.next_node = LinkedList(2)
head.next_node.next_node = LinkedList(3)
head.next_node.next_node.next_node = LinkedList(4)

# before
print("Original list starts with: ")
print(head)

# reverse
reversed_list = head.reverse_linked_list()

# after
print("Reversed list: ")
print_list(reversed_list)
