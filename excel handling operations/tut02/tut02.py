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
df = pd.read_excel("input_octant_transition_identify.xlsx") 

#data pre-prcessing:
df.at[0,'u_avg']=df['U'].mean() 
df.at[0,'v_avg']=df['V'].mean()
df.at[0,'w_avg']=df['W'].mean()

df['U-u_avg']=df['U']-df.at[0,'u_avg']
df['V-v_avg']=df['V']-df.at[0,'v_avg']
df['W-w_avg']=df['W']-df.at[0,'w_avg']

#applying the function made to categorize the data using .apply function
df['octant'] = df.apply(lambda x: oct(x['U-u_avg'], x['V-v_avg'], x['W-w_avg']),axis=1)

#leaving an empty column
df[' '] = ''
df[''] = ''
df.at[1,''] = 'user input'

#counting overall using value_counts function
df.at[0,'Octant ID'] = 'overall count'
df.at[0,'1']  = df['octant'].value_counts()[1]
df.at[0,'-1'] = df['octant'].value_counts()[-1]
df.at[0,'2']  = df['octant'].value_counts()[2]
df.at[0,'-2'] = df['octant'].value_counts()[-2]
df.at[0,'3'] = df['octant'].value_counts()[3]
df.at[0,'-3'] = df['octant'].value_counts()[-3]
df.at[0,'4'] = df['octant'].value_counts()[4]
df.at[0,'-4'] = df['octant'].value_counts()[-4]

#input
mod = 5000
df.at[1,'Octant ID']=mod

midoriya = len(df['octant'])
i=0
#using a while loop to split the data in the given range
while(midoriya):
    temp = mod
    
    #for last range we have to take only till last value
    if midoriya<mod:
        mod = midoriya
    x = i*temp
    y = i*temp+mod - 1
    
    #inserting range and their corresponding data
    df.at[i+2,'Octant ID'] = str(x) +'-'+ str(y) 
    
    #making a new dataframe for a choosen range to count octants
    df1 = df.loc[x:y] 

    #counting octant for the taken range and inserting in the cell
    df.at[i+2,'-1'] = df1['octant'].value_counts()[-1]
    df.at[i+2,'1']  = df1['octant'].value_counts()[1]
    df.at[i+2,'-2'] = df1['octant'].value_counts()[-2]
    df.at[i+2,'2']  = df1['octant'].value_counts()[2]
    df.at[i+2,'-3'] = df1['octant'].value_counts()[-3]
    df.at[i+2,'3'] = df1['octant'].value_counts()[3]
    df.at[i+2,'-4'] = df1['octant'].value_counts()[-4]
    df.at[i+2,'4'] = df1['octant'].value_counts()[4]

    i = i + 1
    midoriya = midoriya - mod

#defining a function to get transition count 
def trans_count(df,hue,huehue):
    oki=0
    for i in range(len(df)-1):
        if df.at[i,'octant'] == hue and df.at[i+1,'octant'] ==huehue:
            oki = oki+1
    return oki


yuno = int(len(df)/mod)
df.at[yuno+6,'Octant ID'] = 'Overall Transition Count'
df.at[yuno+7,'Octant ID'] =  'to'
df.at[yuno+8,'1']=  1
df.at[yuno+8,'-1']= -1
df.at[yuno+8,'2']=   2
df.at[yuno+8,'-2']= -2
df.at[yuno+8,'3']=   3
df.at[yuno+8,'-3']= -3
df.at[yuno+8,'4']=   4
df.at[yuno+8,'-4']= -4

df.at[yuno+9,'']= 'From'
df.at[yuno+8,'Octant ID'] = "Count"  
df.at[yuno+9,'Octant ID']=  -4
df.at[yuno+10,'Octant ID']= -3
df.at[yuno+11,'Octant ID']= -2
df.at[yuno+12,'Octant ID']= -1
df.at[yuno+13,'Octant ID']=  1
df.at[yuno+14,'Octant ID']=  2
df.at[yuno+15,'Octant ID']=  3
df.at[yuno+16,'Octant ID']=  4

#calculating overall transition count
for x in range(int(len(df)/mod)+9,int(len(df)/mod)+13):
    for y in range(-4,5) :
            df.at[x,str(y)] = trans_count(df,x-int(len(df)/mod)-13,y)
for x in range(int(len(df)/mod)+13,int(len(df)/mod)+17):
    for y in range(-4,5) :
            df.at[x,str(y)] = trans_count(df,x-int(len(df)/mod)-12,y)
            
            



midoriya = len(df['octant'])
asta=1

#defining a function for mod transition count
def mod_transition_count(df,mod,hue,huehue):
            oki=0
            if mod*asta-1<len(df):
                for i in range(mod*(asta-1),mod*asta-1):
                    if df.at[i,'octant'] == hue and df.at[i+1,'octant'] ==huehue:
                        oki = oki+1
            else:
                for i in range(mod*(asta-1),len(df)-1):
                    if df.at[i,'octant'] == hue and df.at[i+1,'octant'] ==huehue:
                        oki = oki+1
            return oki 
    
mod = 5000
#using a while loop to calculate mod transition count
while(midoriya>0):
   

    if midoriya<mod:
        midoriya=0
       
    df.at[yuno+20+14*asta,'Octant ID'] = 'Mod Transition Count'
    df.at[yuno+21+14*asta,'Octant ID'] =  'to'
    df.at[yuno+22+14*asta,'1']=  1
    df.at[yuno+22+14*asta,'-1']= -1
    df.at[yuno+22+14*asta,'2']=   2
    df.at[yuno+22+14*asta,'-2']= -2
    df.at[yuno+22+14*asta,'3']=   3
    df.at[yuno+22+14*asta,'-3']= -3
    df.at[yuno+22+14*asta,'4']=   4
    df.at[yuno+22+14*asta,'-4']= -4

    df.at[yuno+22+14*asta,'']= str(mod*(asta-1))+"-"+str(mod*asta)
    df.at[yuno+23+14*asta,'']= 'From'
    df.at[yuno+22+14*asta,'Octant ID'] = "Count"  
    df.at[yuno+23+14*asta,'Octant ID']=  -4
    df.at[yuno+24+14*asta,'Octant ID']= -3
    df.at[yuno+25+14*asta,'Octant ID']= -2
    df.at[yuno+26+14*asta,'Octant ID']= -1
    df.at[yuno+27+14*asta,'Octant ID']=  1
    df.at[yuno+28+14*asta,'Octant ID']=  2
    df.at[yuno+29+14*asta,'Octant ID']=  3
    df.at[yuno+30+14*asta,'Octant ID']=  4

    #transition count
    for x in range(int(len(df)/mod)+24+14*asta,int(len(df)/mod)+28+14*asta):
        for y in range(-4,5) :
                df.at[x,str(y)] = mod_transition_count(df,mod,x-int(len(df)/mod)-28-14*asta,y)
    for x in range(int(len(df)/mod)+28+14*asta,int(len(df)/mod)+32+14*asta):
        for y in range(-4,5) :
                df.at[x,str(y)] = mod_transition_count(df,mod,x-int(len(df)/mod)-27-14*asta,y)


    asta = asta + 1
    midoriya = midoriya - mod
    
#saving file
df.to_excel('output_octant_transition_identify.xlsx')
