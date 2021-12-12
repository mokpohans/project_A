import calendar
import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('mode.chained_assignment',  None)

#그달의 마지막 일(day)를 출력하는 함수
def Months(time):
    __month = time.month
    __year = time.year
    __time = calendar.monthrange(__year, __month)[ 1 ]
    return __time

#그래프를 그리기위한 리스트 만드는 함수
def Data_list(Data : pd.DataFrame, type, Time):

    __temp_1 = []
    result = []
    __col = [str(type), '경사면일사량(인버터단위)', '수평면일사량(인버터단위)']
    __time = ['1H', '1D', '1M']
    __val = ['first()', 'max()', 'mean()']
    __Data = Data
    __Data["측정일시"] = pd.to_datetime(__Data["측정일시"])
    __Data = eval('__Data.set_index("측정일시").resample(__time[Time - 1]).' + __val[Time - 1])
    for i in range(0,3):
        if (__col[i] == '인버팅후 누적발전량') or (__col[i] == '인버팅후 금일발전량' and Time == 1 ):
            __temp = __Data[__col[i]].tolist()
            if __temp[0] == 0:
                __temp_1.append(0.0)
            else:
                __temp_1.append(0)
            for i in range(1, len(__temp)):
                __temp_1.append(abs(__temp[i] - __temp[i-1]))
            if __col[i] == '인버팅후 누적발전량':
                break
            else:
                pass
        else:
            __temp_1 = __Data[__col[i]].tolist()
        result.append(__temp_1)
    return result