from Student import Student     #first Student is the file then the second Student is the class, Student itself

student1 = Student("Mark", "Computer Science", 4.0, False)
student2 = Student("Pam", "Art", 2.5, True)
print(student1.major + " " + str(student1.gpa))