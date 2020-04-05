# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:03:49 2020

@author: meera
"""

import os
import csv
import statistics

pyBank = os.path.join("../CSV_files/pybank.csv")

months = [] #array
dates = [] #array
dateSplit = "" #string
money = [] #array
diff_list = [] #array
avg = 0.00 #float
max_diff = 0.00 #float
min_diff = 0.00 #float
max_date = "" #string
min_date = "" #string

with open(pyBank, encoding="utf-8") as csvfile:
    bank_reader = csv.reader(csvfile, delimiter=",")
    
    header = next(bank_reader)
    
#    total number of months
    for row in bank_reader:
        dates.append(row[0])
        dateSplit = row[0].split("-")
        months.append(dateSplit[0])   

#    sum of profits and losses 
        money.append(float(row[1]))
       
#        average change 
    for i in range(len(money) - 1):
            diff = money[i+1] - money[i]
            diff_list.append(diff)
            avg = statistics.mean(diff_list)
     
#      max-min difference
            max_diff = max(diff_list)
            min_diff = min(diff_list)
            if diff == max_diff:
                max_date = dates[i]
            else:
                pass
            if diff == min_diff:
                min_date = dates[i]
            else:
                pass
        

    print(f"There are a total of {len(months)} months.")
    print(f"Total amount of money: ${sum(money)}")
    print(f"Average difference of profits: ${avg}")
    print(f"The greatest increase in profits: {max_date} ${max_diff}")
    print(f"The greatest decrease in profits: {min_date} ${min_diff}")
   
        
        
        
  
    
        
    

        
        
        
        
    

        
    
    
