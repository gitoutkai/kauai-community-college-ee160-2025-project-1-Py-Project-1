
import csv
import numpy as np
import matplotlib.pyplot as plt

count = 0
headers_row= ""
row= ""
col_index = 'Time(min)', 'Line TC Setpoint(C)', 'Line TC(C)', 'Line Heater(%)', 'Vaporizer TC(C)', 'Vaporizer HeaterTC(C)', 'Vaporizer Heater(%)', 'Vaporizer Scale(lb)', 'Vaporization(lb/h)', 'Powder Feed Setpoint(g/h)', 'Powder Scale(g)', 'Powder Rate(g/h)', 'Chamber TC Setpoint(C)', 'Chamber TC1(C)', 'Chamber TC2(C)', 'Chamber Heater(%)', 'MFC#0', 'MFC#1', 'MFC#2', 'MFC#3', 'ArMFC#1', 'ArMFC#2', 'ArMFC#3', 'XFMR Status', 'Vaccum Pump Outlet TC(C)', 'Vaccum Pump Intlet TC(C)', 'Inlet Valve Open', 'Inlet Valve Closed', 'Outlet Valve Open', 'Outlet Valve Closed', 'MKS Press/Pos', 'MKS Set Point', 'MKS Pressure(Torr)', 'MKS Position(degrees)', 'Injector TC(C)', 'HG-412', 'HG-414', 'HG-416', 'PG-412', 'PG-414', 'PG-416', 'HG-418', 'MTS-414', 'HG-419', 'MH-481', 'MTS-420', 'Vibrator', 'Vibrator2', 'Bell Jar Press(Torr)', 'Exhaust Press(Torr)', 'Run-Time(min)', 'Sub Run-Time(min)'
fullrow= ""
sorted_rows=""
csvfile=""
part_1= []


