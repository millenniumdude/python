
# 1. Define a class Node to describe a node of a Singly Linked List.

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# 2. Define a class SLL to implement Singly Linked list with __init__() method to create and initialize start reference variable.

class SLL:
    def __init__(self, start = None):
        self.start = start

# 3. Define a method is_empty() to check if the linked list is empty in SLL class.

    def is_empty(self):
        return self.start == None

# 4. In class SLL, Define a method insert_at_start() to insert an element at the starting of the list.

    def insert_at_start(self, data):
        new_node = Node(data, self.start)
        self.start = new_node

# 5. In class SLL, define a method insert_at_last() to insert an element at the end of the list.

    def insert_at_last(self, data):
        new_node = Node(data)
        if not self.is_empty(): #list is not entry
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = new_node  
        else:
            self.start =new_node

# 6. In class SLL, define a method search() to find the node with specified element value.

    def search_element(self,data):
        temp = self.start
        while temp != None: #list is not entry
            if temp.data == data:
                return temp  
            temp = temp.next
        return None
    
# 7. In class SLL, define a method insert_after() to insert a new node after a given Node of the list.

    def insert_after(self, temp, new_data):
        if temp is not None:
             new_node = Node(new_data,temp.next)
             temp.next = new_node

# 8. In class SLL, define a method to print all the elements of the list.

    def print_ll(self):
        temp = self.start
        while temp != None:
            print(temp.data, end=" -> ")
            temp = temp.next 

# 9. In class SLL, define a method delete_first() to delete first element from the list.

    def delete_first(self):
        if (self.start is None):
            print("The Singly Linked list is empty")
            return
        self.start = self.start.next
        print("First node deleted successfully.")

# 10. In class SLL, define a method delete_last() to delete last element from the list.

    def delete_last(self):
        if not self.start:
            print("The Singly Linked list is empty. Cannot delete.")
            return

        if not self.start.next: 
            self.start = None
            return

        current = self.start
        while current.next.next: 
            current = current.next
        current.next = None   

# 11. In class SLL, define a method delete_item() to delete specific element from the list.

    def delete_item(self, target_element):
        current = self.start
        prev = None

        if current is not None and current.data is target_element:
            self.start = current.next
            current = None  
            return

        while current is not None and current.data is not target_element:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None  


obj=SLL()

obj.insert_at_start(50)
obj.insert_at_last(20)




obj.print_ll()
