# marks={}
# x=int(input("enter maths marks:"))
# marks.update({"Maths":x})
# x=int(input("enter chemistry marks:"))
# marks.update({'Chemistry':x})
# print(marks)


# set={
#   ("int",9),
#   ("float",9.0)}
# print(set)
# A=set()
# A.add(1)
# A.add("234")
# A.add((1,242,2334,234))
# print(A)
# print(len(A))
# A.remove("234")
# A.remove((1,242,2334,234))
# A.pop() #random delete 
# print(A)


# a={1,2,3,4,5,5,4}
# b={5,4,3,6,7,8,9,10,10}
# print(a.intersection(b))  #gives me only unique shi matching from those 2 a-b
# dict ={"name":"shiva",
#        "class":"12th"}
# dict={
#       "table":("a wood piece","list and figures"),  #two values of one key
#       "cat":"a small cuTEst animal that i love" }          
# print(dict) 
# subject={"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(subject)  #no duplicates only unique
# print(len(subject))
# marks={}
# marks.update({"phy":132})
# marks.update({"bio":123})
# marks.update({"chm":143})
# print(marks)
# set={("int",9),("float",9.0)}
# print(set)


# x=2
# while x<=10:
#   print("ShivAlone",x)
#   x+=1
# print(x) #we came at 11 by x+1 so it stoped
# s=1
# while s<=10:
#   print(s)
#   s-=1  #going backwards isntead of going upwards
# x=100
# while x>=1:#run this until ah condition
#     print(x)
# #     x-=1
# n=int(input("enter number:"))
# x=1
# while x<=10:  #run until this ah value 
#   print( f"{n} * {x} = " ,n*x )
#   x+=1


# list=[1,4,9,16,25,36,49,64,81,100]
# y=0  #gave it the first index
# while y<len(list):
#   print(list[y])  #every value on y'th index of the list
#   y+=1
# fuits=[0,1,2,3]
# x=0
# while x<len(fuits): #jb tj lenght of fruit less than 4 hai, tb tk fruit ka x'th element print krdo
#   print(fuits[x])
#   x+=1


# list=(1,4,9,16,25,36,49,64,81,100)
# x=81  #ELEMENT to find
# i=0    #initialization
# while i<len(list):
#   if(list[i]==x):
#     print("found at number",i) 
#   i+=1


# i=2
# while i<=6:
#   print(i)
#   if(i==4):
#     break
#   i+=1
    

# i=1
# while i<=10:
#   if(i%2!=0):
#     i+=1
#   print(i)
#   i+=1


# count=5
# while count>=1:
#     print(count)
#     count-=1


# i=10 
# while i>=1: #run this until ah value
#   print(i)
#   i-=1


# i=1
# n=int(input("enter number : "))
# while i<=10:
#   print(n*i)
#   i+=1


# list=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx<len(list):
#   print(list[idx])
#   idx+=1


# mans=("SHiva", "ARohiyt","snkit","vErOn")
# idx=0
# while idx<len(mans):
#   print(mans[idx])
#   idx+=1


# tup=(1,4,9,16,81,36,49,64,81,100)
# x=81
# i=0
# while i<len(tup):
#   if(tup[i]==x):
#     print("found at index",i)
#     break
#   else:
#     print("finding...")
#   i+=1


# i=1
# while i<=7:
#   print(i)
#   if(i==5): #will be getting 5 as output cuz printing is beforehead
#     break
#   i+=1


# i=1
# while i<=10:
#   if(i%2==0): #if even is not%2 then do below
#     i+=1
#   print(i)
#   i+=1


# name="ShivAlone"
# for charr in name:  #this loop will hovour in my string without needing to find lenght
#   if(charr=="A"):   #charr is iterator starts from 0
#     print("A found")
#     break
#   else:
#     print("abi tk nhi mila")


# name="ShivAloneA"
# i=0
# while(i<len(name)):
#   if(name[i]=='A'):
#     print("A found at ",i) #didn't used break after this
#   else :
#     print("finding...")
#   i+=1  #we are getting index in this loop 


# list=[1,4,9,16,25,36,49,64,81,100]
# for element in list:  #khatarnak For-Loop
#   print(element)


# tup=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("enter number:"))
# idx=0
# for num in tup:
#   if(num==x):
#     print("number found at",idx)
#     break
#   elif(num!=x):
#     print("not at this index") 
#   idx+=1  #to get a count of index in for loop, we need external iterator


# for i in range(1,101,1):
#   print(i)


# for m in range(100,0,-1):
#   print(m)


# num=int(input("enter number n :"))
# i=1
# for i in range(1,11):   #by defalut the step is 1 if we don't specify and start is 0(if we don't specify it)
#   print(num*i)


# num=int(input("enter number n :"))
# fac=1
# for i in range(1,num+1):
#   fac*=i
# print("factorial is",fac)


# i=0
# while i<=100:
#   print(i)
#   i+=10


# i=100
# while i>=1:
#   print(i)
#   i-=20


# i=1
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1


# tup=(1,4,9,16,25,36,49,64,81,100)
# for num in tup:
#     if(num==36):
#         print("36 found") 
#         break
#     else:
#         print("finding")


# num=(123,2,3,12,312,3)
# numbertofind=12
# idx=0
# for el in num:
#     if(el==numbertofind):
#         print("x found at",idx)
#         break
#     idx+=1


# for i in range(100,0,-1):
#   print(i)


# for table in range(3):
#     print('ShivStoic')


# n=6
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("total:",sum)


# n=5
# fac=1
# for i in range(1,n+1):
#     fac*=i
# print("fac is :",fac)


# n=5
# fac=1
# i=1
# while i<=n:
#     fac*=i
#     i+=1
# print("faac is:",fac)


# def cal(a,b):   #functions
#     sum=(a-b)
#     print(sum)
#     return sum
# cal(2,3)
# cal(4,1)


# def avg_3(a,b,c):
#     avg=(a+b+c)/3
#     return avg  
# print( avg_3(3,4,4) )
# print( avg_3(2,2,10) )


# def len_list(list): #func will take any list
#     a=len(list) #then cal. it's length
#     print(a)
# num=[23,123,234,45]
# name=["shiv", "gori"]
# len_list(num)   #calling
# len_list(name)


# def nature_func(num):
#     nature=num%2    #finding the remander of given parameter
#     if(nature==0):
#         print("even")
#     else:
#         print("odd")
# nature_func(4)
# nature_func(31)


# def countdown(n):
#     print(n)
#     if(n==0):   #base case, stop when we reach 0
#         return 
#     countdown(n-1)   #think like a multiverse, go deeper and deeper
# countdown(4)


# def countup(n):
#     if(n<0):return  #baseCase
#     countup(n-1)    #it will go deeper and deeper from here until the baseCase got hit
#     print(n)    #then from base case it will start printing
# countup(4)    


# def fact(n):    #recursive function for factorial
#     if(n==1 or n==0):
#         return 1  
#     return fact(n-1)*n    #when it reaches 1 then start filling the values of factorial and calcultion and return them
# print(fact(4))
   

