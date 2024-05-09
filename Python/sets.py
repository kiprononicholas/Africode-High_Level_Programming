students = {"enock" , "bett" ,"naomy" , "nicko" ,"gladwel"}
# students_sets [3] = "kiprono"


# print(students{2})

students1 = {"enock" , "bett" ,"naomy" , "ian" ,"ben"}

# print(students.intersection(students1))
# print(students.difference(students1))
# print(students1.difference(students))
# print(students.union(students1))        print all the value


male_students ={"enock" , "bett" , "nicko"} 


# if male_students.issubset(students):
#     print("male_students is a subset of students")
# else:
#     print("male_students is not a subset of students")

if students.issuperset(male_students):
    print("students is a superset of male_students")
else:
    print("students is not a superset of male_students")
