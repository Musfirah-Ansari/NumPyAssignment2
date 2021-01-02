#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# %load C:\Users\zee.j\Downloads\Documents\Python Stuff\Quarter2\Assignments of q2\assign2.py
# Read Instructions carefully before attempting this assignment

# 1) don't rename any function name
# 2) don't rename any variable name
# 3) don't remove any #comment 
# 4) don't remove """ under triple quate values """
# 5) you have to write code where you found "write your code here"
# 6) after download rename this file with this format "PIAICCompletRollNumber_AssignmentNo.py"
#   Example piaic17896_Assignment1.py
# 7) After complete this assignment please push on your own GitHub repository.
# 8) you can submit this assignment through the google form
# 9) copy this file absolute URL then paste in the google form
#  The example above: https://github.com/EnggQasim/Batch04_to_35/blob/main/Sunday/1_30%20to%203_30/Assignments/assignment1.txt

# * Because all assignment we will be checked through software if you missed any above points 
# * then we can't assign your scores in our database.


# In[15]:


import numpy as np


# In[17]:


# Task no 1
def function1():
    # create 2d array from 1,12 range 
    # dimension should be 6row 2 columns  
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
    x =np.arange(1,13).reshape((6,2)) 

    return x

    """
    expected output:
    [[ 1  2]
    [ 3  4]
    [ 5  6]
    [ 7  8]
    [ 9 10]
    [11 12]]
    """    


# In[13]:


x=np.arange(1,13).reshape(6,2)


# In[14]:


x


# In[18]:


# Task2
def function2():
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be satart from 10 and end with 36 (both included)
    # Hint: dtype, reshape 
    
    x = np.arange(1,28,dtype=np.float64).reshape((3,3,3))     
    x= np.arange(10,37,dtype=np.float64).reshape((3,3,3))



    return x
    """
    Expected: out put
array([[[10., 11., 12.],
        [13., 14., 15.],
        [16., 17., 18.]],

       [[19., 20., 21.],
        [22., 23., 24.],
        [25., 26., 27.]],

       [[28., 29., 30.],
        [31., 32., 33.],
        [34., 35., 36.]]])    
    """


# In[19]:


x=np.arange(10,37)


# In[20]:


np.ascontiguousarray(x, dtype=np.float64)


# In[21]:


x = np.arange(10,37,dtype=np.float64).reshape((3,3,3))


# In[22]:


x


# In[23]:


#task3
def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    x = a[(a%5==0) & (a%7==0)]
    return x
    """
    Expected Output:
     [35,  70, 105, 140, 175, 210, 245, 280, 315, 350, 385, 420, 455,
       490, 525, 560, 595, 630, 665, 700, 735, 770, 805, 840, 875, 910,
       945, 980] 
    """ 


# In[24]:


a=np.arange(1, 100*10+1).reshape((100,10))


# In[25]:


x=a[(a%5==0) & (a%7==0)]


# In[26]:


x


# In[28]:



#task4
def function4():
#Swap columns 1 and 2 in the array arr.
   
arr = np.arange(9).reshape(3,3)
  
return arr
"""
Expected Output:
      array([[1, 0, 2],
            [4, 3, 5],
            [7, 6, 8]])
""" 


# In[29]:


arr = np.arange(9).reshape(3,3)


# In[30]:


arr[:,[0, 1]] = arr[:,[1, 0]]


# In[31]:


arr


# In[32]:



#task5
def function5():
#Create a null vector of size 20 with 4 rows and 5 columns with numpy function
   
z =np.zeros(20).reshape(4,5)
  
return z
"""
Expected Output:
      array([[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]])
""" 


# In[33]:


z=np.zeros(20).reshape(4,5)


# In[34]:


z


# In[35]:


#task6
def function6():
    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
   
    arr=np.zeros(10) 
    arr[5]=10
    arr[8]=20
  
    return arr
   


# In[36]:


arr=np.zeros(10)


# In[37]:


arr


# In[39]:



#task7
def function7():
#  Create an array of zeros with the same shape and type as X. Dont use reshape method
x = np.arange(4, dtype=np.int64)
  
return x

"""
Expected Output:
      array([0, 0, 0, 0], dtype=int64)
""" 


# In[40]:


x = np.arange(4, dtype=np.int64)


# In[41]:


x


# In[42]:


np.full_like(x,0)


# In[46]:


#task8
def function8():
    # Create a new array of 2x5 uints, filled with 6.
    
    x = np.full((2,5),6)
  
    return x 


# In[47]:


x = np.full((2,5),6)


# In[48]:


x


# In[50]:



#task9
def function9():
# Create an array of 2, 4, 6, 8, ..., 100.

a = np.arange(2,101,2)
  
return a


# In[51]:


a = np.arange(2,101,2)


# In[52]:


a


# In[55]:



#task10
def function10():
# Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.

arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
brr = np.array([1,2,3])
subt = arr-brr[:,None] 
  
return subt


# In[56]:


arr = np.array([[3,3,3],[4,4,4],[5,5,5]])


