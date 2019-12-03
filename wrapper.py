"""
for delineate GUI and Controller

onclick-methods
"""

from FlightTime import FlightTime
from Report import Report


class Wrapper:
    def __init__(self, filename, period):
        self.wb = Report(filename, period)
        self.ft = FlightTime()

    def onclick_calculate(self):
        self.wb.collect_time(self.ft)
        self.ft.calc_month_sum()
        self.ft.JAN_JUN_sum = self.ft.calc_period(0, 6)
        self.ft.year_sum = self.ft.calc_period(0, 13)
        self.wb.create_workspace(self.ft)
        self.wb.set_print_option()
        self.wb.save_summaries()
