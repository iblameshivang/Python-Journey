import pandas as pd


#---------------------------Series Practice-------------------------#

#PracticeSet 1-----
# marks=pd.Series([78, 91, 64, 91, 55, 83, 72, 91],
#                 index=["Aarav", "Meera", "Kabir", "Diya","Rohan", "Anaya", "Vihaan", "Isha"],
#                 name="Marks")

# #Find How Manny Times each Marks Occureed
# groupbyCount=(marks.value_counts())
# #Find Which marks occur more than once
# highestFre=groupbyCount[groupbyCount>1]
# #How many different marks occurred more than once.
# highestFre.size

# #no of el
# len(marks)
# #dtype
# marks.dtype
# #name
# marks.name
# #Check Weather all val are uniqye
# marks.is_unique
# #its index type
# marks.index.dtype
# #its underlying val
# marks.values

# #Find the names of all students whose marks are above avg
# avgg=marks.mean()
# marks[marks>avgg].index 

# #Student reciving 7 bonus marks. Get the result-> get 100-result 
# marks
# withbonus=marks+7
# 100-withbonus

# #Find the toper and return all of it's rows
# marks[marks==marks.max()]  #sick

# #find all students who scored above 70, sort them from desc and return top 3
# marks[marks>70].sort_values(ascending=False).head(3)



# #PracticeSet 2-----
# orders = pd.Series(
#     ["Laptop", "Mouse", "Keyboard", "Mouse",
#      "Monitor", "Laptop", "Mouse", "Keyboard",
#      "Laptop", "Headphones", "Mouse"],
#     name="Product")

# #Find all orders where the product is either: "Laptop" "M onitor"
# orders[ orders.isin(["Laptop","Monitor"]) ]  #using 'isin' 
# orders[(orders == "Laptop") | (orders == "Monitor")]  #without func

# #find the frequency of every product->which was ordered most->return it's name & count
# group=orders.value_counts()
# most=group.idxmax()  #gives the idx atacched to the largest val
# most,group.max() #finished
# group[group == group.max()] #this jumps the last step at once 

# #check whether 'webcam' exists in the series then check for 'Mouse'
# 'webcam' in orders.values #checks for indexes bydefault 
# "Mouse" in orders.values

# #Create a new sereis contianing the same data but in the reverse order
# orders[ orders.size::-1 ]
# orders[-1::-1]



# #PracticeSet 3-----
# salary = pd.Series(
#     [42000, 58000, 51000, 73000, 46000, 91000, 67000],
#     index=["E01", "E02", "E03", "E04", "E05", "E06", "E07"],
#     name="Salary"
# )

# #Find Emp whose salary is >= 60000
# salary.index[salary>=60000]
# #Sort salries desc and retrive 3 highest
# salary.sort_values(ascending=False).head(3)
# #Cal how much salary each employee is short of 100000(keep all data)
# 100000-salary



# #PracticeSet 4-----
# visits = pd.Series(
#     [120, 85, 240, 175, 90, 310, 150],
#     index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
#     name="Visits"
# )

# #find the days on which visits werre >100 & <250, return full row
# visits[ (visits>100) & (visits<250) ]
# #retrive the visits from wed to sat
# visits["Wed":"Sat"]





#---------------------------Completed Series-------------------------#