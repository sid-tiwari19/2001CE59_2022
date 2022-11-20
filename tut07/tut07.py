#SIDDHARTH TIWARI 2001CE59
from datetime import datetime
start_time = datetime.now()
import openpyxl
from openpyxl.styles import Color, PatternFill, Font, Border, Side
import glob
import os
os.system("cls")







o_s = [1,-1,2,-2,3,-3,4,-4]
onim = {1:"Internal outward interaction", -1:"External outward interaction", 2:"External Ejection", -2:"Internal Ejection", 3:"External inward interaction", -3:"Internal inward interaction", 4:"Internal sweep", -4:"External sweep"}
yellow = "00FFFF00"
yellow_bg = PatternFill(start_color=yellow, end_color= yellow, fill_type='solid')
black = "00000000"
double = Side(border_style="thin", color=black)
black_border = Border(top=double, left=double, right=double, bottom=double)




#Code
def rc(count):
    for item in o_s:
        count[item] = 0

# Method to initialise dictionary with 0 for "o_s" except 'left'
def rce(count, left):
    for item in o_s:
        if(item!=left):
            count[item] = 0

def sf(longest, frequency, outs):
    # Iterating "o_s" and updating sheet
    for i in range(9):
        for j in range(3):
            outs.cell(row = 3+i, column = 45+j).border = black_border

    outs.cell(row=3, column=45).value= "Octant ##"
    outs.cell(row=3, column=46).value= "Longest Subsquence Length"
    outs.cell(row=3, column=47).value= "Count"

    for i, label in enumerate(o_s):
        cR = i+3
        try:
            outs.cell(row=cR+1, column=45).value = label	
            outs.cell(column=46, row=cR+1).value = longest[label]
            outs.cell(column=47, row=cR+1).value = frequency[label]
        except FileNotFoundError:
            print("File not found!!")
            exit()






# Method to set time range for longest subsequence
def longest_subsequence_time(longest, frequency, tr, outs):
    # Naming columns number
    lengthCol = 50
    freqCol = 51
    
    # Initial row, just after the header row
    row = 4

    outs.cell(row=3, column = 49).value = "Octant ###"
    outs.cell(row=3, column = 50).value = "Longest Subsquence Length"
    outs.cell(row=3, column = 51).value = "Count"

    # Iterating all octants 
    for octant in o_s:
        try:
            # Setting octant's longest subsequence and frequency data
            outs.cell(column=49, row=row).value = octant
            outs.cell(column=lengthCol, row=row).value = longest[octant]
            outs.cell(column=freqCol, row=row).value = frequency[octant]
        except FileNotFoundError:
            print("File not found!!")
            exit()

        row+=1

        try:
            # Setting default labels
            outs.cell(column=49, row=row).value = "Time"
            outs.cell(column=lengthCol, row=row).value = "From"
            outs.cell(column=freqCol, row=row).value = "To"
        except FileNotFoundError:
            print("File not found!!")
            exit()

        row+=1

        # Iterating time range values for each octants
        for td in tr[octant]:
            try:
                # Setting time interval value
                outs.cell(row=row, column=lengthCol).value = td[0]
                outs.cell(row=row, column=freqCol).value = td[1]
            except FileNotFoundError:
                print("File not found!!")
                exit()
            row += 1

    for i in range(3, row):
        for j in range(49, 52):
            outs.cell(row=i, column = j).border = black_border



# Method to set frequency count to sheet
			
def fls(outs, t_c):
	# Dictionary to store consecutive sequence count
    count = {}

    # Dictionary to store longest count
    longest = {}

    # Initialing dictionary to 0 for all labels
    rc(count)
    rc(longest)

    # Variable to check last value
    last = -10

    # Iterating complete excel sheet
    for i in range(0, t_c):
        cR = i+3
        try:
            crnt = int(outs.cell(column=11, row=cR).value)

            # Comparing current and last value
            if(crnt==last):
                count[crnt]+=1
                longest[crnt] = max(longest[crnt], count[crnt])
                rce(count, crnt)
            else:
                count[crnt]=1
                longest[crnt] = max(longest[crnt], count[crnt])
                rce(count, crnt)
        except FileNotFoundError:
            print("File not found!!")
            exit()

        # Updating "last" variable
        last = crnt

    # Method to Count longest subsequence frequency
    clsff(longest, outs, t_c)




def clsff(longest, outs, t_c):
    # Dictionary to store consecutive sequence count
    c = {}

    # Dictionary to store frequency count
    fq = {}

    # Dictionary to store time range
    tr = {}

    for l in o_s:
        tr[l] = []

    # Initialing dictionary to 0 for all labels
    rc(c)
    rc(fq)

    # Variable to check last value
    last = -10

    # Iterating complete excel sheet
    for i in range(0, t_c):
        cR = i+3
        try:
            crnt = int(outs.cell(column=11, row=cR).value)
            
            # Comparing current and last value
            if(crnt==last):
                c[crnt]+=1
            else:
                c[crnt]=1        
                rce(c, crnt)

            # Updating freq
            if(c[crnt]==longest[crnt]):
                fq[crnt]+=1

                # Counting starting and ending time of longest subsequence
                end = float(outs.cell(row=cR, column=1).value)
                start = 100*end - longest[crnt]+1
                start/=100

                # Inserting time interval into map
                tr[crnt].append([start, end])

                # Resetting count dictionary
                rc(c)
            else:
                rce(c, crnt)
        except FileNotFoundError:
            print("File not found!!")
            exit()
        except ValueError:
            print("File content is invalid!!")
            exit()

        # Updating 'last' variable
        last = crnt

    # Setting fq table into sheet
    sf(longest, fq, outs)

    # Setting time range for longest subsequence
    longest_subsequence_time(longest, fq, tr, outs)








def tcf(row, T_c, outs):
    # Setting hard coded inputs
    try:
        outs.cell(row=row, column=36).value = "To"
        outs.cell(row=row+1, column=35).value = "Octant #"
        outs.cell(row=row+2, column=34).value = "From"

        for i in range(35, 44):
            for j in range(row+1, row+1+9):
                outs.cell(row=j, column = i).border = black_border

    except FileNotFoundError:
        print("Output file not found!!")
        exit()
    except ValueError:
        print("Row or column values must be at least 1 ")
        exit()

    # Setting Labels
    for i, label in enumerate(o_s):
        try:
            outs.cell(row=row+1, column=i+36).value=label
            outs.cell(row=row+i+2, column=35).value=label
        except FileNotFoundError:
            print("Output file not found!!")
            exit()
        except ValueError:
            print("Row or column values must be at least 1 ")
            exit()

    # Setting data
    for i, l1 in enumerate(o_s):
        maxi = -1

        for j, l2 in enumerate(o_s):
            val = T_c[str(l1)+str(l2)]
            maxi = max(maxi, val)

        for j, l2 in enumerate(o_s):
            try:
                outs.cell(row=row+i+2, column=36+j).value = T_c[str(l1)+str(l2)]
                if T_c[str(l1)+str(l2)] == maxi:
                    maxi = -1
                    outs.cell(row=row+i+2, column=36+j).fill = yellow_bg
            except FileNotFoundError:
                print("Output file not found!!")
                exit()
            except ValueError:
                print("Row or column values must be at least 1 ")
                exit()





