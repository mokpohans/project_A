import datetime

import pandas as pd
import calendar
global  year, month, day, Date_list, Days
# 표 컬럼중 인버터와 관련된 컬럼 리스트
from pandas import DataFrame


# 표 컬럼중 인버터에 대한 통계를 만들고 출력하는 함수
def Invert(Data : pd.DataFrame) -> float:
    __Fun: list = ["mean", "max", "min"]  # 통계를 내기위한 기능 리스트
    __Inverts_list: list = ["인버터전압(R상)", "인버터전압(S상)", "인버터전압(T상)", "인버터전류(R상)", "인버터전류(S상)", "인버터전류(T상)"]
    Invert_list = {}
    for i in __Inverts_list:

        data = Data[i]
        for __fun in __Fun:
            globals()["data_{}".format(str(__fun))] = eval("data." + __fun + "()")
        print(f'{i} 전체 평균 : {data_mean} 최대값 : {data_max} 최소값 : {data_min}')
        Invert_list[i] = {data_mean, data_max, data_min}
    print(Invert_list)
    return Invert_list

#날짜를 리스트로 만드는 함수
def Date_list(Data : pd.DataFrame) -> list:
    global  year, month, day, Days

    year, month, day = 0, 0, 0
    __date_lsit :list = ['year', 'month']

    __Days= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, None]
    __month_list : list = []
    Date_list : list = []

    for j in range(0,2):
        __date = eval("pd.DatetimeIndex(Data['측정일시'])." + __date_lsit[j]) # '측정시간'열에서 년도, 월로 분리하기 위한 변수 선언
        globals()['date_{}'.format(j)] : list = [__date[i] for i in range(1, len(__date)-1)
                                          if __date[i]!= __date[i + 1]] # 년, 월 별로 리스트 생성
        if len(globals()['date_{}'.format(j)]) == 0: # 리스트가 비어있을 때
            globals()['date_{}'.format(j)].append(__date[0]) # 리스트에 최초값 추가
    globals()['date_{}'.format(j)].append(__date[-1]) # for 문에서 append를 할때 마지막 일짜가 추가 되지않는 부분이 있어서 추가 (예 : 8월 ,9월 이있으면 리스트에는 8월만 들어가 있음)
    __conut = 0

    for val in range(0, len(date_1)*len(__Days) - 1):

        try:
            Year, Month, Day = str(date_0[year]), str(date_1[month]).zfill(2), str(__Days[day]).zfill(2)
        except IndexError:
            if Next_Date(year, month, day):
                pass
            else:
                break
        time_1 = Year + "-" + Month + "-" + Day  # 년, 월, 일을 2021-08-01로 만드는 코드
        if Month ==  str(date_1[__conut]).zfill(2):
            Date_list.append(time_1)
        else:
            Date_list.append(__month_list)
            __month_list = [] #여기서 clear를 쓰지 않는 이유는 clear가 list =[] 보다 약간 느리기 때문이다
            __month_list.append(time_1)
            conut = conut + 1
        Next_Date(year, month, day)
    Date_list.append(__month_list)
    return Date_list

def Date_Day(Data : pd.DataFrame, Day):
    try:
        data = Data[Data['측정일시'].str.contains(Day)]
        if len(data.index) == 0:
            return
        else:
            return data
    except:
        return

def Next_Date(__Year : str,__Month : str, __Day):
    global year, month, day, Days
    try:
        if Days[__Day] == calendar.monthrange(date_0[year], date_1[month])[1] : # Day
            day = 0
            if __Month == str(date_1[-1]).zfill(2): # Month
                month = 0
                if __Year == date_0[-1]: # year
                    return False
                else:
                    year = year + 1
                    return year, month, day
            else:
                month = month + 1
                return year, month, day
        else:
            day = day + 1
            return year, month, day
    except:
        return False

def Months(time):
    __month = time.month
    __year = time.year
    __time = calendar.monthrange(__year, __month)[ 1 ]
    return __time

# def test(Data, type):
#     if type == 1:
#         Data
#     elif type == 2:
#
#     elif type == 3:

# DataFrame을 출력할 때 '...'로 생략되는 부분없이 전부다 출력하기위한 설정
#pd.set_option('display.max_columns', None) #생략되는 행없이 출력
# pd.set_option('display.max_rows', None)

# github에 저장되어있는 csv파일을 불러오는 코드
Orignal_CSV: DataFrame = pd.read_csv('CSV/한국지역난방공사_인버터별 분단위 태양광발전 정보_20210831.csv', encoding='CP949')

# CSV파일에서 장소 열에서 발전소 위치를 중복없이 리스트로 만드는 코드
place: pd.Series = Orignal_CSV.장소 # if문에서 비교를 위한 '장소'열의 값을 place에 저장
place_list: list = ['정선한교'] # 장소의 값인 발전소 위치를 저장할 리스트
count_list: int = 0 # place_list의 인덱스

for i in place:
    if place_list[count_list] == i: # 리스트에 있는 장소일 경우
        pass #아무것도 하지않음
    else:
        count_list = count_list + 1 # 리스트의 인덱스를 증가
        place_list.insert(count_list, i) # 리스트에 발전소 위치 추가

# 원본 CSV파일에서 발전소 위치 각각 표를 만듬
for i in range(0, len(place_list)): # 원본파일이 데이터가 많아서 장소별로 DataFrame을 생성
    globals()["Place_{}".format(i + 1)] = Orignal_CSV[Orignal_CSV.장소 == place_list[i]] # 자동변수할당 하여 Place_1, Place_2, ... , Place_10라는 Datafrrame 생성