with open('data11Oct21.csv', 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   for row in csvreader:
       part_1.append(row)
print(len(part_1))


part_1 = part_1[2:]
column_headers = part_1[0]
def part2function():
   column_headers_alpha = sorted(part_1[0])
   print(column_headers_alpha)

part2function()

values=[]
for row in part_1:
   val= row[3]
   values.append(val)
values = values[1:]
#print(values)


def part3function(column_names):
    column_index = [column_headers.index(column_names)][0]
    values=[]
    for row in part_1:
        values.append(row[column_index])

    values = values[1:]
    return values
ans = part3function('Line TC Setpoint(C)')
#print(ans)

#4
def max_partfunction(call_names):
    values= part3function(call_names)
    ans = max(values)
    return ans

def min_partfunction(call_names):
    values= part3function(call_names)
    ans = min(values)
    return ans
#print(max_partfunction("Vaporizer TC(C)"))
#5
def part5function():
    x_time= (part3function("Time(min)"))
    y_time= (part3function("Chamber TC1(C)"))
    plt.plot(x_time, y_time, color='blue')
    plt.show()
part5function()
#6
def part6function():
    x_time= (part3function("Time(min)"))
    y_time= (part3function("Chamber TC2(C)"))
    plt.plot(x_time, y_time, color='blue')
    plt.show()
part6function()

#7 and 8

def part7function(temperature):
    x_time= (part3function("Time(min)"))
    y_time= (part3function(temperature))

    norm_y_temp= []
    y_min = min(y_time)
    y_max = max(y_time)
    for temp in y_time:
        norm_temp= (temp - y_min) / (y_max - y_min)
        norm_y_temp.append(norm_temp)
    plt.plot(x_time, norm_y_temp, color='blue')
    plt.show()
part7function("Chamber TC1(C)")
    
#8
def part8function(temperature1, temperature2):
    y_1= (part3function(temperature1))
    y_2= (part3function(temperature2))
    norm_y_temp1= []
    norm_y_temp2= []
    y_1_min = min(y_1)
    y_1_max = max(y_1)
    y_2_min = min(y_2)
    y_2_max = max(y_2)  
    for temp_1 in y_1:
        norm_temp_1= (temp_1 - y_1_min) / (y_1_max - y_1_min)
        norm_y_temp1.append(norm_temp_1)
    for temp_2 in y_2:
        norm_temp_2= (temp_2 - y_2_min) / (y_2_max - y_2_min)
        norm_y_temp2.append(norm_temp_2)
    plt.scatter(norm_y_temp1, norm_y_temp2)
    plt.show()
part8function("Line TC Setpoint(C)","Vaporizer HeaterTC(C)")
#9
def part9function(temperature1, temperature2):
    y_1= (part3function(temperature1))
    y_2= (part3function(temperature2))
    x_time= (part3function("Time(min)"))
    np_y_temp1= np.array(y_1)
    np_y_temp2= np.array(y_2)
    difference=np_y_temp1-np_y_temp2
    plt.plot(np.array(x_time), difference)
    plt.show()
part9function("Line TC Setpoint(C)","Vaporizer HeaterTC(C)")
#10
def part10function(temperature1, temperature2):
    y_1= (part3function(temperature1))
    y_2= (part3function(temperature2))
    x_time= (part3function("Time(min)"))
    np_y_temp1= np.array(y_1)
    np_y_temp2= np.array(y_2)
    difference=np_y_temp1-np_y_temp2
    plt.plot(np.array(x_time), difference)
    plt.show()
part10function("Vaporizer Heater(%)","Vaporizer HeaterTC(C)")
#function 7 is where the data correllates.

#     csvreader = csv.reader(csvfile)
#     next(csvreader)  # Skip the first row
#     next(csvreader)  # Skip the second row
#     for row in csvreader:
#         if count == 3:
#             headers_row = row
#         count +=1
#     print("headers from row 4:\n", headers_row)

# def get_headers_row(column_headers):
#     with open('data11Oct21.csv', 'r') as csvfile:
#         csvreader = csv.reader(csvfile, delimiter=',')
#         for row in csvfile:
#             if count == 3:
#                 headers_row = row
#         print("headers from row 4:\n", headers_row)


#     return headers_row
# with (open('data11Oct21.csv', 'r') as csvfile):
#     csvreader = csv.reader(csvfile, delimiter=',')
#     x = df['Time(min)'] if 'Time(min)' in df.columns else df.index
#     df[col1].plot(x=x, title=col1)
#     plt.xlabel('Time (min)' if 'Time(min)' in df.columns else 'Index')
#     plt.ylabel(col1)
#     plt.grid(True)
#     plt.show()


# print("hello flynn")
# headers_row = fullrows==[3]
# print("headers from row 4:\n", headers_row)

# with open("data11Oct21.csv", 'r') as csvfile:
#     selected_columns = input("Enter the column names you wish to select:\n")

#     if selected_columns not in headers_row:
#         print("Please enter a valid column name")
#     else:
#         col_index = headers_row.index(selected_columns)
#         print("Selected column name is", headers_row[col_index])
#         print(col_index)

# # part 2
# time= ""
# sorted_headers_row=sorted(headers_row)
# headers_row=""
# row=""
# full_version=""
# csvreader=""

# with open('data11Oct21.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     full_version = list(csvreader)
#     for row in csvfile:
#         if count == 3:
#             headers_row = row
#     print("headers from row 4:\n", sorted_headers_row)
# time= ""
# sorted_headers_row=sorted(headers_row)
# headers_row=""
# row=""
# import pandas as pd
# with open('data11Oct21.csv', 'r') as csvfile:
#     df = pd.read_csv('/Users/kaihehaugoo/Desktop/AA New File/data11Oct21.csv')
# print(df)



# with open('data11Oct21.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=',')
#     fullrows = list(csvreader)
#     for row in csvfile:
#         if count == 3:
#             headers_row = row
#     print("headers from row 4:\n", sorted_headers_row)




# #with open ('data11Oct21.csv', 'r') as ss:
# selected_columns = input("Enter the column names you wish to select:\n")
# if selected_columns not in headers_row:
#     print("Please enter a valid column name")
# else:
#     col_index = headers_row.index(selected_columns)
#     print("Selected column name is", headers_row[col_index])
#     print(col_index)

#     #csv_reader = csv.reader(ss, delimiter=',')
#     #print(ss[::-2])


#     # if co1_index not [x:25):
#     # print("exceeds limits of graph")
#     # else:
#     # sorted_columns=sorted((ʻdata11Oct21.csvʻ), key=lambda row: col_index)
#     # sorted_indicies = np.argsort(-arr[:,1])

# #part 5

# print("End of Part 1")
# print("Thank you CLU")
# print(df.head())
# print(df.info())
# print(df.describe())
# print(type(df))
# import pandas as pd
# df= pd.read_csv('/Users/kaihehaugoo/Desktop/AA New File/data11Oct21.csv')

# for col in df.columns:
#         print(f"- {col}")
# user_input = input("\nWhat column you want to view:\n")
# if user_input in df.columns:
#     print(df[user_input])
#     print(f"\nis da data for column '{user_input}':")
# else:
#     print("you spelled something wrong or the column doesn't exist")
# for col1_2 in df.columns:
#     print(f"- {col1_2}")
# user_input = input("\nWhat two columns do you want to view?\n")
# if user_input in df.columns:
#     print(df[user_input])
#     print(f"\nis da data for column '{user_input}':")
# else:
#     print("you spelled something wrong or the data set doesn't exist")

# for col_t_c in df.columns:
#     print(f"- {col_t_c}")
# user_input = input("\nWhat column you want to view:\n")
# if user_input in df.columns:
#     print(df[user_input])
#     print(f"\nis da data for column '{user_input}':")
# else:
#     print("you spelled something wrong or the column doesn't exist")

# import matplotlib as mpl
# import matplotlib.pyplot as plt
# df = pd.read_csv('data11Oct21.csv')

# print("Chose a column")
# for col in df.columns:
#     print(f"- {col}")

# user_input = input("\nWhat column you want to plot on da graph???:\n")
# if user_input in df.columns:
#     print(f"the info is here", df[user_input])
#     df(user_input).plot(kind='LINE', title=user_input)
#     plt.xlabel('x units')
#     plt.ylabel(user_input)
#     plt.grid(True)
#     plt.show()
# else:
#     print("you spelled something wrong, or the data set doesn't exist. or the master control program is straight buggin")
# #8 Ik its the same code but it should still answer the conparison question because its built off user prompts
# user_input_1 = input("\nWhich temperature you want to plot on da graph???:\n")
# user_input_2 = input("\nWhich temperature you want to plot on da graph???:\n")
# if user_input in df.columns:
#     print(f"the info is here", df[user_input_1])
#     df(user_input_1, user_input_2).plot(kind='LINE', title=user_input_1)
#     plt.xlabel('index')
#     plt.ylabel(user_input_1)
#     plt.grid(True)
#     plt.show()
# else:
#     print("you spelled something wrong, or the data set doesn't exist. or the master control program is straight buggin")

# #9 column #34 is unnormalized data so is column #49
# df= pd.read_csv('/Users/kaihehaugoo/Desktop/AA New File/data11Oct21.csv')
# print(df.columns)

# for var_34 in df.columns:
#     df.doc[var_34] = df.doc[var_34].astype(float)
# for var_49 in df.columns:
#     df.doc[var_49] = df.doc[var_49].astype(float)

# if user_input in df.columns:
#     print(f"the info is here", df[var_34])
#     df(var_34,var_49).plot(kind='LINE', title=var_34)
#     plt.xlabel(var_34)
#     plt.ylabel(var_49)
#     plt.grid(True)
#     plt.show()
# else:
#     print("you spelled something wrong, or the data set doesn't exist. or the master control program is straight buggin. or CLU is straight buggin. on god is tron dead?")

# #10 Ik its the same code but it should still answer the conparison question because its built off user prompts
# user_input_1 = input("\nWhich temperature you want to plot on da graph???:\n")
# user_input_2 = input("\nWhich temperature you want to plot on da graph???:\n")
# if user_input in df.columns:
#     print(f"the info is here", df[user_input_1])
#     df(user_input_1, user_input_2).plot(kind='LINE', title=user_input_1)
#     plt.xlabel('index')
#     plt.ylabel(user_input_1)
#     plt.grid(True)
#     plt.show()
# else:
#     print("you spelled something wrong, or the data set doesn't exist. or the master control program is straight buggin")
