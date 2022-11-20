#SIDDHARTH TIWARI 2001CE59
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.styles import Alignment,Border,Side
import numpy as np
import os
import re
from datetime import datetime
os.system('cls')
start_time = datetime.now()

def one_inn(inn1,bat_pl,bow_pl,s): #making function for one innings
    innbat = Workbook()
    innfow = Workbook()
    innbow = Workbook()
    s1 = innbat.active
    s2 = innbow.active
    s3 = innfow.active
    s1.column_dimensions['A'].width = 25

    
