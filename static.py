class Student:
    name="Pradeep" #--> static attributes
    course="BCA"
    subject="python"
    roll_no=34

    def __init__(self):
        pass

s1=Student()
print(Student.__dict__)
print(Student.name)