# def sum_n(n):
#     if(n==0):
#         return 0
#     return sum_n(n-1)+n
# print(sum_n(5))


# def cal_sum(a,b):
#     sum=a+b
#     print(sum)
# cal_sum(2,5)


# def cal_sum(a,b):
#   return a+b
# print(cal_sum(2,4))


# def print_hello():
#     print("hello")
# print_hello()


# def total_avg(a,b,c):
#     avg=(a+b+c)/3
#     print(avg)
# total_avg(4,34,43)
# total_avg(1,2,3)


# print("shcs"," ")
# print("ef",end=" ") #prevents linebreak
# def value(a,b=4):
#     print(a*b)
# value(8)    #interpret b automaticly
# value(8*2)  #can add of my own to get out of the default shi


# num=[1,2,3,4,5,6,7]
# def cal_len(list):
#     print(len(list))   
# cal_len(num)


# name=["shiva","rohit","mannat"]
# num=[1,2,3,4,5,6,7]
# def print_val(list):
#     for va in list:
#         print(va,end=" ")
# print_val(name)
# print_val(num)


# def find_fac(n):             
#     fac=1                    
#     for i in range(1,n+1):   
#         fac*=i               
#     print(fac) 
# find_fac(5)
# find_fac(6)


# def convert(usd):
#     inr=usd*66
#     print(usd,"USD =",inr,"INR")
# convert(53)
# convert(100)


# def converter(inr):
#     cad=inr/66
#     print(inr,"Rs =",cad,"Dollars ")
# converter(3498)


# def nature(n):
#     if(n%2==0):
#         print("even")
#     else:
#         print("odd")
# nature(1)
# nature(5)
# nature(2)


# def x(n):
#     if (n==0):
#         return
#     print(n)
#     x(n-1)
# x(5)


# def fact(n):
#     if(n==1 or n==0): 
#         return 1      
#     return fact(n-1)*n
# print(fact(5))


# def cal_sum(n):
#     if(n==0 or n==1):
#         return 0
#     return cal_sum(n-1)+n
# a=cal_sum
# print(a(5))
# print(a(4))


# name=["Shiva","Mannat","Riya"]  #printing these using recursion not loop
# num=[34,345,43,56,45,475] 
# def print_el(list,idx):
#     if(idx==len(list)):  #base case/'till then run' case
#         return 
#     print(list[idx])
#     print_el(list,idx+1)    #recursive   
# print_el(num,3)           #will give me loop till end from this idx that i entered

     
# with open("ss.txt","r") as f:
#     data=f.read()
#     print(data)
# with open("ss.txt","w") as f:
#     data=f.write("replace the fukkin file")
#     print(data)
# with open("ss.txt","a") as f:
#     data=f.write("add this at the end")
#     print(data)
# f=open("sm.txt","a")
# f.write("ja raeeeeeeeee")


# import os
# os.remove(".txt")
# with open("practice.txt",'+a') as f:
#     f.write("Hi everyone\nprograng in Java")
# with open("practice.txt",'r') as f:
#     file=f.read()       
# corrected_file=file.replace("Java",'Python')
# print(corrected_file)


# def check_word(n):
#     with open("practice.txt","r") as f:
#         data=f.readline()
#         if(data.find(n) !=-1):
#             print("found on line ",n)
#         else:
#             print("not found")
# check_word("")   
# check_word("learning")
# check_word("afhfght")


# def check_line():
#     word="like"
#     data=True
#     line_no=1
#     with open("practice.txt",'r') as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1
#         else:
#             print("-1")   
# check_line()


# count=0
# with open("practice.txt","r") as f:
#     data=f.read()
#     num=data.split(",")
#     for val in num:
#         if(int(val)%2!=0):
#             count+=1
# print(count)


# class Names:
#     sharada='Marks:',34
#     riya='Marks:',94
# n1=Names()
# print(n1.sharada)
# n2=Names()
# print(n2)


# class Marks:
#     Shiva=94
#     Gori=97
#     Rohit=87
# M=Marks()
# # M2=Marks()    #can name it anything i want
# # M3=Marks()
# print(M.Shiva)    
# print(M.Gori)
# print(M.Rohit)


# class Student:
#     gender="male"
#     def __init__(self,name,jaat,persentile,status):
#         self.name=name
#         self.jaat=jaat
#         self.persentile=persentile
#         self.status=status
#         print("Database of student in JEE:")
# s1=Student("Shiva","Rajput","68.08","Not qualified")
# print(s1.name,s1.gender,s1.jaat,s1.persentile,s1.status)
# s2=Student("Abhay","Sc","65.76%","Passed")
# print(s2.name,s1.gender,s2.jaat,s2.persentile,s2.status)


# class Player:
#     Game="BGMI"
#     def __init__(self,Name,Age,KD):
#         self.Name=input("enter Name:")
#         self.Age=input("enter Age:")
#         self.KD=input("enter KD:")
#         print("Info of player- ",end=" ")
# P1=Player("Name","Age","KD")
# print(P1.Name,P1.Age,P1.KD,P1.Game)
# P2=Player("Name","Age","KD")   
# print(P2.Name,P2.Age,P2.KD,P2.Game)  


# class Gamers:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def welcome(self,name):
#         print("welcome gamer",self.name,end=" ")  
#     def gam_age(self,age):
#         print("of age",self.age)
# G1=Gamers("shiva",19)
# G1.welcome("name")
# G1.gam_age(19)


# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     @staticmethod   #requires no self statement   
#     def jaat():
#         print("rajput keve")    
#     def find_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#             avg=sum/len(self.marks)
#         print("wassup",self.name,"avg score is:",avg)              
# S1=Student("Shiva",[92,80,82,70])  
# S1.jaat()      
# S1.find_avg()
# S1.name='Alone'
# S1.find_avg()


# class Accout:
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.account_no=acc
#     def debit(self,amount):
#         self.balance-=amount
#         print("Rs.",amount, "was debited")
#         print("total balance:",self.get_balance())
#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs.",amount,"was credited")  
#         print("total balance:",self.get_balance())
#     def get_balance(self):
#         return self.balance     
# A1=Accout(75000,"645343646")
# print(A1.balance)
# print(A1.account_no)
# A1.debit(1000)
# A1.credit(500)
# A1.debit(10000)


# class Super:
#     Gender="Male"
#     def __init__(self,name,power,damage,):
#         self.name=name
#         self.power=power
#         self.damage=damage
#     def welcome(self):
#         print("welcome suckers,",self.name)
#     def daamage(self):
#         return self.damage
# s1=Super("Shiva","Multipower",999999)
# print(s1.name,s1.Gender,s1.power,s1.damage)
# s2=Super("Alone","matured","10000000")
# print(s2.name,s2.power,s2.damage)
# s3=Super("Vyom","macho",99999)
# print(s3.name,s3.Gender,s3.power,s3.damage)
# s1.welcome()
# s2.welcome()
# s3.welcome()
# print(s1.daamage())


