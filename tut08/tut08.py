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

    #scorecard and index
    s1['A1'] = s + ' Innings'
    s1['I1'] = '0-0'
    s1['J1'] = '0 overs'
    s1['A2'] = 'Batter'
    s1['F2'] = 'R'
    s1['G2'] = 'B'
    s1['H2'] = '4s'
    s1['I2'] = '6s'
    s1['J2'] = 'SR'

    s2['A1'] = 'Bowler'
    s2['D1'] = 'O'
    s2['E1'] = 'M'
    s2['F1'] = 'R'
    s2['G1'] = 'W'
    s2['H1'] = 'NB'
    s2['I1'] = 'WD'
    s2['J1'] = 'ECO'

    s3['A1'] = 'Fall of wickets'
    
    #using regex
    over = re.compile(r'(\d\d?\.\d)')
    zero = re.compile(r'no run')
    no_ball = re.compile(r', (no ball),')
    wide = re.compile(r', wide,')
    wide2 = re.compile(r', 2 wides,')
    wide3 = re.compile(r', 3 wides,')
    single = re.compile(r', 1 run,')
    six = re.compile(r', SIX,')
    four = re.compile(r', FOUR,')
    byes = re.compile(r', (byes),')
    lbyes = re.compile(r', (leg byes),')
    double = re.compile(r', 2 runs,')
    triple = re.compile(r', 3 runs,')
    out = re.compile(r', out')
    player = re.compile(r'(\d\d?\.\d) (\w+) (to|\w+ to) (\w+)( \w+)?,')
    caught = re.compile(r', out Caught by (\w+)')
    lbw = re.compile(r', out Lbw!!')
    bowled = re.compile(r', out Bowled!!')
    run_out = re.compile(r'Run Out!! ')
    runs = 0
    wickets = 0
    nb = 0
    nlb = 0
    nw = 0
    nnb = 0
    ppr = 0

    