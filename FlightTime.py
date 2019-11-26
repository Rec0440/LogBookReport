'''

'''


class FlightTime:
    # data structure for collect and sum time by month
    YearTimeList = {'01': {'hour': [], 'min': [], 'sum': [0, 'JAN']},
                    '02': {'hour': [], 'min': [], 'sum': [0, 'FEB']},
                    '03': {'hour': [], 'min': [], 'sum': [0, 'MAR']},
                    '04': {'hour': [], 'min': [], 'sum': [0, 'APR']},
                    '05': {'hour': [], 'min': [], 'sum': [0, 'MAY']},
                    '06': {'hour': [], 'min': [], 'sum': [0, 'JUN']},
                    '07': {'hour': [], 'min': [], 'sum': [0, 'JUL']},
                    '08': {'hour': [], 'min': [], 'sum': [0, 'AUG']},
                    '09': {'hour': [], 'min': [], 'sum': [0, 'SEP']},
                    '10': {'hour': [], 'min': [], 'sum': [0, 'OCT']},
                    '11': {'hour': [], 'min': [], 'sum': [0, 'NOV']},
                    '12': {'hour': [], 'min': [], 'sum': [0, 'DEC']}}
    list_month = YearTimeList.keys()
    YearSummary = {'Hour': [], 'min': []}
    JAN_JUN_sum = {'Hour': [], 'min': []}

    def calc_month_sum(self):
        ''' Calculate time from month '''
        for lik in self.list_month:
            minutes = sum(self.YearTimeList[lik]['min'])
            calcmin = minutes % 60
            calchour = minutes // 60
            calchour = calchour + sum(self.YearTimeList[lik]['hour'])
            month_result = str(calchour) + ':' + str('%02d' % calcmin)
            self.YearTimeList[lik]['sum'][0] = month_result

    def calc_jan_jun(self):
        for lik in self.list_month[:5]:
            minutes = sum(self.YearTimeList[lik]['min'])
            calcmin = minutes % 60
            calchour = minutes // 60
            calchour = calchour + sum(self.YearTimeList[lik]['hour'])
            month_res = str(calchour) + ':' + str('%02d' % calcmin)
            self.JAN_JUN_sum = month_res

