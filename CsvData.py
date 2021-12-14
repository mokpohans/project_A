import calendar
import pandas as pd
import requests
from bs4 import BeautifulSoup

import CsvCreate

pd.set_option('display.max_columns', None)
pd.set_option('mode.chained_assignment',  None)

global __temp_storage_df
__temp_storage_df = pd.DataFrame()

def Csv_First_Date(plantname:str): #csv에서 가장 빠른 날짜를 추출하는 함수
    plant_df: pd.DataFrame = CsvCreate.Matching_Place_csv(plantname)
    Date = CsvCreate.Date_list(plant_df)
    try:
        return Date[0][0]
    except:
        return Date[0]

def Csv_Last_Date(plantname:str): #csv에서 가장 빠른 날짜를 추출하는 함수
    plant_df: pd.DataFrame = CsvCreate.Matching_Place_csv(plantname)
    Date = CsvCreate.Date_list(plant_df)
    try:
        return Date[-1][-1]
    except:
        return Date[-1]

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
        __temp = __Data[__col[i]].tolist()
        if __col[i] == '인버팅후 금일발전량' and Time == 1 :
            if __temp[0] == 0:
                __temp_1.append(0.0)
            else:
                __temp_1.append(0)
            for j in range(1, len(__temp)):
                __temp_1.append(abs(__temp[j] - __temp[j-1]))
        elif __col[i] == '인버팅후 누적발전량':
            SR = coll_S_R()
            if __temp[0] == 0:
                __temp_1.append(0.0)
            else:
                __temp_1.append(0)
            for j in range(1, len(__temp)):
                __value = __temp[j] - __temp[0]
                __result = (__value/1000) * (SR[0] + SR[1] + 1.0)
                __temp_1.append(__result)
            result.append(__temp_1)
            return result
        else:
            __temp_1 = __Data[__col[i]].tolist()
        result.append(__temp_1)
    return result

def coll_S_R(): #한국 전력 거래소에서 금일 SMP과 REC 평균값을 가져온다
    __url = 'https://www.kpx.or.kr/'#한국 전력 거래소 사이트 주소
    __response = requests.get(__url)

    if __response.status_code == 200:
        __html = __response.text
        __soup = BeautifulSoup(__html, 'html.parser')
        __tSMP = __soup.select_one('#smp_01 > table > tbody > tr:nth-child(4) > td')
        __tREC = __soup.select_one(
            '#m_contents > div.m_cont_rg > div.m_today_rec > div.rec > table > tbody > tr:nth-child(3) > td')
        __SMP = __tSMP.get_text()
        __temp = __tREC.get_text()
        __REC = __temp.replace(" ", "")
        __REC = __REC.replace(",", "")
        result = [float(__SMP), float(__REC)]
        return result
    else:
        print(__response.status_code)

# CSV파일에서 시간('분'단위 까지), 발전소 이름 을 이용해 해당 시간의 데이터 행 불러와 검사.
def GetInvertState(time:str, plantname:str):
    global __temp_storage_df
    plant_df: pd.DataFrame = CsvCreate.Matching_Place_csv(plantname) # 먼저 발전소 이름을 조회해서 몇번째 발전소 데이터프레임인지 확인
    try:
        live_checked_df: pd.DataFrame = plant_df[plant_df['측정일시'].str.contains(time)] #발전소 데이터프레임의 '측정일시'부분에서 시간 검사 후 확인
        if (live_checked_df.empty == False): #시간이 존재할 때
            # temp_m = time[len(time)-2, len(time)]
            # print(temp_m)
            __temp_storage_df = live_checked_df.copy(deep=True)
        elif(live_checked_df.empty == True): # 시간이 존재하지 않을 때
            if(__temp_storage_df.empty == False): # 임시 저장 데이터프레임이 비어있지 않다면
                print(__temp_storage_df)
            elif(__temp_storage_df.empty == True): # 임시 저장 데이터프레임 조차도 비어있다면(처음 입력할 때 부터 존재하지 않는 시간)
                pass
    except:
        print('Please check your time, in this version you can only use August and September informations')

def Trans_DF(Data, Date, Time): #캘린더에서 입력 받은 날짜를 시간, 일간, 월간에 맞춰서 날짜변환하는 함수
    if Time == 1 :# 예) 2021-08-01 그대로 사용
       pass
    elif Time == 2 :# 예) 2021-08로 -01 제거
        Date = Date[0:-3]
    elif Time == 3 :# 예) 2021로 -08-01 제거
        Date = Date[0:5]
    data = Data[Data['측정일시'].str.contains(Date)]# 측정일시를 위 조건문에 설정된 대로 필터링
    return data

def sampleing(Data, time):
    __Data = Data
    __time = ['1H', '1D', '1M']
    __Data.set_index("측정일시").resample(__time[time]).first()