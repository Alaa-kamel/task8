import subject_module
import student_module

# Create objects of the Subject class
subject1 = subject_module.Subject("Math", 85)
subject2 = subject_module.Subject("Science", 90)
subject3 = subject_module.Subject("English", 80)

# Create objects of the Student class
student1 = student_module.Student("John", 18, "New York")
student2 = student_module.Student("Emily", 17, "London")
student3 = student_module.Student("Alex", 19, "Paris")

# Use the methods of the Student class
student1.add_mark(80)
student1.add_mark(75)
student1.add_mark(90)

student2.add_mark(95)
student2.add_mark(85)
student2.add_mark(88)

student3.add_mark(92)
student3.add_mark(87)
student3.add_mark(84)

print(student1.get_all_marks())
print(student1.calc_average())

print(student2.get_all_marks())
print(student2.calc_average())

print(student3.get_all_marks())
print(student3.calc_average())