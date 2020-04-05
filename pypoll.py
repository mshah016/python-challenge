# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:06:04 2020

@author: meera
"""

import os
import csv

pyPoll = os.path.join("../pypoll.csv")

votes = 0 #int
candidates = [] #array
unique_candidates = [] #array
num_candidates = 0 #int
candidate_names = "" #string
khan = 0 #int
correy = 0 #int
li = 0 #int
o_tooley = 0 #int
winner = "" #string


with open(pyPoll, encoding="utf-8") as csvfile:
    poll_reader = csv.reader(csvfile, delimiter=",")
    
    header = next(poll_reader)

    for row in poll_reader:
        votes += 1
        candidates.append(row[2])
               
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        else:
            o_tooley += 1
            
        if khan > correy and khan > li and khan > o_tooley:
            winner = "Khan"
        elif correy > khan and correy > li and correy > o_tooley:
            winner = "Correy"
        elif li > khan and li > correy and li > o_tooley:
            winner = "Li"
        elif o_tooley > khan and o_tooley > correy and o_tooley > li:
            winner = "O'Tooley"
        else:
            winner = "null"
        
print("Election Results:")
print("----------------------")
print("The Candidates: " + str(set(candidates)))
print("Total Votes: " + str(votes))
print("----------------------")    
print("Khan: " + str(khan))
print("Correy: " + str(correy))
print("Li: " + str(li))
print("O'Tooley: " + str(o_tooley))
print("----------------------")
print("Winner: " + str(winner))
print("----------------------")
    
    
            
        
    
    
    
        
        