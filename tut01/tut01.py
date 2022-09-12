#function for categorizing the data into different octant 
def oct(x,y,z):
    if x>0:
        if y>0:
            if z>0:
                return 1
            else :
                return -1
        else:
            if z>0:
                return 4
            else :
                return -4
    else:
        if y>0:
            if z>0:
                return 2
            else :
                return -2
        else:
            if z>0:
                return 3
            else :
                return -3


def octact_identification(mod=5000):
    print('a')

#importing pandas
import pandas as pd 

#reading the input file
df = pd.read_csv("octant_input.csv") 

#data pre-prcessing:
df.at[0,'u_avg']=df['U'].mean() 
df.at[0,'v_avg']=df['V'].mean()
df.at[0,'w_avg']=df['W'].mean()

df['U-u_avg']=df['U']-df.at[0,'u_avg']
df['V-v_avg']=df['V']-df.at[0,'v_avg']
df['W-w_avg']=df['W']-df.at[0,'w_avg']

#applying the function made to categorize the data using .apply function
df['octant'] = df.apply(lambda x: oct(x['U-u_avg'], x['V-v_avg'], x['W-w_avg']),axis=1)



mod=5000
octact_identification(mod)