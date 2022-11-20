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

    # Concatenating the given data 
    DataF.loc[DataF.Roll == '', 'Roll'] = DataF.Attendance.str.split().str.get(0)
    DataF.loc[DataF.Time == '', 'Time'] = DataF.Timestamp.str.split().str.get(1)
    DataF.loc[DataF.Date == '', 'Date'] = DataF.Timestamp.str.split().str.get(0)
    DataF.loc[DataF.Day == '', 'Day'] = DataF.Date.str.split('-').str.get(0)
    DataF.loc[DataF.Month == '', 'Month'] = DataF.Date.str.split('-').str.get(1)
    DataF.loc[DataF.Year == '', 'Year'] = DataF.Date.str.split('-').str.get(2)

    # (Modays and Thurdays)
    v_D = []
    Dhwaj = ''
    
    # Indexing over the dataframe for getting valid dates, using 'datetime' library for the same.
    for i in DataF.index:
        Dhatt = datetime(int(DataF['Year'][i]), int(DataF['Month'][i]), int(DataF['Day'][i]))
        if (Dhatt.weekday() == 0 or Dhatt.weekday() == 3):
            if (Dhwaj != DataF['Date'][i]):
                v_D.append(DataF['Date'][i])
                Dhwaj= DataF['Date'][i]
        else:
            DataF['Date'][i] = -1

  
    DataF = DataF.sort_values('Roll')

    