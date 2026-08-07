import numpy as np
#function(used right in the defination of array)

a=np.array([3,4,5,2,6])   #This is the portal that turns normal Python data lists into NumPy data arrays
print(a)
print()


b1=np.zeros(5)            #fills all by 0, it's for future filling value
print(b1)                 #gives array of 5 straight row lenght
print()

b2=np.zeros((4,3))        #4 rows 3 columns or 4 lines and 3 values in each line (No_line,No_value)
print(b2)                 
print()

c1=np.full(5,7)           #it prints any word of our choice, 5 is the lenght(dimention) and 7 is number
print(c1)
print()

c2=np.full((2,3),8)       #this 2,3 is the 2D dimention(2 row 3 colums) that i gave and 8 is the number
print(c2)                 #full function can only print same number in the whole matrix
print()


d1=np.eye(3)              #this is for printing the identity matrix i
print(d1)
print()

d2=np.eye(5)              #it creates same number of rows and columns of our identity matrix
print(d2)
print()


#attributes (used in the ending while printing)

a1=np.array([3,6,2,6,2])
a2=np.array([[1,2,34,5,4,6,2],
            [4,5,3,35,3,6,23],
            [25,62,7,22,6,2,7]])
print(a1.shape,a2.shape)              #prints the number of rows*columns 
print()


b=np.array([[1,2,34,5,4,6,2],
            [4,5,3,35,3,6,23],
            [25,62,7,22,6,2,7]])
print(b.size)                         #prints the total number of elements in the whole array
print()


c1=np.array([1,2,4,5,5])                  #1D array
c2=np.array([ [3,6,2,62,2],[2,2,6,1,2] ])   #2D array
c3=np.array([ [3,3,6,7,2],                #2D array
              [5,2,7,2,7],
              [5,71,61,3,2] ])
c4=np.array([ [ [1,2,34],[25,62,2] ] ])   #3D array
print(c1.ndim,c2.ndim,c3.ndim,c4.ndim)    #prints the number of dimentional a array is
print()


d1=np.array([10,53,42,62,6.3])    
d2=np.array(["wer","rhj"])
d3=np.array([3,2,5])
print(d1.dtype,d2.dtype,d3.dtype)  #print the datatype of the whole array
print()


e=np.array([5.2,52.9,5.9,99.99,0])    #used to change the datatype of array
changetype=e.astype(int)              #can put any datatype in paranthesis that we want to change into
print(changetype)
print()


#mathametical operation

a=np.array([9,16,21])       #IT'S COnvinenet cuz we ddin't need to loop here
print(a+5)   #where a represents all the element of the array so operations are applied on each element
print(a-5)  #after appling it will not save the changes on a, a will remain as it was
print(a*5,a**2,a/2)  #these are also the results of the optrations performend on those element
print()

#aggrigation function

a1=np.sum([[4,4,2],[4,2,5]])     #cal sum of all the elements combined and dimention doesn't matter means all the elements will add and make 1 digit sum
a2=np.sum([[4,5,6,2]])
print(a1,a2)
print()

b1=np.mean([1,2,3,4,5,6,7,8,9,10])     #cal aveage balue of all the elements, matrix doens't matter
b2=np.mean([[1,2,3,4,5],[6,7,8,9,10]])
b3=np.mean([[[1,2,3],[4,5,6],[7,8,9]]])  #i can create any shape but the mean will be of all the values in all those matrices
print(b1,b2,b3)
print()

cdef=np.array([1,2,3,4,5,6,7,8,9,10])
print(np.min(cdef))
print(np.max(cdef))
print(np.std(cdef),np.var(cdef))     #standard devitaion formula is used and variance formula is used  
print()


#indexing and slicing (we got start stop and step in here)

a=np.array([10,20,30,40,50])     #disscussing about start!
print(a[0])    #first elemet value(starts from 0)
print(a[3])
print(a[-1])   #last element value(last starts from -1)

