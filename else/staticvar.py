class Student:
    college="ucla"
    def __init__(self,name,no,marks):
        self.name1=name
        self.no1=no
        self.maeks1=marks
    def display(self):

        print("name is {},roll on is {},marks is {}, College name is{}".format(self.name1,self.no1,self.maeks1,Student.college)) 
s=Student("Vikas",100,78.46)
s.display()          