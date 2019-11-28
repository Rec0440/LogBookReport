'''
Структура даних, для зберігання оброленої інформації
'''

import datetime


class FlightTime:
    # data structure for collect and sum time by month
    months_digits = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    months_flight_time = {}  # main data structure
    year_sum = ''
    JAN_JUN_sum = ''

    # create main data structure
    def __init__(self):  # dict  --->  '01': {'hour': [], 'min': [], 'sum': [0, 'JAN']} ...
                         # dict  --->  '12': {'hour': [], 'min': [], 'sum': [0, 'DEC']}
        self.months_flight_time = {ind: {'hour': [], 'min': [], 'sum': [0, mon]}
                                   for ind, mon in zip(self.months_digits, self.months)}

    # calculate day_time by months
    def calc_month_sum(self):
        ''' Calculate time from month '''
        for lik in self.months_digits:
            minutes = sum(self.months_flight_time[lik]['min'])
            calc_min = minutes % 60
            calc_hour = minutes // 60
            calc_hour = calc_hour + sum(self.months_flight_time[lik]['hour'])
            # timeform = datetime.timedelta(hours=calc_hour, minutes=calc_min)  its not working right now
            month_result = str(calc_hour) + ':' + str('%02d' % calc_min)
            self.months_flight_time[lik]['sum'][0] = month_result

    # calculate months_time by start-stop period - use to get 6 months total flight time
    def calc_period(self, start, stop):
        minutes = []
        hours = []
        for lik in self.months_digits[start:stop]:
            hour, mint, sec = self.months_flight_time[lik]['sum'][0].split(':')
            minutes.append(int(mint))
            hours.append(int(hour))
        m = sum(minutes)
        calc_m = m % 60
        calc_h = m // 60
        calc_h = calc_h + sum(hours)
        period = str(calc_h) + ':' + str('%02d' % calc_m) # delete soon
        return period
