class Complex:

    def __init__(self,real,img):
        self.real=real
        self.img=img

    def ShowNumber(self):
        print(f"{self.real}i + {self.img}j")

    def __add__(one,two):
        real=one.real+two.real
        img=one.img+two.img
        return Complex(real,img)
    
c1=Complex(3,12)
c2=Complex(-6,-7)
c3=Complex(5,5)

c4=c1+c2+c3
c4.ShowNumber()