# class Account:
#     def __init__(self,balance,acc_no):
#         self.balance=balance
#         self.acc_no=acc_no
#     def credit(self,money):
#         self.balance+=money
#         print("total of",money,"credited to your account")
#         print("totat balance:",self.balance)
#     def debit(self,money):
#         self.balance-=money
#         print("total of",money,"debited to your account")
#         print("totat balance:",self.balance)
#     def present_bal(self):
#         return self.balance                  
# A1=Account(70000,10218234)
# print(A1.balance)
# print(A1.acc_no)        
# A1.credit(500)
# A1.debit(10000)


# class Student:
#     def __init__(self,name):
#         self.name=name
# s1=Student("SHiva")
# print(s1.name)
# del s1.name
# print(s1.name)  #will not get printed cuz it's deleted


# class Account:
#     def __init__(self,no,password):
#         self.no=no
#         self.__password=password    #when we use '__' then this makes it unAccesable
#     def recet(self):              #until i use explicitly this funtion donw below, it will not show the pass
#         print(self.__password)
# acc1=Account("12334","xyz")
# print(acc1.no)
# #print(acc1.__password)    #no direct access, error will pop
# acc1.recet()    #need to run it with external function to view the code


# class Car:
#     color="black"
#     @staticmethod
#     def start():
#         print("car started")
#     def stop(self):
#         print("car stopped")
# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand=brand            
# car1=ToyotaCar("fortuner")
# car2=ToyotaCar("prius")
# print(car2.start())
# print(car1.color)
# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type=type
# car1=Fortuner("diesel")
# car1.start()        
# print(car1.type)


# class A:
#     vA="welcome at A"
# class B:
#     vB="welcome at B"
# class C(A,B):
#     vC="welcome at C"        
# c1=C()
# print(c1.vA)
# print(c1.vB)
# print(c1.vC)


# class Car:
#     def __init__(self,type):
#         self.type=type
#     @staticmethod    
#     def start():
#         print("car started") 
#     def stop(self):
#         print("car stoped") 
# class Toyota(Car):
#     def __init__(self,name,type):
#         super().__init__(type)      #super refers to the parent class
#         self.name=name
# car1=Toyota("fortuner","electic")        
# print(car1.type)
# car1.start()
# car1.stop()
  

# class Person:
#   name="anonymous"
#   def named(self,name):
#     Person.name=name
#     @classmethod   #it modifies the global blueprint
#     def named(cls,name):
#         cls.name=name
# p1=Person()
# p1.named("AloneShiva")
# print(p1.name)        
# print(Person.name)  #see, name is also changed here


# class Student:
#   def __init__(self,phy,chem,math,eng,pe):
#     self.phy=phy
#     self.chem=chem
#     self.math=math
#     self.eng=eng
#     self.pe=pe
#   @property     #now i can't change or assign the value dowm below
#   def percentage(self):
#     return str(((self.phy +self.chem +self.math +self.eng +self.pe)/5))+"%" 
# S1=Student(80,90,80,93,95)
# print(S1.percentage)
# S1.phy=69
# S1.math=74
# S1.eng=91
# S1.pe=95
# S1.chem=84
# print(S1.percentage)


# class Complex:
#   def __init__(self,real,img):
#     self.real=real
#     self.img=img
#   def bothNo(self):
#     print(self.real,"i +",self.img,"j")
#   def __add__(self,num2): 
#     newReal=self.real+num2.real
#     newImg=self.img+num2.img
#     return Complex(newReal,newImg)  
# num1=Complex(2,7)
# num1.bothNo()           
# num2=Complex(4,5)
# num2.bothNo()
# num3=num1+num2
# num3.bothNo()


# class Circle:
#   def __init__(self,radius):
#     self.radius=radius
#   def area(self):
#     return (22/7)*(self.radius*self.radius)
#   def perimeter(self):
#     return (2*22/7)*(self.radius)    
# C1=Circle(21)
# print("the area of circle is:",C1.area(),"and the perimeter is",C1.perimeter())       


# class Employee:
#   def __init__(self,role,salary,department):
#     self.role=role
#     self.department=department
#     self.salary=salary
#   def ShowDetails(self):
#     print("The post is",self.role,"and the salary is Rs",self.salary,"in the",self.department,"department")   
# class Engineer(Employee):
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#     super().__init__("engineer",85000,"IT")   #calls and let's us to access the info from the parent class
# E1=Employee("manager",85000,"IT")
# E1.ShowDetails()
# E2=Engineer("Shiva","17.5")
# E2.ShowDetails()


# class Order:
#   def __init__(self,item,price):
#     self.item=item
#     self.price=price
#   def __gt__(order1,order2):   #this gt is dunder fucntion which means 'greater than' and lhs is greater than i.e order1 a.k.a self
#     return order1.price>order2.price
# order1=Order("chips",40)
# order2=Order("diet",35)        
# print(order1>order2)  #Gives the result in true or false


# class Stu:
#   def __init__(self,name):
#     self.name=name
# s1=Stu("Shiva")
# print(s1.name)        
# del s1.name    #this will get deleted
# s1=Stu("AloneShiv")
# print(s1.name)


# class Account:
#   def __init__(self,acc_no,acc_pass):
#     self.acc_no=acc_no
#     self.__acc_pass=acc_pass  #used '__' that make private shi
#   def recet(self):
#     print(self.__acc_pass)    
# a1=Account(2384743289,13485)
# a1.recet()   #only using this we can acces the pass not else
# print(a1.acc_no)        


# class Car:
#   color="black"
#   @staticmethod   #now 'self' doesn't required
#   def start():
#     print("car started")
#   def stop(self):
#     print('car stopped')
# class Toyota(Car):
#   def __init__(self,name,engine):
#     self.name=name
#     self.engine=engine
# class Fortuner(Toyota):
#   def __init__(self,HP,TyreSize):
#     self.HP=HP
#     self.TyreSize=TyreSize
# T1=Toyota("fortuner","V6")  #added name and engine and since fortuner class inherit everything
# print(T1.name) 
# print(T1.color)
# T1.stop()             
# print(Car.color)
# T2=Fortuner("863","30inch")         
# T2.start()             
# T2.engine='v13'   #can't use values of another classes, only atribute defined we can use
# print(T2.engine)
# print(T2.HP)
# print(T2.TyreSize)


# class A:
#     varA="welcome at A"
# class B:
#     varB="welcome at B"
# class C(A,B):
#     varC="welcome at C"    
# c1=C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)


# class Person:
#   name="anonymous"
#   @classmethod
#   def changeName(self,name):
#     self.name=name
# p1=Person()
# p1.changeName("Shiva")
# print(p1.name)
# a=Person.name   #this means i changed the class's name too
# print(a)


# class Student:
#   def __init__(self,phy,chem,math):
#     self.phy=phy
#     self.chem=chem
#     self.math=math  
#   @property
#   def persentage(self):
#     return str((self.phy+self.chem+self.math)/3)+"%"
# S1=Student(67,76,75)
# print(S1.persentage)
# S1.phy=56  
# print(S1.persentage)        


