#Siddharth Tiwari 2001CE59
import openpyxl
wb = openpyxl.load_workbook(r'input_octant_longest_subsequence.xlsx')
st = wb.active
rcount=st.max_row
total_count=rcount-1

#List storing octant signs
lis = [1, -1, 2, -2, 3, -3, 4, -4]

