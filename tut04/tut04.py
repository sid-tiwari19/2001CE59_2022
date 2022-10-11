#SIDDHARTH TIWARI 2001CE59

#importing pandas and numpy
import pandas as pd 
import numpy as np
import os

os.system('cls')

#function for categorizing the data into different octant 
def oct(x,y,z):
    if x>0:
        if y>0:
            if z>0: 
                return 1 #when x,y,z all are positive
            else :
                return -1 #when x,y is positive and z is negative
        else:
            if z>0:
                return 4  #when x,z is positive and y is negative
            else :
                return -4 #when z,y is negative and x is positive
    else:
        if y>0:
            if z>0:
                return 2 #when z,y is positive and x is negative
            else :
                return -2 #when z,x is negative and y is positive
        else:
            if z>0:
                return 3 #when x,y is negative and z is positive
            else :
                return -3 #when x,y,z all are negative


#reading the input file
df = pd.read_excel("input_octant_longest_subsequence_with_range.xlsx") 

#data pre-prcessing:
df.at[0,'u_avg']=df['U'].mean() 
df.at[0,'v_avg']=df['V'].mean()
df.at[0,'w_avg']=df['W'].mean()

df['U-u_avg']=df['U']-df.at[0,'u_avg']
df['V-v_avg']=df['V']-df.at[0,'v_avg']
df['W-w_avg']=df['W']-df.at[0,'w_avg']

#applying the function made to categorize the data using .apply function
df['octant'] = df.apply(lambda x: oct(x['U-u_avg'], x['V-v_avg'], x['W-w_avg']),axis=1)

#making columns for subsequence
df['Octant_no'] = ''
df['Longest Subsequence Length'] = ''
df['Count'] = ''

l = [1,-1,2,-2,3,-3,4,-4] #making a list of all the octants
l1 = df['octant'].tolist()
i=0
for x in l: #finding subsequence for every octant
    df.at[i,'Octant_no'] = x
    count = 1
    temp = 1
    mx = 0
    for y in range(len(l1)-1):
        if x == l1[y] and x == l1[y+1]:
            temp += 1
        else:
            if mx == temp:
                count += 1
            elif mx < temp:
                count = 1
            mx = max(mx,temp)
            temp = 1
    df.at[i,'Longest Subsequence Length'] = mx
    df.at[i,'Count'] = count
    i += 1

