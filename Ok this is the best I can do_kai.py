# Kai_Goo_Python_Project_1
# Kaihehau_Goo_Project#1
# I am going to give this my all, I know you told me that Scott and I are the curve, but I refuse to give up
# Let's Go!
# 1 open and print, print number of lines
# file = open('data11Oct22.csv')
# print(file.read())

import csv
import numpy as np
from numpy import log, exp
import matplotlib.pyplot as plt
import time

# new line character ("\n")
# global scope
# print(file.read())
# I added that to see the data
# make variables for the time(min) Chamber TC2(C)
# defining empty list for data matrix to store the variables for question 5 and 6
count = 0
headers_row = ""
row = ""
fullrows = ""
col_index = 'Time(min)', 'Line TC Setpoint(C)', 'Line TC(C)', 'Line Heater(%)', 'Vaporizer TC(C)', 'Vaporizer HeaterTC(C)', 'Vaporizer Heater(%)', 'Vaporizer Scale(lb)', 'Vaporization(lb/h)', 'Powder Feed Setpoint(g/h)', 'Powder Scale(g)', 'Powder Rate(g/h)', 'Chamber TC Setpoint(C)', 'Chamber TC1(C)', 'Chamber TC2(C)', 'Chamber Heater(%)', 'MFC#0', 'MFC#1', 'MFC#2', 'MFC#3', 'ArMFC#1', 'ArMFC#2', 'ArMFC#3', 'XFMR Status', 'Vaccum Pump Outlet TC(C)', 'Vaccum Pump Intlet TC(C)', 'Inlet Valve Open', 'Inlet Valve Closed', 'Outlet Valve Open', 'Outlet Valve Closed', 'MKS Press/Pos', 'MKS Set Point', 'MKS Pressure(Torr)', 'MKS Position(degrees)', 'Injector TC(C)', 'HG-412', 'HG-414', 'HG-416', 'PG-412', 'PG-414', 'PG-416', 'HG-418', 'MTS-414', 'HG-419', 'MH-481', 'MTS-420', 'Vibrator', 'Vibrator2', 'Bell Jar Press(Torr)', 'Exhaust Press(Torr)', 'Run-Time(min)', 'Sub Run-Time(min)'
# linking da col_index to the list of values in that collumn this is where I am stuck
sorted_rows=sorted(fullrows)
time=[]


with open('data11Oct21.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    fullrows = list(csvreader)
    for row in csvfile:
        if count == 3:
            headers_row = row
        count += 1
    print("the number of rows is", count)
    print("hello flynn")
    headers_row = fullrows[3]
    print("headers from row 4:\n", headers_row)

    selected_columns = input("Enter the column names you wish to select:\n")

    if selected_columns not in headers_row:
        print("Please enter a valid column name")
    else:
        col_index = headers_row.index(selected_columns)
        print("Selected column name is", headers_row[col_index])
        print(col_index)

time=[]
time: ""
sorted_headers_row=sorted(headers_row)
headers_row:""
row:""
import pandas as pd
with open('data11Oct21.csv', 'r') as csvfile:
    df = pd.read_csv('/Users/kaihehaugoo/Desktop/AA New File/data11Oct21.csv')
print(df)


with open('data11Oct21.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    fullrows = list(csvreader)
    for row in csvfile:
        if count == 3:
            headers_row = row
    print("headers from row 4:\n", sorted_headers_row)




#with open ('data11Oct21.csv', 'r') as ss:
selected_columns = input("Enter the column names you wish to select:\n")
if selected_columns not in headers_row:
    print("Please enter a valid column name")
else:
    col_index = headers_row.index(selected_columns)
    print("Selected column name is", headers_row[col_index])
    print(col_index)

    #csv_reader = csv.reader(ss, delimiter=',')
    #print(ss[::-2])


    # if co1_index not [x:25):
    # print("exceeds limits of graph")
    # else:
    # sorted_columns=sorted((ʻdata11Oct21.csvʻ), key=lambda row: col_index)
    # sorted_indicies = np.argsort(-arr[:,1])

#part 5

print("End of Line")
print("Thank you TRON")