# class Complex:
#   def __init__(self,real,img):
#     self.real=real
#     self.img=img
#   def shownumber(self):
#     print(self.real,"i +",self.img,"j")
#   def __mul__(self,num2):
#     newREal=self.real*num2.real
#     newImg=self.img*num2.img
#     return Complex(newREal,newImg)
# num1=Complex(3,2)
# num1.shownumber()
# num2=Complex(2,3)
# num2.shownumber()
# num3=num1*num2
# num3.shownumber()

           
# class Employee:
#   def __init__(self,role,department,salary):
#     self.role=role
#     self.department=department
#     self.salary=salary
#   def Showdetails(self):
#     print("the role of tha person is",self.role)
#     print("the department of the person is",self.department)  
#     print("the salary of the person is",self.salary)
# class Enginier(Employee):
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#     super().__init__("enginner","IT",75000)  #using super i can fill info directly to main class
# Number_of_person=int(input("enter the number of person living="))
# engg1=Enginier("SHIva","17")
# engg1.Showdetails()


# class Order:
#   def __init__(self,items,price):
#     self.items=items
#     self.price=price    
#   def __gt__(self,odr2):
#     return self.price>odr2.price
# odr1=Order("PRotien",150)
# odr2=Order("tea",10)
# print(odr1>odr2)



# ------------------------------Projects---------------------------------#


#1.Monthly Rent Calculater

# rent= int(input("Enter your Monthly Room Rent = "))
# food= int(input("Enter your Monthly Groceries Charge = "))
# elec_bill_in_KWh= int(input("Enter Monthly KwH Charge = "))
# charge_perUnit= 5.44
# Number_of_Roomates= int(input("Enter Number of Person Living = "))
# total_bill= elec_bill_in_KWh * charge_perUnit
# output=(food+rent+total_bill)/Number_of_Roomates
# print("You have to Pay Total of Rs",output)





#2.Rock\Paper\Scisors

# import random

# list=["Rock","Paper","Sciser"]    
# user_choice=input("Enter your Fukkin Move Nigga-[Rock-Paper-Sciser]:")
# comp_choice=random.choice(list)    #random is itself a toolkit, seee via doing 'random.' to view all it's features

# print(f'User Chosed={user_choice},Computer Chosed={comp_choice}')

# if user_choice==comp_choice:   #tie case sorted
#   print("It's Tie")

# elif user_choice=="Rock":    #all possibilites for rock by user
#   if comp_choice=="Sciser":
#     print("You Win! and Computer Lost")
#   else:
#     print("You are a Looser dumb nigga, Computer Wins")   #tie is done, Sciser is done above, this one was for papaer

# elif user_choice=="Paper":
#   if comp_choice=="Rock":
#     print("You Win! and Computer Lost")
#   else:
#     print("You loose dumb ass, Computer Wins")

# elif user_choice=="Sciser":
#   if comp_choice=="Paper":
#     print("You Win!,Computer looses")
#   else:
#     print("You Lost and Computer Wins")

 



#3.Digital Clock

# import tkinter as tk    #it's a toolkit for creating GUI application. It include scrollbars,text fields and buttons etc
# from time import strftime   #strftime lives inside the module 'time' it's not the standalone itself, will be using to make the time format

# window=tk.Tk()          #this Tk() is there to create a blank page/screen which act as a background  
# window.title("Clock Clock")    #to give title to my screen(as application name)

# label= tk.Label(              #Label is non-editable poster like on a wall which can hold manny things like text time etc
#                 window,       #Window is the place where all this will be put, rest are styling keys
#                 font=("Helvetica",55,"bold"),
#                 bg='#1e1e24',
#                 foreground="#00f5d4",
#                 cursor="hand2")     #Now our label is done but we havn't puted it on the wall yet
              
# label.pack(anchor="center", padx=30, pady=30)   #this 'pack' put this label we made on that screen and 'anchor' make it on center

# def time():   #making a function to desing the info. 'String Format Time' takes current time and convert it into accesable form using %codes
#   written=strftime("%I : %M  %p  \n  %A, %B %d")  # I-12hour format, M-minutes, P-Am/Pm, A-weekday, B-month, d-date
#   label.config(text=written)    #config joins the label format that we made eirlier to the written(strftime) that we made just now, What it does here it that it updates the text that we made inside the written 
#   label.after(1000,time)     #after makes code to wait for updating, it have it's parameters (how_long_to_wait,what_action_to_do). 1000 is the milisecond that i have to wait for,we put name of the function 'Time' to make it recursion and call itself

# time()
# window.mainloop()   #this mainloops tell python to don't stop here, keep the window open and active on the user's desktop.





#4.Text Editor App

# import tkinter as tk    # messagebox allows us to display quick warning, notification or message as per we want when we do like "messagebox.showinfo/showwarning('Text')" like that.
# from tkinter import filedialog,messagebox   # importing filedialoge allows us to get the access of saving/selecting/viewing of location of the files from local storage 


# root=tk.Tk()    #creating screen
# root.title("Simple Text Editor")    
# root.geometry("800x600")   #resizing it


# text =  tk.Text(     #this is the formating and looks on the frontend
#                 root,
#                 wrap=tk.WORD,   #helps to move autoly down when the edge came
#                 font=("Consolas",17),
#                 bg="black",
#                 fg="white"
#                )
# text.pack(expand=True,fill="both")   #pack places it onto the screeen , vrna it's invisible. #it tells and allows the text box to fit into the whole screen. these parameters just fill the screen 

# options=tk.Menu(root)    #creating a options field(it's a feature of the tkinter that can showcase things to hang on top). Note- it's created not pasted
# root.config(menu=options)    #take that ^invisible 'options' above that we created and snap it physically in the topmost layout that is prexiting in config(menu)


# def new_file():   #we are creating new feature named 'new_file' so we have to check the text box area and delete everything from start to end. that's how we manuplate computer to make a new file
#     text.delete(1.0,tk.END)   #1.text mean all the data that we have inside the main text area | #2.delete takes two parameters(delete_from,till) | #3.this 1.0 is the starting row, this 'tk.End' is the absolute end of the text document

# def open_file():   #so we are again creating a new feature, when we use it then it will open that pop up window of bunch of file location locally and if we don't use the type ourself then it will open every file and text
#     file_path=filedialog.askopenfilename(defaultextension=".txt")    #1.this askopenfile forces our computer to automaticly open that 'open file' popUp window of the file explorer | #2.this defualtextention tells that when i don't select any extention explicitly then make is 'txt' by default
#     if file_path:   #THIS is to check weather user accutaly opened a file, not like he/she just click cancel. Cus after the window popUP we got 2 choices, to open something or to go back and cancel. so this if will only exicutes if they oopend something
#         with open(file_path,"r") as target_file:   #we are opening the existing file and making it readable and preparing it to slam into the editor through the code below
#             text.delete(1.0,tk.END)     #now before inserting we have to make sure that everything from the text editor screen should be clear so we delete everything
#             text.insert(1.0,target_file.read())    #and then we insert(where,what) i.e on firstrow.firstindex paste everthing from that file we selected eirliere. this ".read()" converts every file data into string and then the 'Insert' comes into play and it pastes the whole thing inside our text field

