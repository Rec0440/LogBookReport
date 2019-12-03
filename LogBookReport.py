"""
план виконання завдання:
юзер запускає прогу у директорії де знаходиться шуканий excel-workbook,
у разі відсутності файлу з назвою по замовчуванню, юзер вводить назву файлу, що треба обробити
юзер вказує за який період необхідно провести обрахунки, в роках.
програма проводить обрахунки,
результат роботи додається, як worksheet в кінець workbook
"""
from Report import Report
from FlightTime import FlightTime

# testing
FileName = 'PILOT_LOG_532.xlsx'
wb = Report(FileName)
print('Start application at: ' + str(wb.ExecutionTime) + '\n')

# collect time into months array
flight_time = FlightTime()
wb.collect_time(flight_time)

print('create worksheet: ' + wb.workSh.title, end='')
print(' at file : ' + FileName)

# calculate all periods
flight_time.calc_month_sum()  # calculate time by month
flight_time.JAN_JUN_sum = flight_time.calc_period(0, 6)
flight_time.year_sum = flight_time.calc_period(0, 13)

wb.create_workspace(flight_time)

wb.set_print_option()
wb.save_summaries()

print('Done')