b=np.array([41,52,33,14,95,46])  #last one is not included and it starts from 0 always
print(b[0:3])     #1st elemnt to 2nd(last one doesn't included)
print(b[2:])      #3rd element to  last 
print(b[1:5])      #2nd element to 4th 
print(b[-1])       #last element only, -ve indexing starts from -1
print(b[:-1])       #whole array print
print(b[-4:])        #4th elment from last to last element
print(b[-5:-2])     #last 5th elment to last 3nd element(last one doens't included in rhs)
print()             #now let's talk about step!

print(b[: :2])     #after using (start : stop : step)  we have given last input here only i.e step so it will cover whole array with that step
print(b[: :-1])    #this reverse the whole array cux IT autorecognize that step is -1 so we are going backword and it will also autocovers whole array
print(b[: :-2])    #this will also put values from last into first with 2 steps
print(b[3: :-2])   #this will limit to choose only between first 4 values(starts from 4th reverse to 1st cuz here minus is included) and 2 is the step
print()

print(b[ [0,2,4] ])  #fency indexing,can select and show values using muntiple indexes at once(should store the index of elements in internal list)
print()

print(b[b>40])       #boolian mastering,can add operator condition to get values,this thing is 10x faster than loops
print(b[b>42])        #ALL these things that we did don't work on orignal array ,it works on a copy of orignal
print()


#reshaping 


a=np.array([1,2,3,4,5,6,7,8])    #can make shape ourself of array by entering values of rows,colums out of a normal array
reshaped1=a.reshape(2,4)         #can only reshape if the dimentions matches or are in even. It can convert 1d to 2d and so on and lower order too
reshaped2=a.reshape(4,2)         #this will convert the orignal array into (rows*colums) that we specified
print(reshaped1)                 #so,this reshaping doens't create a copy, it create a view and changes orignal array
print(reshaped2)
print()

b=np.array([  [1,2,5,2,5],
            [32,62,62,72,72],
          [632,623,847,124,141] ])
flatterned=b.flatten()              #it makes a copy and then convets into a stright 1d array
print(flatterned)
 
rAvel=b.ravel()      #it also do the same but now it changes the orignal array, it does't makes a copy
print(rAvel)
print()


#insert

a1D=np.array([23,6,23,27,82,25])     #used to insert a value at an perticular index that i'll enter, this do not change the orignal array 
print(a1D)
NewValInsert=np.insert(a1D, 3, 99 )    #inside paranthesis add (array_name, index_location, dezired_value), this is how we insert the values in 1D array
New2val=np.insert(a1D,5,(44,55))
print(NewValInsert,New2val)        #value got inserted at that entered location and all the other moved one step
print()

a2D=np.array([ [13,21,15,11],     #now for 2d array there's little refinement
               [32,62,61,55] ])
print(a2D)
inserrtt=np.insert(a2D, 1, [1,2,4,3], axis=0 )   #by adding axis,i can make the value- a diffrent array in matrix
i2nserrtt=np.insert(a2D, 2, (0,0,0), axis=None)  #if i enter axis = null then i'll be flattering the whole array and if i totally skip the axis part,then it again wil add values in straight order like 1D array 
print(inserrtt,i2nserrtt)                        #if axis= 0 then it's vertical array stacking, if axis=1 then it's horizontal array stacking 


#append 

appendd1=np.append(a2D, 43)    #append also creates a copy of array and it have only 2 parameters(array_name,value).
ap2=np.append(a2D,[[42,62,762]])
print(appendd1, ap2)           #values always will get added at the end.


#concatination

c1=np.array([1,23,32])        #it adds both the arrays
c2=np.array([12,51,22])        #concatination of array only work if both the arrays who are making out, are of same datatype
conn=np.concatenate((c1,c2))    #have to use (()) paranthesis two times
print(conn)


#delete

d=np.array([1,3,152,51,21])   #Delets the element at perticular index

newd=np.delete(d,0)          #for 1D Array deletion
print(d,newd)

new2=np.delete(d,[1,2,3])    #can delete list of indexes too
print(new2) 


d2=np.array([[1,2,53,5],      #for 2D arary deletion
            [32,6,62,7]])
