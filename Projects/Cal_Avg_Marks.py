class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg(self):
        total=0
        for val in self.marks:
            total+=val
            avg=total/len(self.marks)

        print(f"Hi!..{self.name} your avg is {avg}")    


s1=Student("SHiva",[98,88,95])
s1.avg()

s2=Student("GOri",[95,94,97])
s2.avg()                

s3=Student("ShivGori",[98,94,96,95,97])
s3.avg()