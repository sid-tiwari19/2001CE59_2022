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

    #coding dynamically based on each line
    while True:
        t = inn1.readline()
        if not t:
            break
        crun = 0
        cex = 0
        ov = over.findall(t)
        if float(ov[0]) == int(float(ov[0])) + 0.6:
            ov[0] = str(int(float(ov[0]))+1)
        if float(ov[0])== int(float(ov[0])) + 0.1:
            orun = runs
        nnnb = no_ball.findall(t)
        wbb = wide.findall(t)
        sr = single.findall(t)
        zr = zero.findall(t)
        by = byes.findall(t)
        lby = lbyes.findall(t)
        pl = player.finditer(t)
        w2 = wide2.findall(t)
        w3 = wide3.findall(t)
        for i in pl:
            cbow = i.group(2)
            cbat = i.group(4)
        r = 1
        for col in s1.iter_cols(min_col=1,max_col = 1):
            for cell in col:
                if  cell.value == bat_pl[cbat]:
                    crow = cell.row
                    r = 0
                    break
        if r:
            s1.append([bat_pl[cbat],'not out','','','',0,0,0,0,0])
            crow = s1.max_row

        s = 1
        for col in s2.iter_cols(min_col=1,max_col = 1):
            for cell in col:
                if  cell.value == bow_pl[cbow]:
                    cbrow = cell.row
                    s = 0
                    break
        if s:
            s2.append([bow_pl[cbow],'','',0,0,0,0,0,0,0])
            cbrow = s2.max_row

        