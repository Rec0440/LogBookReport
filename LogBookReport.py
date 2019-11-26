'''
план виконання завдання:
юзер запускає прогу у директорії де знаходиться шуканий excel-workbook,
у разі відсутності файлу з назвою по замовчуванню, юзер вводить назву файлу, що треба обробити
юзер вказує за який період необхідно провести обрахунки, в роках.
програма проводить обрахунки,
результат роботи додається, як worksheet в кінець workbook
'''

from Report import Report
from FlightTime import FlightTime


# testing
FileName = 'PILOT_LOG_532.xlsx'
result_wb = Report(FileName)
TotalFT = FlightTime()
result_wb.collect_time(TotalFT.YearTimeList)

print('Start application at: ' + str(result_wb.ExecutionTime) + '\n')
print('create worksheet: ' + result_wb.workSh.title, end='')
print(' at file : ' + FileName)

TotalFT.calc_month_sum()  # calculate time by month
TotalFT.JAN_JUN_sum()
result_wb.create_workspace(TotalFT.YearTimeList)
result_wb.set_print_option()
result_wb.save_summaries()
