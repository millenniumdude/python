class node:
    def __init__(self, prev= None, item = None, next= None):
        self.prev = prev
        self.item = item
        self.next = next


class DLL:
    def __init__(self, start = None):
        self.start = start
        
    def is_empty(self):
        return self.start == None
    
    def insert_at_begining(self, data):
        n = node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start= n

    def insert_at_last(self, data):
        temp = self.start
        if self.start is not None:
            while temp.next is not None:
                temp = temp.next
        
        n = node(temp, data, None)

        if temp == None:
            self.start = n
        else: 
            temp.next = n


    def search(self, data):
        temp = self.start 
        while temp is not None:
            if temp.data == data:            
                return data    
            temp = temp.next
        return None


    def insert_after(self, value, data):
        temp = self.start
        while temp is not None and temp.item != value:
            temp = temp.next
        if temp is not None:
            n = node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n


    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end ="->")
            temp =temp.next



    def delete_first(self):
        if self.is_empty():
            return
        self.start = self.start.next
        if self.start is not None:
            self.start.prev = None

    def delete_last(self):
        
        if self.is_empty():
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next is None

    def delete_item(self, data):
        temp = self.start 
        while temp is not None:
            if temp.item == data:
                if temp.next is not None:            
                    temp.next.prev = temp.prev
                if temp.prev is not None:    
                    temp.prev.next = temp.next
                else:
                    self.start = temp.next
                break
            temp = temp.next 


obj =DLL()

obj.insert_at_begining(550)

obj.insert_after(550,30)
obj.insert_at_last(50)
obj.delete_item(30)

obj.delete_first()
#obj.delete_last()
obj.print_list()