# def save_file():   #so after writing somthing we can go here then this 'saveas' will pop up, then if we saved it then it will create that location and put our whole text data into that location and pop up as message 
#     file_path=filedialog.asksaveasfilename(defaultextension=".txt")   #pop up menu which shows the save option for our existing file
#     if file_path:   #if it's really opened then do this below
#         with open(file_path,"w") as file:   #this makes the file that i saved as writable( it's still empty cuz we made a location yet, not the data )
#             file.write(text.get(1.0,tk.END))    #this 'text.get' gets the text data from start(1.0) till end(of screen) and the write outside will paste the whole data into the empty file that we made
#             messagebox.showinfo("Message","File Saved Successfully")   #directly after that, this message will pop up which contains (title,text) 


# options.add_command(label="New",command=new_file)    #1.options' is where to place the button | #2.add_command creates a clickable button | #3.name of that button | #4.holds the location
# options.add_command(label="Open",command=open_file)
# options.add_command(label="Save",command=save_file)
# options.add_command(label="Exit",command=root.quit)    #premade fucntion is the quit that helped here to quit out of the window completly and exit the programm


# root.mainloop()    #runs forevever in our bg of the window





#5.Number Guess Game

# import random

# print("       =============HELLO MF============== \n       | Welcome to Number Guessing Game |\n|| You have 7 Fukkin Chance to Win a Prizepool ||\n                 |--BE READY--|")

# low=int(input("\nDefine Startion: "))
# high=int(input("Define The End: "))

# print(f"\nYou Got 5 Chances to Guess Between {low} and {high}\n")

# num=random.randrange(low,high)   #The toolkit random have this feature named 'randrange' which helps to randomize and pick a number between a (start,end)
# total_chances=5
# guess_count=0

# while guess_count<total_chances:
#   guess_count+=1
   
#   your_guess=int(input("Enter Your Tukka: "))
    
#   if your_guess==num:
#     print(f"\nCorrect you Jawari !!\nThe Number was {num}.\nYou Made it in {guess_count} Attempts.")
#     break
#   elif guess_count>=total_chances and your_guess!=num:  #situation defined when we ran out of chances
#     print(f"\nYou're out of Chances Dumbass, The Number was {num}")
#   elif your_guess>num:
#     print("Agee nikal gya !\n")
#   else:
#     print("Pecche reh gya !\n")





#Task Organizer

# def task():

#   print("\n\t-----Welome to your Task Book-----")

#   tasks=[]   #created a empty list that will store the elements that we'll enter gradually

#   total_task=int(input("\nEnter the Number of Tasks You Wanna Add = "))
    
#   for i in range(1,total_task+1):   #cuz last one is not included so it's "+1"
#     task_name=input(f"\nEnter task {i} = ")   #takes input till the count of our total task that we entered above and stores in the list
#     tasks.append(task_name)   #this is the part where our task are getting into the list that we made

#   print(f"\nToday's Task : {tasks}")   #this will show the tasks that we entered at one go


#   while True:   #this is for until break statement is there the whole code below will run again and again unless i press 5 cuz that's where break is. if i entered 6 or more or less than 0 the whole shit will work again and again
#     opperation=int(input("\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n"))
    
#     if opperation==1:
#       add=input("\nEnter Task You Wanna Add = ")
#       tasks.append(add)
#       print(f"\n! Task [{add}] Added !")

#     elif opperation==2:
#       update=input("\nEnter task you wanna Change = ")

#       if update in tasks:    #checking if our task that we wanna update is already in the list
#         up=input("Enter Replacement : ")   #replacment is stored in variable named 'up' and we have to switch it
#         ind=tasks.index(update)    #new variable 'ind' will give me that index of the thing we want to replace
#         tasks[ind]=up     #this will set the 'wannaChange' task's index to the 'replacement' task that we entered inside 'up' variable
#         print(f"\nYour Task was Updated as [{up}]")
           
#     elif opperation==3:
#       delete=input("\nEnter task you want to delete = ")

#       if delete in tasks:   #checking if our task that we wanna delete is already in the list, now we if it's in the list then we have to find the location of it
#         ind=tasks.index(delete)   #if it is in the list then make a variable 'ind' and store the index value of that task we wanna delete
#         del tasks[ind]    #then delete that shit
#         print(f"Task [{delete}] has Been Deleted...")

#     elif opperation==4:
#       print(f"\nTotal Task = {tasks}") 

#     elif opperation==5:
#       print("\nClosing Yo Fukkin Program...\n")
#       break

#     else:
#       print("Invaid Number You Dumb")   #this will run infinitly cuz until i reach break statement this will not stop cuz we did 'While(true)'

# task()





#Number Guessing Game(With Hints)    //Nhi Samaj aya:<

# import random

# num=random.randrange(1000,10000)    #it will randomize and give one number between 1000(included) & 9999(included) and store that mystirious value inside this variable that we made
# tries=0

# n=int(input("Guess your fukkin 4 digit number : "))

# if(n==num):
#   print("Great You lucky fella !! It's Right!! ")

# else:
#   while(n!=num):
#     tries+=1
#     count=0
#     n=str(n)      #CONVERTED TO STRING TO CHECK WHICH NUMBERS I GOT RIGHT
#     num=str(num)
#     correct_digit=[]

#     for i in range(0,4):
#       if(n[i]==num[i]):
#         count+=1
#       else:
#         continue  
#       correct_digit.append(n[i])

#     if(count<4) and (count !=0):  #IT doens't shows the digit but the count of how manny numbers i got right
#       print("Not the Number but you got",count,"digits correct")        
#       for k in correct_digit:
#         print(k,end="")
#         print("\n")
#         print("\n")
#         n=int(input("Enter your Next Choice of Numbers:"))

#     elif(count==0):
#       print("None of your hell Numbers you entered match.")
#       n=int(input("Enter Your Next Choice of Numbers:"))

#       if n==num:
#           print("Correct you Sattebazz!! You Gussed Right")





#Computer Quiz

# print("-------------Welcome To My Fukkin Quiz-------------\n")
# playing=input("Do you want to play? : ")

# if playing.lower() != "yes":   #if i enter 'YeS' then this lower will autoly lowerCase that shit
#   quit()   #code below never runs if user print anything rather than 'yes'
 
# print("\n-------------Okayy! Let's play Pussy:)-------------")
# score=0

# answer=input("\nWhat does CPU stands for? : ")
# if answer.lower()=="central processing unit":
#   print("Fukkin correct!!")
#   score+=1
# else:
#   print("Incorect you MF! :(")

# answer=input("\nWho is going to get a high paying job in future? : ")
# if answer.lower()=="shivang manhas":
#   print("hell correct!!")
#   score+=1
# else:
#   print("Wrong you kid..")    

# answer=input("\nIn Which Field do the Shivang Manhas is going to Exel? : ")
# if answer.lower()=="ai and ml":
#   print("Right!")
#   score+=1
# else:
#   print("Not Correct")

# print("\n\nYour Score percentage is ", str((score/3)*100)+"%")    #we are joining this '%' sign together so that's why i need 'str'
# print("You Got " + str(score) + " Questions Right!\n")    #str is cuz when we use + then it should be in string