# In[57]:


arr


# In[58]:


brr = np.array([1,2,3])


# In[59]:


brr


# In[60]:


subt = arr-brr[:,None] 


# In[61]:


subt


# In[63]:




#task11
def function11():
# Replace all odd numbers in arr with -1 without changing arr.

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
ans = np.where(arr%2!=0,-1,arr)  
  
return ans


# In[64]:


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[65]:


ans = np.where(arr%2!=0,-1,arr)


# In[66]:


ans


# In[68]:



#task12
def function12():
# Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
# HINT: use stacking concept

arr = np.array([1,2,3])
ans = np.r_[np.repeat(arr, 3), np.tile(arr, 3)] 
  
return ans


# In[69]:


arr = np.array([1,2,3])


# In[70]:


np.r_[np.repeat(arr, 3), np.tile(arr, 3)]


# In[72]:


#task13
def function13():
    # Set a condition which gets all items between 5 and 10 from arr.
    
    
    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    ans = arr[(arr>5) & (arr<10)] 
  
    return ans


# In[73]:


arr = np.array([2, 6, 1, 9, 10, 3, 27])


# In[74]:


ans = arr[(arr>5) & (arr<10)]


# In[75]:


ans


# In[77]:


#task14
def function14():
    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
    # Hint use split method
    
    
    arr = np.arange(10, 34, 1) 
    ans = arr.reshape(8,3)
    ans = np.split(ans,[1,3,5,7])  
  
    return ans


# In[78]:


arr = np.arange(10, 34, 1).reshape(8,3)


# In[79]:


arr


# In[80]:


ans = arr.reshape(8,3)


# In[81]:


ans


# In[82]:


ans=np.split(ans,[1,3,5,7])


# In[83]:


ans


# In[85]:



#task15
def function15():
#Sort following NumPy array by the second column


arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
ans = np.sort(arr, axis=0) 
  
return ans


# In[86]:


arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])


# In[87]:


arr


# In[88]:


np.sort(arr, axis=0)


# In[90]:



#task16
def function16():
#Write a NumPy program to join a sequence of arrays along depth.


x = np.array([[1], [2], [3]])
y = np.array([[2], [3], [4]])
ans = np.dstack((x, y)) 
  
return ans


# In[91]:


x = np.array([[1], [2], [3]])
y = np.array([[2], [3], [4]])


# In[92]:


arr = np.dstack((x, y))


# In[93]:


arr


# In[102]:


#Task17 
def function17():
    # replace numbers with "YES" if it divided by 3 and 5
    # otherwise it will be replaced with "NO"
    # Hint: np.where
    arr = np.arange(1,10*10+1).reshape((10,10))
    return np.where([(arr%3 == 0) & (arr%5 == 0)], "YES", "NO")


# In[105]:


arr = np.arange(1,10*10+1).reshape((10,10))


# In[106]:


arr


# In[107]:


ans=np.where((arr%3==0)&(arr%5==0),'YES','NO')


# In[108]:


ans


# In[109]:


#Task18
def function18():
    # count values of "students" are exist in "piaic"
    piaic = np.arange(100)
    students = np.array([5,20,50,200,301,7001])
    x = np.count_nonzero(np.where(students<101))+1
    return x

    #Expected output: 3


# In[110]:


piaic = np.arange(100)


# In[111]:


students = np.array([5,20,50,200,301,7001])


# In[112]:


x=np.count_nonzero(np.where(students<101))+1


# In[113]:


x


# In[114]:


# Task19
def function19():
    #Create variable "X" from 1,25 (both are included) range values
    #Convert "X" variable dimension into 5 rows and 5 columns
    #Create one more variable "W" copy of "X" 
    #Swap "W" row and column axis (like transpose)
    # then create variable "b" with value equal to 5
    # Now return output as "(X*W)+b:

    X = np.arange(1,26).reshape(5,5)
    W = np.copy(x)
    W.T
    b = np.array(5)
    output =(x*W)+b
    return output
    #expected output
    """
    array([[  6,  17,  38,  69, 110],
       [ 17,  54, 101, 158, 225],
       [ 38, 101, 174, 257, 350],
       [ 69, 158, 257, 366, 485],
       [110, 225, 350, 485, 630]])
    """


# In[115]:


x=np.arange(1,26).reshape(5,5)


# In[116]:


x


# In[117]:


W=np.copy(x)


# In[118]:


W


# In[119]:


W.T


# In[120]:


b=np.array(5)


# In[121]:


b


# In[122]:


outPut=(x*W)+b


# In[123]:


outPut


# In[124]:


#Task20
def function20():
    #apply fuction "abc" on each value of Array "X"
    x = np.arange(1,11)
    def abc(x):
        return x*2+3-2

    return x*2+3-2
#Expected Output: array([ 3,  5,  7,  9, 11, 13, 15, 17, 19, 21])
#--------------------------X-----------------------------X-----------------------------X----------------------------X---------------------


# In[125]:


x = np.arange(1,11)


# In[126]:


x*2+3-2


# In[ ]:




