
#
# class bloodbank():
#     def __init__ (self, name, age, bloodtype):
#         self.name = name
#         self.age = age
#         self.bloodtype = bloodtype
#
#     def apositive(self, bloodcollection):
#         print("name -->", self.name)
#         print("age -->", self.age)
#         print("bloodtype -->", self.bloodtype)
#         count = bloodcollection[self.bloodtype]
#         print("remaining blood available ", count - 1)
#
#     def bpositive(self, bloodcollection):
#         print("name -->", self.name)
#         print("age -->", self.age)
#         print("bloodtype -->", self.bloodtype)
#         count = bloodcollection[self.bloodtype]
#         print("remaining blood available ", count - 1)
#
#     def abpositive(self):
#         print("name -->", self.name)
#         print("age -->", self.age)
#         print("bloodtype -->", self.bloodtype)
#         count = bloodcollection[self.bloodtype]
#         print("remaining blood available ", count - 1)
#
#
# bloodcollection = {"apositive": 2, "bpositive": 1, "abpositive": 3}
#
# bloodtype = input("enter the blood type :")
# name = input("enter the name :")
# age = int(input("enter the age: "))
#
# bloodtype = bloodtype.strip()
# if (bloodtype in bloodcollection):
#     tt = bloodbank(name, age, bloodtype)
#     if (bloodtype == "apositive"):
#         tt.apositive(bloodcollection)
#     elif (bloodtype == "bpositive"):
#         tt.bpositive(bloodcollection)










class marklist():
    def __init__(self,name,age,rollno,sub):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.sub=sub

    def tamil(self,marks):
        print("name",self.name)
        print("age",self.age)
        print("rollno",self.rollno)

        rankcard = marks[self.sub]
        print("print the remaining mark",rankcard-1)
    def english(self,marks):
        print("name",self.name)
        print("age",self.age)
        print("rollno",self.rollno)
        rankcard = marks[self.sub]
        print("print the remaining mark",rankcard-1)

marks = {"tamil": 2,"english": 1}
rollno = int(input("enter the rollno"))
name = input("enter the name")
age = int(input("enter the age"))
sub= input("enter the sub")


sub = sub.strip()
if (sub in marks):
    tt = marklist(name, age, rollno,sub)
    if (sub == "tamil"):
        tt.tamil(marks)
    elif (sub  == "english"):
        tt.english(marks)















