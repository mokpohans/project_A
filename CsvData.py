import calendar
import pandas as pd
import requests
from bs4 import BeautifulSoup

import CsvCreate

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

def coll_S_R():
    __url = 'https://www.kpx.or.kr/'
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

# 표 컬럼중 인버터에 대한 통계를 만들고 출력하는 함수
def Invert_state(Data: pd.DataFrame, Time) -> list:
    __Fun: list = ["mean", "max", "min"]  # 통계를 내기위한 기능 리스트
    __Inverts_list: list = ["인버터전압(R상)", "인버터전압(S상)", "인버터전압(T상)", "인버터전류(R상)", "인버터전류(S상)", "인버터전류(T상)"]
    __Data = Data
    __Data[__Inverts_list[0]].str.contains(Time)

def GetInvertState(time, plantname):
    plant_df: pd.DataFrame = CsvCreate.Matching_Place_csv(plantname)
    try:
        live_checked_df: pd.DataFrame = plant_df[plant_df['측정일시'].str.contains(time)]
        print(live_checked_df)
    except:
        print('Please check your time, in this version you can only use August and September informations')