#Guess Number   //gotta work on finding counts

# import random

# highest_no=input("\nType Highest Number : ")

# if highest_no.isdigit():
#   highest_no=int(highest_no)  

#   if highest_no<=0:
#     print("\nType a Number Larger Than 0 Next Time..")
#     quit()

# else:       #THIS IS FOR if number is any other datatype
#     print("\nPlease Type a Number Next Time..")
#     quit()

# random_number=random.randrange(0,highest_no)   #till the number we entered, it will generate a random number before that number
# guess_no=0

# while True:
#   guess_no+=1
#   your_guess=input("\nMake a fukkin Guess : ")

#   if your_guess.isdigit():
#     your_guess=int(your_guess)   #this thing make sure to converent float into int everytime
#   else:
#     print("\nPlease Type a Number Next Time..")
#     continue

#   if your_guess==random_number:
#     print(f"\nYou Got it Right Under {guess_no} Chances\n")
#     break
#   elif your_guess>random_number:
#     print("You Are Higher!")
#   else:
#     print("You are Lower!")    





#Rock-Paper-Scissor  

# import random

# user_win=0
# comp_win=0
# options=['rock','paper','scissors']

# while True:   #jb tk ander se break na bje tb tk puuchte rho shuru se run krte rho
#   user_input=input("\nChoose between Rock-Paper-Scissors or Q to Quit:").lower()
  
#   if user_input=="q":
#     break
#   if user_input not in options:
#     continue
    
#   random_number=random.randint(0,2)   #runs 3 times(0 1 2)  #rock=0  paper=1  scissor=2
  
#   computer_pick=options[random_number]   # from the 'options' which is our set, use any index(random) and store it in a variable named 'computerChoice'
#   print("\nBoat's Choice : ", computer_pick)
#   print("Your Choice : ", user_input)
#   if user_input==computer_pick:
#     print("\nIts a Tie - Try Again...")

#   elif user_input=="rock" and computer_pick =="scissors":    #now declaring all the win cases from my side so we will declare all the losed cases at once
#     print("\nYou Fukkin Won!!")
#     user_win+=1

#   elif user_input=="paper" and computer_pick=="rock":
#     print("\nYou Fukkin Win!!")
#     user_win+=1

#   elif user_input=="scissor" and computer_pick=="paper":
#     print("You Fukkin Won!!")   
#     user_win+=1

#   else:
#     print("\nYou Lost Dumb Nigga :(")
#     comp_win+=1   
    
# print("\nYOUR WON COUNT : ",user_win)
# print("BOAT WON COUNT : ",comp_win)         

# if user_win>comp_win:
#   print("The Ultimate Winner is YOU")
# elif user_win<comp_win:
#   print("The Ultimate Winner is Boat")
# else:
#   print("It's a Tie\n")

# print("\n...GOOD BYE...\n")



#Hoe Advanture.

# name=input("Type Your Name: ")
# print("WELCOME!",name,"in this Advanture Game.. ")
# answer=input("You are Sleeping..Type 'Wake up' to PLAY or type 'Keep Sleeping' to QUIT ").lower()

# if answer=="wake up":
#   answer=input("Now type 'Open' to OPEN the Door and Go out.. ").lower()
#   if answer=="open":
#     answer=input("Type Car or Bike you want to drive..").lower()
#     if answer=="bike":
#       answer=input("you are going in a bike and found a chick on the way...type 'talk' to TALK with her or type 'Pass by' to ignore ").lower()
#       if answer=="talk":
#         answer=input("She liked you...She is ready to hangout with you...type a location 'Home' or 'Park ").lower()
#         if answer=="home":
#           answer=input("You are at your House...type 'Bed' to go to bed or type 'Washroom' to go to the washroom ").lower()
#           if answer=="bed":
#               answer=input("She's horny for you...type 'Romance' to join her or type 'kill' to kill her.. ").lower()
#               if answer=="romance":
#                 print("You both are kissin each other like crazy!...Game Completed..")
#               elif answer=="kill":
#                 print("You killed her with a Knife...Game Completed..")
#               else:
#                 print("Invalid Input..Game Over")        
#           elif answer=="washroom":
#             answer=input("she is inviting you to bath together..type 'yes' to agree or 'no' to quit ").lower()
#             if answer=="yes":
#               print("You both are unziping your clothes...Game Completed.. ")
#             elif answer=="no":
#               print("kick her Ass out of the House ")
#             else:
#               print("Invalid input..Game Over ")        
#           else:
#             print("Invalid input..Game Over ")                                
#         elif answer=="park":
#           print("You both spend quality time together in the park...Now she's gone.. ")
#         else:
#           print("Invalid input..Game Over ")    
#       elif answer=="pass by":
#         print("you passed away...Game Over:( ")
#       else:
#         print("Invalid Input..Game Over ")     
#     elif answer=="car":
#       answer=input("you are out of gas..type 'Gas' to go to the Gastation ").lower()
#       if answer=="gas":
#         answer=input("you are full of gas..type 'home' to go Home or type 'race' to Race ").lower()
#         if answer=="home":
#           print("Now You reached Home...Part finished... ")
#         elif answer=="race":
#           print("you participated in a race,it will begain in upcoming time..till then wait.. ")
#         else:
#           print("Invalid input..Game Over ")        
#       else:
#         print("Invalid Input..Game Over")
#     else:
#       print("Invalid Input...Game Over")                    
#   else:
#     print("Invalid input ,Game Over ") 
# elif answer=="keep sleeping":
#     print("Bye...Good Night")
#     quit()
# else:
#     print("Not a Valid Input..Try Again")

# print("Thankyou For Playing",name,"GOOD BYE!")






#Password Managment System.

# # from cryptography.fernet import Fernet

# # master_password=input("What is the Master Password? ")

# # def write_key():
# #   key=Fernet.generate_key()
# #   with open("key.key","wb") as key_file:
# #     key_file.write(key)

# def view():
#   with open("password.txt","r") as f:
#     for line in f.readlines():
#       data=line.rstrip()
#       user,password=data.split("|")
#       print("User:",user+"\n"+"Password:",password)

# def add():
#   name=input("ACCOUNT NAME: ")
#   password=input("PASSWORD: ")

#   with open("password.txt","a") as f:
#     f.write(name + "|" + password + "\n")

# while True:
#   mode=input("Would you like to add a new password or view existing once?(add,view),press 'q' to quit ").lower()

#   if mode=="q":
#     break 
#   if mode=="view":
#     view()
#   elif mode=="add":
#     add()
#   else:
#     print("Invalid mode..")
#     continue





#Dice Game    //Tough shit

# import random

# while True:  # this while helps to keep asking to enter right number of players i.e (2-4), otherwise it keeps running until break
#     players = input("Enter the number of players playing (2-4): ")

#     if players.isdigit():
#         players = int(players)

#         if 2 <= players <= 4:  # if user entered right number of players then break from these checks and move on
#             break
#         else:
#             print("Must be between 2-4 players...")

#     else:
#         print("Invalid Number...")


# target_score = 20  # Score needed to win the game

