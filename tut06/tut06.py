#SIDDHARTH TIWARI 2001CE59

import pandas as pd
import os
from datetime import datetime
start_time = datetime.now()

os.system('cls')

def AR():

    try:
  
        DataF =pd.read_csv('input_attendance.csv')
        DataF2 =pd.read_csv('input_registered_students.csv')
    except:
        print("Errorin reading the file.")

    # Adding empty columns 
    DataF['Roll'] = ''
    DataF['Time'] =''
    DataF['Date'] = ''
    DataF['Day'] = ''
    DataF['Month'] =''
    DataF['Year'] = ''

 