"""
Author: Thinh Mai
Date: 3/17/2020
Purpose: Final Exam - Question 2

"""

#load packages
import datetime
import os
import pandas as pd

#Asking for inputs
"""
takes the following as command line arguments
"""
StartDate = input("Enter the Start Date: ")
EndDate = input("Enter the End Date: ")
folder_path = input("Enter the Folder Path")

#re-use some parts from the in class exercise

fileNameBase = "sales.csv"
Start = None
End = None
ToProcessFileList = []

try:
    Start = datetime.datetime.strptime(StartDate,"%m/%d/%Y")
    End = datetime.datetime.strptime(EndDate,"%m/%d/%Y")
except ValueError as e:
    print(e)
    print("Please Provide a valid start and end data in MM/DD/YYYY format")
    quit()

#using example from class
# subtracting two dates returns a timedelta https://docs.python.org/3/library/datetime.html
# the delta variables .days property below has the number of days between the two dates.
delta = End - Start
date = Start
fileName = None

# we need to include the last day in the list
for i in range (0 , delta.days+1):
    # identify the date for which we need to look for a file
    date = Start + datetime.timedelta(i)

    #creating a function to read file name with format 1 for odd days, 2 for even days
    if date.day % 2:
        nn = 1
    else:
        nn = 2

    # construct the file name inclusive of the path
    # NOTE Filename should be of format mm_dd_YYYY_nn_sales.csv
    fileName = folder_path + "/" + date.strftime("%#m") + "_" + date.strftime("%#d") + "_" + str(date.year) + "_" + str(nn) +"_" + fileNameBase

    # Test if the file exists and if so add it to the ToProcessFileList list.
    if os.path.isfile(fileName) :
        print(fileName)
        ToProcessFileList.append(fileName)

# Process all files in the ToProcessFileList
ConsolidatedDf = None
for file in ToProcessFileList:
    # Read the file using Pandas
    df = pd.read_csv(file)

    if ConsolidatedDf is None:
        # This should be true for the first time
        ConsolidatedDf = df
    else:
        ConsolidatedDf = pd.concat([ConsolidatedDf,df])

#for my specific machine, so I know where the file generated saved at
output_fileName = r'C:\Users\Mai\Downloads\SalesData_Final\Output_File\Consolidated.csv'

# if we found no files to process, ConsolidatedDf will be None, so guard against that
if ConsolidatedDf is not None:
    ConsolidatedDf.to_csv(output_fileName, sep=",", header=True,index=False)

