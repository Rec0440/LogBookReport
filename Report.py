"""
тут - модель даних для обробки Excel-файлу,

відкрити файл,
обрахувати дані,
створити листок YearSummary-звіт,
додати в кінець workbook
"""

from openpyxl.styles import Alignment, Font, Border, Side
from openpyxl import load_workbook
from datetime import datetime


class Report:
    # create workbook
    def __init__(self, filename, year='2019'):
        self.filename = filename                                # name of datafile
        self.default_year = year[2:]                            # two last digit of def year
        self.workb = load_workbook(filename)                    # data workbook
        self.ExecutionTime = datetime.now()                     # date and time when starting count
        self.typeDate = type(self.ExecutionTime)                # type of datetime obj
        self.ReportName = self.set_report_title()               # construct name of report
        self.workSh = self.workb.create_sheet(self.ReportName)  # create report worksheet at last position in workbook
        self.Name_Sheets = self.workb.sheetnames                # list of worksheets
        self.Name_Sheets.reverse()                              # reverse for counting from today into past
        self.length_sheets_names = len(self.Name_Sheets)        # number of worksheets

    def set_report_title(self):
        month = self.ExecutionTime.strftime('%m')
        my_title = 'Report20' + str(self.default_year) + '-' + month
        return my_title

    # collect time from all sheets and put ot total_data_structure
    def collect_time(self, total_data, yr='19', end='56'):
        end_sheet = end                      # worksheet for stop calculating
        year = yr                            # default year for calculating
        tds = total_data.months_flight_time  # data structure for total flight-time

        for sh in self.Name_Sheets:  # list of sheet names
            # if title is digit (not report) and title not later 2019
            if self.workb[sh].title.isdigit() and (self.workb[sh].title >= end_sheet):
                for row in self.workb[sh]:  # next row in worksheet, row[0] - date, row[10] - time
                    my_date = row[0].value
                    # try find date type
                    if type(my_date) == self.typeDate:
                        calc_year = my_date.strftime('%y')  # '19' this for calculating only 1 year
                        # collect only 1 year, if trying collect another year - break
                        if calc_year != year:
                            break
                        my_time = str(row[10].value)         # take col'J', "Total time'
                        calc_month = my_date.strftime('%m')  # '07' - month
                        h, m, s = my_time.split(':')
                        tds[calc_month]['hour'].append(int(h))
                        tds[calc_month]['min'].append(int(m))
            # stop counting, when date of sheet too old
            elif self.workb[sh].title < end_sheet:
                break

    # create form of summary
    def create_workspace(self, total_data):
        flt = total_data.months_flight_time

        # Style preparing
        ft = Font(bold=True)
        bd = Side(style='medium')
        set_border = Border(left=bd, bottom=bd, right=bd, top=bd)
        hv_alignment = Alignment(horizontal='center', vertical='center')
        hvw_alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
        wr_alignment = Alignment(wrap_text=True)

        hv_array = ['H2', 'H3', 'I3', 'F2', 'E2', 'B1', 'A2', 'A1',
                    'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10', 'J11',
                    'J12', 'J13', 'J14', 'J15', 'J16', 'J17', 'J18', 'J19']
        hvw_array = ['J2', 'G2', 'D2', 'C2', 'B2']

        # insert current time into A1
        self.workSh['A1'].value = self.ExecutionTime.strftime('%d-%m-%y')

        #    HEADER
        self.workSh.merge_cells('B1:J1')
        self.workSh['B1'] = 'PILOT RECORD/Облік польотів'
        self.workSh.merge_cells('A2:A3')
        self.workSh['A2'] = 'Year: 20' + self.default_year
        self.workSh.column_dimensions['A'].width = 16

        self.workSh.merge_cells('B2:B3')
        self.workSh['B2'] = 'SINGLE-ENGINE'
        self.workSh.column_dimensions['B'].width = 11.0
        self.workSh.merge_cells('C2:C3')
        self.workSh['C2'] = 'MULTI-ENGINE'
        self.workSh.column_dimensions['C'].width = 11.0
        self.workSh.merge_cells('D2:D3')
        self.workSh['D2'] = 'MULTI-ENGINE MULTI-PILOT'
        self.workSh.column_dimensions['D'].width = 14
        self.workSh.merge_cells('E2:E3')
        self.workSh['E2'].value = 'JET'
        self.workSh.column_dimensions['E'].width = 7.0
        self.workSh.merge_cells('F2:F3')
        self.workSh['F2'].value = 'TURBOPROP'
        self.workSh.column_dimensions['F'].width = 12

        self.workSh.merge_cells('G2:G3')
        self.workSh['G2'] = 'TOTAL FLIGHT TIME'
        self.workSh.column_dimensions['G'].width = 14
        self.workSh.merge_cells('H2:I2')
        self.workSh['H2'].value = 'LANDINGS'
        self.workSh['H3'].value = 'DAY'
        self.workSh.column_dimensions['H'].width = 5
        self.workSh['I3'].value = 'NIGHT'
        self.workSh.column_dimensions['I'].width = 7
        self.workSh.merge_cells('J2:J3')
        self.workSh['J2'] = 'LANDINGS TOTAL'
        self.workSh.column_dimensions['J'].width = 10

        self.workSh['A4'].value = flt['01']['sum'][1]
        self.workSh['J4'].value = flt['01']['sum'][0]
        self.workSh['A5'].value = flt['02']['sum'][1]
        self.workSh['J5'].value = flt['02']['sum'][0]
        self.workSh['A6'].value = flt['03']['sum'][1]
        self.workSh['J6'].value = flt['03']['sum'][0]
        self.workSh['A7'].value = flt['04']['sum'][1]
        self.workSh['J7'].value = flt['04']['sum'][0]
        self.workSh['A8'].value = flt['05']['sum'][1]
        self.workSh['J8'].value = flt['05']['sum'][0]
        self.workSh['A9'].value = flt['06']['sum'][1]
        self.workSh['J9'].value = flt['06']['sum'][0]
        self.workSh['A10'].value = 'TOTALS 6mo'
        self.workSh['J10'].value = total_data.JAN_JUN_sum

        self.workSh['A11'].value = flt['07']['sum'][1]
        self.workSh['J11'].value = flt['07']['sum'][0]
        self.workSh['A12'].value = flt['08']['sum'][1]
        self.workSh['J12'].value = flt['08']['sum'][0]
        self.workSh['A13'].value = flt['09']['sum'][1]
        self.workSh['J13'].value = flt['09']['sum'][0]
        self.workSh['A14'].value = flt['10']['sum'][1]
        self.workSh['J14'].value = flt['10']['sum'][0]
        self.workSh['A15'].value = flt['11']['sum'][1]
        self.workSh['J15'].value = flt['11']['sum'][0]
        self.workSh['A16'].value = flt['12']['sum'][1]
        self.workSh['J16'].value = flt['12']['sum'][0]
        self.workSh['A17'].value = 'YEAR TOTALS'
        self.workSh['J17'].value = total_data.year_sum
        self.workSh['A18'].value = 'TOTALS prev.YEARS'
        self.workSh['A18'].alignment = wr_alignment
        self.workSh['A19'].value = 'TOTALS TO DATE'

        # set styles and alignment
        for cel in hv_array:
            self.workSh[cel].alignment = hv_alignment
        for cel in hvw_array:
            self.workSh[cel].alignment = hvw_alignment
        for col in self.workSh.columns:
            for cel in col:
                cel.font = ft
                cel.border = set_border

    # prepare print options
    def set_print_option(self):
        self.workSh.set_printer_settings('9', 'landscape')

    # save result of calculating
    def save_summaries(self):
        self.workb.save(self.filename)


if __name__ != '__main__':
    print('Execute TimeCalculate.py')
