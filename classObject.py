class Student:
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks
    
    def display(self):
        print(self.name , self.id)

rahul = Student(1, "Rahul", 90)
rakesh = Student(2, "Rakesh", 55)

rahul.display()
rakesh.display()