new3=np.delete(d2, 1, axis=0)     #2nd row will got deleted fully
new4=np.delete(d2, 2, axis=1)     #3rd element of each row's column will got deleted
new5=np.delete(d2, 2, axis=None)   #convert array into flatten and then delete only 2th index value
new6=np.delete(d2, 2)              #if we don't pass axis, then still we will be getting process same as where axis=none
print(new3)
print(new4)
print(new5)
print(new6)
print()


#stacking

a=np.array([1,23,32])       
b=np.array([12,51,22])   

vv=np.vstack((a,b))    #will add both complete array vertically, can use (concatenate+axis=0) here too, same work
hh=np.hstack((a,b))    #will add them in a horizontal row or columnn based, can use (concatenate+axis=1) here too, same work
print(vv)
print(hh)
print()


#split

arr=np.array([23,1,2,35,62,1,1,11])

splitt=np.split(arr,2)     #distribute array into 2 parts
SP2=np.split(arr,4)      #will not work if the array is odd, so element inside array should be even 
print(splitt) 
print(SP2)

d2=np.array([[1,2,53,5],      #for 2D arary split, added more [] in result, andd it will distribute equal number of array each side 
            [32,6,62,7]])
SP3=np.split(d2,2)
print(SP3)
print()


#how numpy is better than looping in a array

prices=[100,200,300,400]  #WE'LL Caclucalte 10percent discout on all array elements using loops and numpy

discount=10
newprice=[]

for price in prices:   #where price starts from first to last element in that array(it's that fukkin 'for loop')
    dd=price-((price/100) * discount)
    newprice.append(dd)

print(newprice)    
print()


discount=20            #by numpy
numPriceListArray=np.array([100,200,300,400])

numpynewprize=numPriceListArray- (numPriceListArray/100) * discount

print(numpynewprize)     #it's faster and short way
print()


#brodcasting

matrix=np.array([[1,2,4],       #brodcaasting expand smaller array to larger array to match them
                 [4,5,6]])
vector=np.array([10,20,30])      #if there were not matching size then there will be error   #this is scaller brodcasting 

add=matrix+vector                #dimentions are matching here in both the array. so it's adding
print(add)
print()

#vectorization

a1=np.array([1,2,4])        #APPLY OPERATION to whole array
a2=np.array([4,5,6])        #IT'S FASTER THAN python loops on lists or array 

addvector=a1+a2
multiple=a1*a2
print(addvector, multiple)


#handling misssing values             #always return boolian value

arr=np.array([1,2,np.nan,4,np.nan,5 ])     # putting missing value in it to experement, nan() used to check if missing value exist or not
print(np.isnan(arr))                       #this isnan() is used to check the position of those missiing value (true is the position and true is defined as yes, missing value is there at that location)

replaceMissing=np.nan_to_num(arr, nan=69)      #this is to replce value, this is it's syntax- np.nan_to_nam(arr_name, nan= replace_val) and if i don't pass this nan=replace then it will fill those by 0 by default
print(replaceMissing)                           #nan- not a number



inn=np.array([4,2,np.inf,4,-np.inf,6])    #putting infinity value inside array to experement on

checkInfinity=np.isinf(inn)     #this returns true on the location where the value is infinity
print(checkInfinity)          #left finite values will be written as true,so it's to check there location

replaceinfinity=np.nan_to_num(inn, posinf= 1000, neginf= -1000)   #in infinity have to pass positiveInfinity=+ve and vise versa for -ve infinity values
print(replaceinfinity)                                             #they will be replaced with their located position
print()



def seprate_num(number):

    number=np.array(number)              #converted all the numbers into array
    even=number[number % 2 == 0]         #store all even numbers
    odd=number[number % 2 != 0]

    return even,odd                     #THAT WAS the function defination part, now let's work on user input


number=list(map(int,input("Enter YOur NUmbers with spaces : ").split()))   #could have also wrote in the starting section
even,odd=seprate_num(number)  #this convert the list above into array and then seprete them also in odds and evens
 
print("\nEven Number : ", even)
print("Odd number :", odd)