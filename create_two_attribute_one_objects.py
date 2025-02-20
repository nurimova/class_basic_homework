from create_two_attribute import Person

#create an object named "person" whose name is "Ali", age is "25"
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
person=Person(name='Ali', age=25)
print(f"Name: {person.name}, Age: {person.age}")