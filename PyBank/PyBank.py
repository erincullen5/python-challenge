#Import Modules 
import os
import csv

#create path to CSV files
pathCSV_1 = os.path.join("Resources", "budget_data_1.csv")
pathCSV_2 = os.path.join("Resources", "budget_data_2.csv")

path_output_1 = os.path.join("Resources","output_data_1.txt")
path_output_2 = os.path.join("Resources","output_data_2.txt")

#Create function for calculating greatest increase 
def great_inc(csvread):
    global great_inc_rev
    global great_inc_month
    
    great_inc_rev = 0
    great_inc_month = None

    for row in csvread: 
        i = int(row[1])
        if great_inc_rev < i: 
            great_inc_rev = i
            great_inc_month = row[0]
    
    print(f'Greatest Increase in Revenue: {great_inc_month} ,{great_inc_rev}')

def great_dec(csvread):
    
    global great_dec_rev
    global great_dec_month
    
    great_dec_rev = 0
    great_dec_month = None
    for row in csvread: 
        i = int(row[1])
        if great_dec_rev > i: 
            great_dec_rev = i
            great_dec_month = row[0]
    print(f'Greatest Decrease in Revenue: {great_dec_rev} was in {great_dec_month}')


#Creat function for calculating accounting
def run_accounting(csv_path):
    # Read in the CSv
    with open(csv_path, newline='') as csvfile:
        csvread = csv.reader(csvfile, delimiter=",")
        next(csvfile)

        #Create lists for months and revenue
        month_list = []
        revenue = []

        # loop through each row
        csvread = list(csvread) # convert to list instead of generator

        for row in csvread:  

            #add each month to the list month_list 
            month_list.append(row[0])

            #add each revenue to list revenue
            revenue.append(row[1])

        #The final Display
        print("Financial Analysis")
        print("-----------------------------------------------------")

        # The total number of months included in the dataset
        month = (len(month_list))
        print("Total Months: " + str(month))

        # The total amount of revenue gained over the entire period
        revenue  = [ int(x) for x in revenue ]
        total = sum(revenue)
        print("Total Revenue:  " + str(total))

        # The average change in revenue between months over the entire period
        average_change = total/month
        print("Average Revenue Change:  " + str(average_change))

        # The greatest increase in revenue (date and amount) over the entire period
        great_inc(csvread)

        # The greatest decrease in revenue (date and amount) over the entire period
        great_dec(csvread)  

        output = (
            f"\nFinancial Analysis\n"
            f"----------------------------\n"
            f"Total Months: {month}\n"
            f"Total Revenue: ${total}\n"
            f"Average Revenue Change: ${average_change}\n"
            f"Greatest Increase in Revenue: {great_inc_rev} (${great_inc_month})\n"
            f"Greatest Decrease in Revenue: {great_dec_rev} (${great_dec_month})\n")


    with open(path_output_1, "a+") as txt_file:
        txt_file.write(output)

#Run the program functions twice for each CSV Path 
run_accounting(pathCSV_1)
run_accounting(pathCSV_2)