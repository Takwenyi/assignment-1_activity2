# Assignment 1: Student class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)

# Create a student object and display info
student1 = Student("Celia", 19, "A")
student1.display_info()

print()  # Adds space between outputs

# Activity 2: Vehicle and Car classes
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)

class Car(Vehicle):
    def __init__(self, brand, speed, color):
        super().__init__(brand, speed)
        self.color = color

    def show_details(self):
        self.show_info()
        print("Color:", self.color)

# Create vehicle and car objects
vehicle1 = Vehicle("Toyota", 180)
vehicle1.show_info()

print()  # Adds space between outputs

car1 = Car("BMW", 240, "Red")
car1.show_details()
