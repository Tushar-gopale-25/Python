# Method to remove at given index
def remove_at_index(self, index):
    if self.head is None:
        return

    current_node = self.head
    position = 0
    
    if index == 0:
        self.remove_first_node()
    else:
        while current_node is not None and position < index - 1:
            position += 1
            current_node = current_node.next
        
        if current_node is None or current_node.next is None:
            print("Index not present")
        else:
            current_node.next = current_node.next.next