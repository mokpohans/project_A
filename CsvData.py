import calendar
import pandas as pd
import CsvCreate as tc
pd.set_option('display.max_columns', None)
def Months(time):
    __month = time.month
    __year = time.year
    __time = calendar.monthrange(__year, __month)[ 1 ]
    return __time

def test(Data : pd.DataFrame, type):
    choice = Data.loc[Data[type] != 0]
    choices = pd.DatetimeIndex(choice['측정일시']).resample('1H').first()
    print(choices)

test(tc.Place_1, "인버팅후 인버터전력")