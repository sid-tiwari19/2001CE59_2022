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

    # Creating a dataframe to store to consolidated output.
    DataF3 = pd.DataFrame()
    DataF3['Roll'] = ''
    DataF3['Name'] =''
    for i in range(0, len(v_D)):
        DataF3[v_D[i]] = ''
    DataF3['Actual Lecture Taken'] = ''
    DataF3['Total Real']= ''
    DataF3['% Atd'] = ''

    # Giving structure according to our valid dates stored in the list.
    for i in DataF2.index:
        DataF3.at[i+1, 'Roll'] = DataF2['Roll No'][i]
        DataF3.at[i+1,'Name'] = DataF2['Name'][i]
        DataF3.at[i+1, 'Actual Lecture Taken'] = len(v_D)
        DataF3.at[i+1,'Total Real'] = DataF3.at[i+1, '% Atd']  = 0



    try:
        # Main Loop (iterating for each roll number one by one)
        for i in DataF2.index:

            # A variable dataframe which will store data for every roll number
            DataF4 = pd.DataFrame()
            DataF4['Date'] = ''
            DataF4['Roll'] =''
            DataF4['Name'] = ''
            DataF4['Total Atd Count'] = 0
            DataF4['Real'] = ''
            DataF4['Duplicate'] = ''
            DataF4['Invalid'] = ''
            DataF4['Absent']= ''

            DataF4.at[0,'Roll'] = DataF2['Roll No'][i]
            DataF4.at[0, 'Name'] = DataF2['Name'][i]

            # Writing valid dates in the dataframe
            for j in range(1, len(v_D)+1):
                DataF4.at[j, 'Date'] = v_D[j-1]
                DataF4.at[j, 'Total Atd Count'] = DataF4.at[j, 'Real'] = DataF4.at[j,'Duplicate'] = DataF4.at[j, 'Invalid'] =  DataF4.at[j, 'Absent'] = 0

            # Temporary variable
            Teemp = DataF2['Roll No'][i]

            # Counting Atd according to the given criteria
            for j in DataF.index:
                if(Teemp == DataF['Roll'][j]):
                    if (DataF['Date'][j] != -1):
                        IndeX = v_D.index(DataF['Date'][j])
                        DataF4.at[IndeX+1, 'Total Atd Count'] += 1
                        if (DataF['Time'][j] >= '14:00' and DataF['Time'][j] <= '15:00'):
                            if (DataF4['Real'][IndeX+1] == 0):
                                DataF4.at[IndeX+1, 'Real'] += 1
                            else:
                                DataF4.at[IndeX+1, 'Duplicate'] +=  1
                        else:
                            DataF4.at[IndeX+1, 'Invalid'] += 1

            # Marking absent from the above evaluated Atd.
            for j in range(1, len(v_D)+1):
                if (DataF4['Real'][j] == 0):
                    DataF4.at[j, 'Absent'] = 1
                    DataF3.at[i+1, v_D[j-1]] = 'A'
                else:
                    DataF3.at[i+1, v_D[j-1]] = 'P'
                    DataF3.at[i+1, 'Total Real'] += 1
                DataF3.at[i+1, '% Atd'] = round(DataF3.at[i+1, 'Total Real']* 100 /DataF3.at[i+1, 'Actual Lecture Taken'], 2)



            # Saving the excel file for each roll number.
            DataF4.to_excel('output/'+Teemp+'.xlsx', index=False)
    except:
        print("Index overflow!")

    try:
        
        DataF3.to_excel('output/attendance_report_consolidated.xlsx', index=False)
    except:
        print("Error saving the excel file")


AR()

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))