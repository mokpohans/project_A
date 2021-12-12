import calendar
import pandas as pd
import CsvCreate as tc
pd.set_option('display.max_columns', None)
def Months(time):
    __month = time.month
    __year = time.year
    __time = calendar.monthrange(__year, __month)[ 1 ]
    return __time

def Data_list(Data : pd.DataFrame, type, Time):

    result = []
    choice = Data
    choice['측정일시'] = pd.to_datetime(choice['측정일시'])
    if Time == 1:
        choices = choice.set_index('측정일시').resample('1H').first()
    elif Time == 2:
        choices = choice.set_index('측정일시').resample('1D').max()
    elif Time == 3:
        choices = choice.set_index('측정일시').resample('1M').mean()
    else:
        return

    if (type == '인버팅후 누적발전량') or (type == '인버팅후 금일발전량' and Time == 1 ):
        __temp = choices[type].tolist()
        result.append(abs(__temp[1] - __temp[0]))
        for i in range(1, len(__temp)):
            result.append(abs(__temp[i] - __temp[i-1]))
    else:
        result = choices[type].tolist()
    return result