
# ASSESSMENT 3.2
# LINEAR DATA STRUCTURE: LINKED LIST
# LAST NAME: DELA CUESTA

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # INSERTION
    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

    # DISPLAY
    def display(self):
        current = self.head

        if current is None:
            print("EMPTY")
            return

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("NULL")

    # DELETION
    def remove(self):
        if self.head is not None:
            removed = self.head.data
            self.head = self.head.next
            return removed


my_list = LinkedList()

print("================================")
print("    LINKED LIST - DELA CUESTA")
print("================================")

# INSERTION
print("\nAdding letters to the linked list...")

for letter in "DELACUESTA":
    my_list.add(letter)

print("Linked list after insertion:")
my_list.display()

# DELETION
print("\nRemoving letters from the linked list...")

while my_list.head is not None:
    removed = my_list.remove()

    print("\nRemoved letter:", removed)
    print("Remaining linked list:")
    my_list.display()

print("\nLinked list is now EMPTY.")
print("================================")
