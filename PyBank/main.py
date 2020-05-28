import os
import csv

PyBankDatacsv = r"C:\Users\megan.moroney\Desktop\python-challenge\PyBank\Resources\PyBank_budget_data.csv"

months = 1
profittotal = 0
profitchange = 0
profitstart = 0
profit = []
changemonthly = []
date = []
profitchangelist = []
with open(PyBankDatacsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    csvhead = next(csvreader)
    firstrow = next(csvreader)
    profitchange += int(firstrow[1])
    profitstart = int(firstrow[1])
    profittotal = profitchange
    for row in csvreader:
        months = months + 1
        date.append(row[0])
        profit.append(row[1])
        profittotal = profittotal + int(row[1])
        print( "Profittotal line 34 is =", profittotal)
        profitend = int(row[1])
        changemonthly_profit = profitend - profitstart
        changemonthly.append(changemonthly_profit)
        profitchange = profitchange + changemonthly_profit
        print( "profitchange line 41 is =", profitchange)
        profitstart = profitend
        profitchangelist.append(changemonthly_profit)
        print(profitchangelist)
        maxincrease_profits = max(changemonthly)
        maxdecrease_profits = min(changemonthly)
        maxincreasedate = date[changemonthly.index(maxincrease_profits)]
        maxdecreasedate = date[changemonthly.index(maxdecrease_profits)]
    profitchange_average = round((sum(profitchangelist)/len(profitchangelist)), 2)
    print(f'Financial Analysis')
    print(f'-------------------------------------------')
    print(f'Total Months: {months}')
    print(f'Total: ${profittotal}')
    print(f'Average Change: ${profitchange_average}')
    print(f'Greatest Increase in Profits: {maxincreasedate} (${maxincrease_profits})')
    print(f'Greatest Decrease In Profits: {maxdecreasedate} (${maxdecrease_profits})')
financialanalysis = os.path.join("PBResults.txt")
with open(financialanalysis, 'w') as txtfile:
        txtfile.write('Financial Analysis')
        txtfile.write('\n------------------------------------')
        txtfile.write(f'\nTotal Months: {months}')
        txtfile.write(f'\nTotal: ${profittotal}')
        txtfile.write(f'\nAverage Change: ${profitchange_average}')
        txtfile.write(f'\nGreatest Increase In Profits: {maxincreasedate} (${maxincrease_profits})')
        txtfile.write(f'\nGreatest Decrease In Profits: {maxdecreasedate} (${maxdecrease_profits})')