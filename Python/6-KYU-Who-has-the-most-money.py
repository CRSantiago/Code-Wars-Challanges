# You're going on a trip with some students and it's up to you to keep track of how much money each Student has. A student is defined like this:

# class Student:
#     def __init__(self, name, fives, tens, twenties):
#         self.name = name
#         self.fives = fives
#         self.tens = tens
#         self.twenties = twenties
# As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. If every student has the same amount, then return "all".

# Notes:

# Each student will have a unique name
# There will always be a clear winner: either one person has the most, or everyone has the same amount
# If there is only one student, then that student has the most money

class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)

students = [geoff]

def most_money(students):
    std_dict = {}
    for student in students:
        student_total = (student.fives * 5) + (student.tens * 10) + (student.twenties * 20)
        std_dict[student.name] = student_total

    if len(students) > 1:
        if max(std_dict, key=std_dict.get) == min(std_dict, key=std_dict.get):
            return 'all'
        else:
            return max(std_dict, key=std_dict.get)
    else:
        return students[0].name