# # Create a list containing one score (0) for every player
# # Example:
# # players = 3  ---> [0, 0, 0] in this each player total will be stored and keep adding on individual columns
# players_scores = [0 for _ in range(players)] #_says that i doesnt' care about variable


# # Continue the game until someone reaches the target score
# while max(players_scores) < target_score:  # compares highest player's score with the target score

#     # Give each player one turn
#     for player_idx in range(players):  # this iterates through every player's turn
#         print("\nPlayer Number", player_idx + 1, "Turn has just Started!")
#         print("Your Total Score is:", players_scores[player_idx], "\n")

#         current_score = 0  # Stores points earned only in THIS turn

#         while True:
#             should_roll = input("Enter (y) to roll: ")

#             if should_roll.lower() != "y":  # if anything except 'y' is entered, end the turn
#                 break

#             value = random.randint(1, 6)

#             if value == 1:  # Threshold: rolling 1 ends the player's turn and loses turn score
#                 print("You rolled a 1! Turn Done...")
#                 current_score = 0
#                 break

#             else:
#                 current_score += value
#                 print("You rolled a:", value)
#                 print("Your current turn score is:", current_score)

#                 # Optional stopping point so player doesn't become too greedy
#                 if current_score >= 30:
#                     print("You reached", current_score)
#                     break

#         # Add this turn's score to the player's total score
#         # Example:
#         # players_scores = [12, 8, 15]
#         # player_idx = 1
#         # current_score = 10
#         # Result -> [12, 18, 15]
#         players_scores[player_idx] += current_score

#         print("Your Total Score is:", players_scores[player_idx])


# # Find the highest score achieved
# winning_score = max(players_scores)

# # Find the index where that highest score exists
# # Example:
# # players_scores = [18, 27, 22]
# # winning_score = 27
# # winning_idx = 1
# winning_idx = players_scores.index(winning_score)

# # +1 because Python starts indexing from 0 while humans count from 1
# print("\n🎉 Player Number", winning_idx + 1,
#       "is the Winner with a Score of:", winning_score)





#Story Maker  //what's wrong in this shi
   
# with open("storu.txt","r") as f:
#   story=f.read()

# words=set()
# start_of_word=-1    

# target_start="<"
# target_end=">"

# for i, char in enumerate(story):
#   if char==target_start:
#     start_of_word=i
#     if char==target_end and start_of_word!=-1:
#       word=story[start_of_word:i+1]
#       words.add(word)
#       start_of_word=-1
                         
# answers={}

# for word in words:
#   answer=input("Enter a Word For"+word+": ")
#   answers[word]=answer

# for word in words:
#   story=story.replace(word,answers[word])             
   
# print(story)





#Timed Math Challenge. GIt Worthy

# import random   #to generate random numbers for calculations
# import time     #to measure and show in how manny seconds you finished

# Signs=["+","-","*"]
# min_opra=2   #this gives us the random number genration startion
# max_opra=10  #so between ^ and this max thing, we will get our numbers randomly

# def generate_prob():
#   left=random.randint(min_opra,max_opra)  #this is understandable i know this
#   right=random.randint(min_opra,max_opra)
#   operators=random.choice(Signs)   #i can also select only one from the list that i passed here using a tool(choice) from our 'random' toolkit

#   expretion=str(left)+""+operators+""+str(right)  #this is nothing but the body and we are conveting it into string cuz we are using '+' and it's just for display so doens't matter
#   answer=eval(expretion)   #this 'eval' i.e evaluate staticly and beforly calculates the answer of each problem after problems got generated through randomint
#   return expretion,answer  #%%%%%%%%%%%%%%%%%%


# print("\n ___________________________________")
# input("\n     Press ENTER to start! ")   #i've written 'input' so i need an 'Enter' to start ts
# print("___________________________________")

# start_time=time.time()  #%%%%%%%%%%%%%%%%%%

# total_prob=5
# wrong=0  #counter for total wrong answer, will desplayed at the end of the quiz with results

# for i in range(total_prob):   #this will simply run 5 times, that means our question will be 5 inTotal
#   expretion,answer=generate_prob()   #%%%%%%%%%%%%%%
         
#   guess=input("\nProblem #"+ str(i+1) +" : "+ expretion +" = ")  #this is nothing but the final body which is counting the problem and right next to it DISPLAYING the problema too  
  
#   if guess==str(answer):  #guess is what user will enter and this asnwer is what we evaluated beforehead of every question
#     print("Correct!")
#   else:       
#     print("Wrong!")
#     wrong+=1             
        
# end_time = time.time() 

# total_time = end_time - start_time        
# print("\n__________________________________\n")
# print("Total Time Taken :",total_time//1,'Sec')  #this '//' makes it it float or single decimal i.e 0
# print("Total Wrong Attempts :",wrong)
# print("___________________________________\n")





#Slot Machine

# import random

# MAx_LINES=3
# MAx_bet=100
# Min_bet=1

# rows=3
# cols=3

# symbol_count={
#     "A":2,
#     "B":4,
#     "C":6,
#     "D":8
# }
# symbol_values={
#     "A":5,
#     "B":4,
#     "C":3,
#     "D":2
# }
# def check_winning(colums,lines,bet,values):
#     winnings=0
#     winnings_line=[]
#     for line in range(lines):
#         symbol=colums[0][line]
#         for column in colums:
#             symbol_check=column[line]
#             if symbol !=symbol_check:
#                 break
#         else:
#             winnings+=values[symbol]*bet 
#             winnings_line.append(line + 1)
#     return winnings,winnings_line


# def get_slot_spin(rows,cols,symbols):
#     all_symbols=[]
#     for symbol,symbol_count in symbols.items():
#         for _ in range(symbol_count):
#             all_symbols.append(symbol)

#     columns=[]
#     for _ in range(cols):
#         column=[]
#         current_symbols=all_symbols[:]
#         for _ in range(rows):
#             value=random.choice(current_symbols)
#             current_symbols.remove(value)
#             column.append(value)
            
#         columns.append(column)    

#     return column    

# def print_machine(column):
#     for row in range(len(column[0])):
#         for i,colu in enumerate(column):
#             if i !=len(column)-1:
#                 print(colu[row],end= " | ")
#             else:
#                 print(colu[row],end="")    
#         print()

# def deposit():
#     while True:
#         amount=input("What would you like to deposit? $")
#         if amount.isdigit():
#             amount=int(amount)
#             if amount>0:
#                 break
#             else:
#                 print("Amount Must be greater than 0.")
#         else:
#             print("Enter Valid Number.")        

#     return amount

# def get_no_lines():
#     while True:
#         lines=input("Enter number of line you want to bet on (1-"+str(MAx_LINES)+")? ")
#         if lines.isdigit():
#             lines=int(lines)
#             if 1<=lines<=MAx_LINES:
#                 break
#             else:
#                 print("Enter Valid number of lines.")
#         else:
#             print("Enter Valid Number.")        

#     return lines

# def get_bet():
#     while True:
#         amount=input("What would you like to BET on each Line? $")
#         if amount.isdigit():
#             amount=int(amount)
#             if Min_bet<=amount<=MAx_bet:
#                 break
#             else:
#                 print(f"Amount Must be betweeen ${Min_bet}-${MAx_bet}.")
#         else:
#             print("Enter Valid Number.")        

