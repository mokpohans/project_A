import calendar
import pandas as pd
import requests
from bs4 import BeautifulSoup

import CsvCreate

pd.set_option('display.max_columns', None)
pd.set_option('mode.chained_assignment',  None)

global __temp_storage_df, return_R, return_S, return_T
__temp_storage_df = pd.DataFrame()
return_R, return_S, return_T = 0, 0, 0

def Csv_First_Date(plantname:str): #csv에서 가장 빠른 날짜를 추출하는 함수
    plant_df: pd.DataFrame = CsvCreate.Matching_Place_csv(plantname)
    Date = CsvCreate.Date_list(plant_df)
    return Date[0]

def Csv_Last_Date(plantname:str): #csv에서 가장 빠른 날짜를 추출하는 함수
    plant_df: pd.DataFrame = CsvCreate.Matching_Place_csv(plantname)
    Date = CsvCreate.Date_list(plant_df)
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
def Get_RST_InvertState(time:str, plantname:str):
    global __temp_storage_df, return_R, return_S, return_T
    plant_df: pd.DataFrame = CsvCreate.Matching_Place_csv(plantname) # 먼저 발전소 이름을 조회해서 몇번째 발전소 데이터프레임인지 확인
    live_checked_df: pd.DataFrame = plant_df[plant_df['측정일시'].str.contains(time)] #발전소 데이터프레임의 '측정일시'부분에서 시간 검사 후 확인
    if (live_checked_df.empty == False): #시간이 존재할 때
        __temp_storage_df = live_checked_df.copy(deep=True) # 비교용 임시저장_DF에 시간 저장
        # 임시저장 DF 저장 후, 라이브체크 df에서 값 얻어옴
        R_state, S_state, T_state = live_checked_df['인버터전류(R상)'].values[0], live_checked_df['인버터전류(S상)'].values[0], \
                                      live_checked_df['인버터전류(T상)'].values[0]
        if ((R_state == None) and (S_state == None) and (T_state == None)):
            return_R, return_S, return_T = 0, 0, 0
            # return return_R, return_S, return_T
            return [return_R, return_S, return_T]
        elif ((R_state != 0) and (S_state != 0) and (T_state != 0)):
            return_R, return_S, return_T = 1, 1, 1  # 1은 켜진상태
            # return return_R, return_S, return_T
            return [return_R, return_S, return_T]
        elif ((R_state == 0) and (S_state == 0) and (T_state == 0)):
            return_R, return_S, return_T = 0, 0, 0  # 0은 꺼진상태
            # return return_R, return_S, return_T
            return [return_R, return_S, return_T]
        else:
            return_R, return_S, return_T = 2, 2, 2  # 2는 셋 중에 하나, 두개가 이상한 상태
            # return return_R, return_S, return_T
            return [return_R, return_S, return_T]

    elif(live_checked_df.empty == True): # 시간이 존재하지 않을 때
        if(__temp_storage_df.empty == False): # 임시 저장 데이터프레임이 유효하다면
            # 임시 저장 DF에서 값 불러옴
            R_state, S_state, T_state = __temp_storage_df['인버터전류(R상)'].values[0], __temp_storage_df['인버터전류(S상)'].values[0], \
                                       __temp_storage_df['인버터전류(T상)'].values[0]
            if ((R_state == None) and (S_state == None) and (T_state == None)):
                return_R, return_S, return_T = 0, 0, 0
                # return return_R, return_S, return_T
                return [return_R, return_S, return_T]
            elif ((R_state != 0) and (S_state != 0) and (T_state != 0)):
                return_R, return_S, return_T = 1, 1, 1  # 1은 켜진상태
                # return return_R, return_S, return_T
                return [return_R, return_S, return_T]
            elif ((R_state == 0) and (S_state == 0) and (T_state == 0)):
                return_R, return_S, return_T = 0, 0, 0  # 0은 꺼진상태
                # return return_R, return_S, return_T
                return [return_R, return_S, return_T]
            else:
                return_R, return_S, return_T = 2, 2, 2  # 2는 셋 중에 하나, 두개가 이상한 상태
                # return return_R, return_S, return_T
                return [return_R, return_S, return_T]

        elif(__temp_storage_df.empty == True): # 임시 저장 데이터프레임 조차도 비어있다면(처음 입력할 때 부터 존재하지 않는 시간)
            time_number = len(time)     # 존재하지 않는 시간의 1초 전 데이터 프레임 내용을 가져오자.
            target_time = time
            if(time_number == 15):
                parsed_year = int(target_time[0:4])
                parsed_month = int(target_time[5:7])
                parsed_day = int(target_time[8:10])
                parsed_hour = int(target_time[11:12]) # 시간 부분만 타임포맷이 다르다
                parsed_minute = int(target_time[13:15])

            elif(time_number == 16):
                parsed_year = int(target_time[0:4])
                parsed_month = int(target_time[5:7])
                parsed_day = int(target_time[8:10])
                parsed_hour = int(target_time[11:13]) # 시간 부분만 타임 포맷이 다르다
                parsed_minute = int(target_time[14:16])

            if parsed_month in [8, 9]: # 분석한 시간의 '월'이 8,9월이면
                parsed_minute = parsed_minute - 1 # '분' 먼저 차감
                if(parsed_minute < 0): # '분'이 음수가 될 때
                    parsed_hour = parsed_hour - 1 # '시' 차감하고
                    parsed_minute = 59  # 자동으로 '59분'으로 맞춤
                    if(parsed_hour < 0): # '시' 또한 음수가 될 때
                        parsed_day = parsed_day - 1 # '일' 차감
                        parsed_hour = 23  # '23시'로 맞춤
                        if(parsed_day == 0): #'일'이 '0일'이 될 때 #31일, 30일, 29일, 28일 중 하나를 선택하도록 해야함
                            parsed_month = parsed_month - 1 # 우선 비정상 상태이므로 '월' 부터 차감
                            #비정상 상태부터 처리
                            if(parsed_month == 0): # '월'이 0일 때(0월은 존재X; '년' 변동 필요)
                                parsed_year = parsed_year - 1 # '년' 차감
                                if((parsed_year % 4 == 0) and (parsed_month == 2)):
                                    parsed_day = 29 # '차감된 년'이 윤달이고 2월일 때 -> parsed_day는 29일
                                elif((parsed_year % 4 != 0) and (parsed_month == 2)):
                                    parsed_day = 28 # '차감된 년'이 윤달이 아니고 2월일 때 -> parsed_day는 28일

                            # 정상 상태일 때( 년 변동 필요 없을 때; 월만 차감됬을 때)
                            elif ((parsed_year % 4 == 0) and (parsed_month == 2)):
                                parsed_day = 29 # 윤달, 2월 처리
                            elif ((parsed_year % 4 != 0) and (parsed_month == 2)):
                                parsed_day = 28 # not윤달, 2월 처리
                                # 1,3,5,7,8,10,12월은 31일
                            elif parsed_month in [1,3,5,7,8,10,12]:
                                parsed_day = 31
                                # 4,6,9,11월은 30일
                            elif parsed_month in [4,6,9,11]:
                                parsed_day = 30

                edited_time_str = "{0:d}-{1:02d}-{2:02d} {3:d}:{4:02d}".format(
                    parsed_year, parsed_month, parsed_day, parsed_hour, parsed_minute)
                # print(f'time edited (minus 1) : {edited_time_str}')

                __temp_storage_df = plant_df[plant_df['측정일시'].str.contains(edited_time_str)]
                # print(__temp_storage_df)

                # 임시 저장 DF에서 값 불러옴
                R_state, S_state, T_state = __temp_storage_df['인버터전류(R상)'].values[0], __temp_storage_df['인버터전류(S상)'].values[0], \
                                            __temp_storage_df['인버터전류(T상)'].values[0]

                if ((R_state == None) and (S_state == None) and (T_state == None)):
                    return_R, return_S, return_T = 0, 0, 0
                    # return return_R, return_S, return_T
                    return [return_R, return_S, return_T]
                elif ((R_state != 0) and (S_state != 0) and (T_state != 0)):
                    return_R, return_S, return_T = 1, 1, 1  # 1은 켜진상태
                    # return return_R, return_S, return_T
                    return [return_R, return_S, return_T]
                elif ((R_state == 0) and (S_state == 0) and (T_state == 0)):
                    return_R, return_S, return_T = 0, 0, 0  # 0은 꺼진상태
                    # return return_R, return_S, return_T
                    return [return_R, return_S, return_T]
                else:
                    return_R, return_S, return_T = 2, 2, 2  # 2는 셋 중에 하나, 두개가 이상한 상태
                    # return return_R, return_S, return_T
                    return [return_R, return_S, return_T]

            else:
                print(f'ERROR : time edited (minus 1)')
                return_R, return_S, return_T = 0, 0, 0
                return [return_R, return_S, return_T]

    #

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
    __val = ['first()', 'max()', 'mean()']
    __Data["측정일시"] = pd.to_datetime(__Data["측정일시"])
    __Data = eval('__Data.set_index("측정일시").resample(__time[time - 1]).' + __val[time - 1])
    __Data.reset_index(drop=False, inplace=True)
    return __Data