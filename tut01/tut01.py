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





mod=5000
octact_identification(mod)