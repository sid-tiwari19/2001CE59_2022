#SIDDHARTH TIWARI 2001CE59

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

#ounting overall using value_counts function
df.at[0,'octant ID'] = 'overall count'
df.at[0,'-1'] = df['octant'].value_counts()[-1]
df.at[0,'1']  = df['octant'].value_counts()[1]
df.at[0,'-2'] = df['octant'].value_counts()[-2]
df.at[0,'2']  = df['octant'].value_counts()[2]
df.at[0,'-3'] = df['octant'].value_counts()[-3]
df.at[0,'3'] = df['octant'].value_counts()[3]
df.at[0,'-4'] = df['octant'].value_counts()[-4]
df.at[0,'4'] = df['octant'].value_counts()[4]

