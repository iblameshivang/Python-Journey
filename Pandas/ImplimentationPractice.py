import pandas as pd
import numpy as np

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



# You have a veriable `scores` with 1 column 'runs'.
# Tasks:
# 1. Squeeze it into a 1D Series.
# 2. Replace all NaN values with the median of valid scores.
# 3. Clip scores so no single innings exceeds x & y.
# 4. Count how many innings were between 
# 5. Filter all innings where the batsman scored exactly x,y.
# 6. Categorize innings using `.apply()`:
#    - "Century+" if >= 100
#    - "Regular Score" otherwise


# #           **Answer**          #         
# scores = [99, 49, 118, np.nan, 22, 11, np.nan, np.nan]
# intoseries=pd.Series(scores,name='Runs')  #name will be shown down below, since sereis have only 1 column i.e 1D

# scores = intoseries.fillna(intoseries.median())

# scoreclipped=scores.clip(30,50) #every score before and after both p changes into those p

# countinn=scores.between(20,30).sum()  #adds only true once as 1+1+..

# filterspecific=scores.isin([22,11])

# catogrize=scores.apply(lambda x: 'Century' if x>100 else 'regular shi'



#---------------------------Completed Series-------------------------#


#Challege 1st
# data={
#     'order_id': [101, 102, 103, 104, 105, 106],
#     'city':     ['Delhi', 'Mumbai', 'Delhi', 'Kolkata', 'Mumbai', 'Delhi'],
#     'amount':   [450.0, 1200.5, 300.0, 850.0, 2100.0, 150.5],
#     'status':   ['Delivered', 'Pending', 'Delivered', 'Cancelled', 'Delivered', 'Pending']
# }

# df=pd.DataFrame(data)
# # df.info()
# df.describe()
# df.shape,df.size, df.dtypes

# df['order_id'] = df['order_id'].astype('int32')
# df['city'] = df['city'].astype('category')
# df['status']= df['status'].astype('category')
# #df.info()
# df.values.dtype   #umPy's strict homogeneity constraint forcing heterogeneous columns into object.



# #Challenge 2nd
# import pandas as pd

# import pandas as pd

# data = {
#     'Q1': [150, 200, 120],
#     'Q2': [180, 210, 130],
#     'Q3': [160, 220, 125]
# }
# df = pd.DataFrame(data, index=['Store_A', 'Store_B', 'Store_C'])

# df.sum(axis=1)
# df.mean(axis=1)

# df['Q2']
# type(df['Q2'])

# df[['Q2','Q3']]
# df[['Q2','Q3']]



# #Challenge 3rd
# data = {
#     'Dept': ['HR','IT','Finance','IT'],
#     'Salary': [50,85,70,90],
#     'Rating': [4.2,4.8,3.9,4.5]
# }
# df = pd.DataFrame(data, index=['Emp_101','Emp_102','Emp_103','Emp_104'])

# df.loc['Emp_102']
# df.iloc[1]

# df.loc['Emp_101':'Emp_103']
# df.iloc[0:3]

# df.loc['Emp_102':'Emp_104' , ['Dept','Rating']]
# df.iloc[0:2,1:]



# #Challenge 4th
# data={
#     'City':       ['Delhi', 'Mumbai', 'Delhi', 'Kolkata', 'Delhi', 'Mumbai'],
#     'Driver':     ['Vikram', 'Anil', 'Vikram', 'Suresh', 'Vikram', 'Anil'],
#     'Fare':       [450, 120, 550, 300, 700, 200],
#     'Payment':    ['UPI', 'Cash', 'UPI', 'UPI', 'Cash', 'UPI'],
#     'Completed':  [True, False, True, True, True, False]
# }
# df= pd.DataFrame(data)

# mask1=df['City']=='Delhi'
# mask2=df['Fare']>500
# fmask=mask2 & mask1
# df.loc[fmask,['Driver','Fare']]

# mask1=df['Payment']=='Cash'
# mask2=df['Completed']==False
# fmask=mask1 | mask2
# fmask.sum()

# mask1=df['Payment']=='UPI'
# mask2=df['Completed']==True
# fmask= mask1 & mask2
# (fmask.sum()/mask2.count()) *100 



# #Challenge 5th 
# data = {
#     'Role': ['Data Scientist', 'Backend Dev', 'Fullstack Dev', 'ML Engineer', 'Frontend Dev'],
#     'Skills': ['Python|SQL|AWS', 'Java|Spring|Docker', 'Python|React|Node', np.nan, 'React|CSS|HTML'],
#     'Experience': [3, 5, 2, 4, 1],
#     'Salary_LPA': [14, 18, 11, 16, 8]
# }
# df=pd.DataFrame(data)

# df.dropna(inplace=True)

# df['Primary_Skills'] = df['Skills'].str.split('|').str[0]
# df['Primary_Skills']

# mask1=df['Skills'].str.contains('Python')
# mask2=df['Experience']>=3
# fmask=mask1 & mask2
# df.loc[fmask,['Role','Salary_LPA']]



# #Challenge 6th
# data = {
#     'Team1': ['CSK', 'MI', 'RCB', 'CSK', 'KKR', 'MI'],
#     'Team2': ['MI', 'CSK', 'CSK', 'KKR', 'MI', 'RCB'],
#     'Winner': ['CSK', 'MI', 'CSK', 'KKR', 'MI', 'RCB'],
#     'Margin_Runs': [20, 14, 8, 35, 10, 5]
# }
# df=pd.DataFrame(data)

# def head_to_head(team_a,team_b):
#     a=(df['Team1']==team_a) | (df['Team2']==team_a)
#     b=(df['Team2']==team_b) | (df['Team1']==team_b)
#     return df[a & b]

# rivalry_df=head_to_head('CSK','MI')
# print((rivalry_df['Winner']=='CSK').sum())



#Challenge 7th

# raw_data = {
#     'txn_id': [1001, 1002, 1003, 1004, 1002, 1005, 1006, 1007],
#     'user_id': ['U10', 'U20', 'U30', 'U10', 'U20', 'U40', 'U50', 'U10'],
#     'app': ['PhonePe', 'GPay', 'Paytm', 'PhonePe', 'GPay', 'Paytm', 'GPay', 'PhonePe'],
#     'amount': [500.0, 1200.0, np.nan, 300.0, 1200.0, 4500.0, np.nan, 500.0],
#     'status': ['SUCCESS', 'FAILURE', 'SUCCESS', 'SUCCESS', 'FAILURE', 'SUCCESS', 'PENDING', 'SUCCESS']
# }
# df = pd.DataFrame(raw_data)

# df['amount'].hasnans

# df['app']=df['app'].astype('category')
# df['status']=df['status'].astype('category')
# df['txn_id']=df['txn_id'].astype('int32')

# df.dropna(subset='amount',inplace=True)

# df.duplicated(subset=['user_id','app','amount']).sum()

# df.drop_duplicates(subset=['user_id','app','amount'], keep='last',inplace=True)

# df['user_id'].nunique()

# df['app'].value_counts()



#Challenge 8th