#     return amount

# def main():
#     balance=deposit()
#     lines=get_no_lines()
#     while True:
#         bet=get_bet()
#         totol_bet=bet*lines
        
#         if totol_bet>balance:
#             print("You don't have enough to bet that amount,your current balance is:"+"$"+str(balance),)
#         else:
#             break

#     print(f"You are Betting ${bet} on {lines} lines. Total BET is equal to: ${totol_bet}")
    
#     slots=get_slot_spin(rows,cols,symbol_count)
#     print_machine(slots)
#     winnings,wining_line=check_winning(slots,lines,bet,symbol_values)
#     print(f"You Won${winnings}.")
#     print(f"You won on lines:", *wining_line)

# main()





# Turtule game

# import turtle
# import time
# import random

# Width,Height=500,500
# Colors=['red','blue','green','black','cyan','pink','yellow','orange','brown','purple']

# def get_number_of_racers():
#     racers=0
#     while True:
#         racers=input("Enter the number of racers (2-10): ")
#         if racers.isdigit():
#             racers=int(racers)
#         else:
#             print("Invalid input...")  
#             continue

#         if 2<=racers<=10:
#             return racers
#         else:
#             print("Number not in range...")

# def create_turtles(colors):
#     turtle=[]
#     spacingx=Width // (len(colors) + 1)
#     for i,color in enumerate(colors):
#         racer=turtle.Turtle()
#         racer.color(color)
#         racer.shape("turtle")
#         racer.left(90)
#         racer.penup()
#         racer.setpos(-Width//2+(i+1)*spacingx,-Height//2+20)
#         racer.pendown()
#         turtle.append(racer)

# def init_turtule():
#     screen=turtle.Screen()
#     screen.setup(Width,Height)
#     screen.title("Turtule Game")            

# racers=get_number_of_racers()
# init_turtule()

# random.shuffle(Colors)
# colors=Colors[:racers]
# create_turtles(colors)





#WPM Test

# import curses
# from curses import wrapper
# import time
# import random

# def start_screen(stdscr):
#     stdscr.clear()
#     stdscr.addstr("Welcome to the Speed Typing Test You Nigga!\n")
#     stdscr.addstr("\nPress Any key to begin !")
#     stdscr.refresh()
#     stdscr.getkey()

# def display_text(stdscr,target,current,wpm=0):
#     stdscr.addstr(target)
#     stdscr.addstr(1,0,f"WPM:{wpm}")

#     for i,char in enumerate(current):
#         correct_char=target[i]
#         color=curses.color_pair(1)
#         if char!=correct_char:
#             color=curses.color_pair(2)

#         stdscr.addstr(0,i,char,color)

# def load_text():
#     with open("s.txt","r") as f:
#         lines=f.readlines()
#         return random.choice(lines).strip()

# def wpm_test(stdscr):
#     target_text=load_text()

#     current_text=[]
#     wpm=0
#     start_time=time.time()
#     stdscr.nodelay(True)

#     while True:
#         time_elapsed=max(time.time() - start_time,1)
#         wpm=round(len(current_text)/(time_elapsed/60))/5
     
#         stdscr.clear()
#         display_text(stdscr,target_text,current_text,wpm)
#         stdscr.refresh()

#         if "".join(current_text)==target_text:
#             stdscr.nodelay(False)
#             break


#         try:
#             key=stdscr.getkey()
#         except:
#             continue    

#         if ord(key)==27:
#             break

#         if key in ("KEY_BACKSPACE","\b",'\x7f'):
#             if len(current_text)>0:
#                 current_text.pop()
#         elif len(current_text)<len(target_text):        
#             current_text.append(key)

    
# def main(stdscr):
#     curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
#     curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
#     curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)

#     start_screen(stdscr)

#     while True:
#         wpm_test(stdscr)
#         stdscr.addstr(2,0,"You completed the text! Press any key to continue...")
#         stdscr.refresh()
#         key=stdscr.getkey()

#         if ord(key)==27:
#             break

# wrapper(main)    





#Alarm Clock and Timer

# from playsound import playsound
# import time

# Clear="\033[2J"
# clear_return="\033[H"

# def alarm(seconds):
#     time_elapsed=0

#     print(Clear)
#     while time_elapsed<seconds:
#         time.sleep(1)
#         time_elapsed+=1

#         time_left= seconds-time_elapsed
#         minuts_left=time_left//60
#         seconds_left=time_left%60

#         print(f"{clear_return}Alarm will Sound in {minuts_left:02d}:{seconds_left:02d}")

#     playsound("Frozen.mp3")

# minutes=int(input("How manny minutes to wait:"))    
# seconds=int(input("How manny seconds to wait:")) 
# total_seconds=minutes*60+seconds
#alarm(total_seconds)  





#Password Generator

# import random
# import string

# def generate_pass(min_lenght,numbers=True,special_charectors=True):
#   letters=string.ascii_letters
#   digits=string.digits
#   special=string.punctuation

#   charectors=letters
  
#   if numbers:
#     charectors+=digits
#   if special_charectors:
#     charectors+=special

#   pwd=""
#   meets_criteria=False
#   has_number=False
#   has_special=False

#   while not meets_criteria or len(pwd)<min_lenght:
#     new_char=random.choice(charectors)
#     pwd+=new_char

#     if new_char in digits:
#       has_number=True
#     elif new_char in special:
#       has_special=True

#     meets_criteria=True

#     if numbers:
#       meets_criteria=has_number
#     if special_charectors:
#       meets_criteria=meets_criteria and has_special                    
  
#   return pwd

# min_lenth=int(input("Enter theeeeeee minimum Lenght: "))
# has_numbers=input("Do You want to have numbers (y/n)? ").lower()=="y"
# has_special=input("Do you want special cherectors (y/n)? ").lower()=="y"

# pwd=generate_pass(min_lenth,has_numbers,has_special)
# print("the generated password is:",pwd)






# Currency Converter.

# from requests import get
# from pprint import PrettyPrinter

# API="c962a240265c4cd5b02b2c2afb475680"
# Base_Url="https://free.currconv.com/"

# printer=PrettyPrinter()

# def get_currencies():
#     endpoint=f"api/v7/currencies?apiKey={API}"
#     url=Base_Url+endpoint
#     data=get(url).json()

#     printer.pprint(data)

# get_currencies()





#Yt video downloder

# from pytube import YouTube
# import tkinter as tk
# from tkinter import filedialog

# def download_video(url,save_path):
#     try:
#         yt=YouTube(url)
#         streams=yt.streams.filter(progressive=True,file_extension="mp4")
#         highest_res_stream=streams.get_highest_resolution()
#         highest_res_stream.download(output_path=save_path)
#         print("Video Downloded sucess!!")
#     except Exception as e:
#         print(e)

# url="https://youtu.be/2ANwf9FJO3I"
# root=tk.Tk()
# root.withdraw()
# save_path=filedialog.askdirectory()
# download_video(url,save_path)