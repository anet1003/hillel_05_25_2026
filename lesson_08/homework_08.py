class Student:


    def __init__(self, name, surname, age, rating):
        self.name = name
        self.surname = surname
        self.age = age
        self.rating = rating


    def change_rating(self, new_rating):
        self.rating = new_rating


    def show_info(self):
        print(f"Name: {self.name}, " 
              f"Surname:{self.surname}, " 
              f"Age:{self.age}, " 
              f"Rating:{self.rating},")


my_student = Student(name='Anna',surname='Malko', age=18, rating=100)
my_student.show_info()
my_student.change_rating(55)
my_student.show_info()

