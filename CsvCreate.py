import pandas as pd
import calendar
import CsvData
from pandas import DataFrame
global  year, month, day, Date_list, Days

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
        (year, month, day)
    Date_list.append(__month_list)
    return Date_list

def Date_Day(Data : pd.DataFrame, Day): # Date를 읽어들어와서 기준 날짜로 필터링한다
    try:
        data = Data[Data['측정일시'].str.contains(Day)]
        if len(data.index) == 0:
            return
        else:
            return data
    except:
        return

def Next_Date(__Year : str,__Month : str, __Day): #날짜 리스트를 만들때 월의 마지막날 등에 맞춰 년, 월, 일을 설정하는 함수
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

def TransF_Date(Data, Date, Type, Time): #캘린더에서 입력 받은 날짜를 시간, 일간, 월간에 맞춰서 날짜변환하는 함수
    if Time == 1 :# 예) 2021-08-01 그대로 사용
       pass
    elif Time == 2 :# 예) 2021-08로 -01 제거
        Date = Date[0:-3]
    elif Time == 3 :# 예) 2021로 -08-01 제거
        Date = Date[0:5]
    data = Data[Data['측정일시'].str.contains(Date)]# 측정일시를 위 조건문에 설정된 대로 필터링
    result = CsvData.Data_list(data, Type, Time)
    return result

def Matching_Place_csv(place_name):# 메인에서 선택한 발전소 이름을 Place_넘버링에 맞춰서 찾는 함수
    for i in range(0, len(place_list)):
        if globals()["Place_{}".format(i)].iloc[1]['장소'] == place_name:
            return globals()["Place_{}".format(i)]
        else:
            pass

__temp_csv_1: DataFrame = pd.read_csv('Resources/csv_files/한국지역난방공사_인버터별 분단위 태양광발전 정보_20210831.csv',
                                      encoding='CP949')
__temp_csv_2: DataFrame = pd.read_csv('Resources/csv_files/한국지역난방공사_인버터별 분단위 태양광발전 정보_20210930.csv',
                                      encoding='CP949')
#2개의 데이터프레임을 하나로 합치는 코드
Orignal_CSV: DataFrame = pd.concat([__temp_csv_1, __temp_csv_2], ignore_index=True)

place: pd.Series = Orignal_CSV.장소 # if문에서 비교를 위한 '장소'열의 값을 place에 저장
place_list: list = ['정선한교'] # 장소의 값인 발전소 위치를 저장할 리스트
count_list: int = 0 # place_list의 인덱스

for i in place:
# for i in range(len(place)):
    if place_list[count_list] == i: # 리스트에 있는 장소일 경우
        pass #아무것도 하지않음
    else:
        count_list = count_list + 1 # 리스트의 인덱스를 증가
        place_list.insert(count_list, i) # 리스트에 발전소 위치 추가

# 원본 CSV파일에서 발전소 위치 각각 표를 만듬
for i in range(0, len(place_list)): # 원본파일이 데이터가 많아서 장소별로 DataFrame을 생성
    globals()["Place_{}".format(i)] = Orignal_CSV[Orignal_CSV.장소 == place_list[i]] # 자동변수할당 하여 Place_1, Place_2, ... , Place_10라는 Datafrrame 생성
    # print(globals()[f"Place_{i}"])