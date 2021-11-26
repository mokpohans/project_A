import datetime
import pandas as pd
#import matplotlib.pyplot as plt

# 표 컬럼중 인버터와 관련된 컬럼 리스트
Invert_list= ["인버터전압(R상)", "인버터전압(S상)", "인버터전압(T상)",
              "인버터전류(R상)", "인버터전류(S상)", "인버터전류(T상)"]

# 표 컬럼중 인버터에 대한 통계를 만들고 출력하는 함수
def Invert(Data):
    for i in Invert_list:
        data = Data[i]
        data_Allmean = data.mean() # 평균을 구하는 함수
        data_Max = data.max() # 최대값을 구하는 함수
        data_Min = data.min() # 최소값을 구하는 함수
        data_Median = data.median() # 중앙값을 구하는 함수

        print(i, " 전체 평균 :", data_Allmean, " 최대값 :", data_Max,
              " 최소값 :", data_Min, " 중앙값 :", data_Median, "\n")

#날짜를 리스트로 만드는 함수
def Date(Data):
    __date_lsit = ['year', 'month', 'day']

    for j in range(0,3):
        __date = eval("pd.DatetimeIndex(Data['측정일시'])." + __date_lsit[j]) # '측정시간'열에서 년도, 월, 일로 분리하기 위한 변수 선언
        globals()['date_{}'.format(j)] = [__date[i] for i in range(1, len(__date)-1)
                                          if __date[i]!= __date[i + 1]] # 년, 월, 일 별로 리스트 생성
        if len(globals()['date_{}'.format(j)]) == 0: # 리스트가 비어있을 때
            globals()['date_{}'.format(j)].append(__date[0]) # 리스트에 최초값 추가
        print(globals()['date_{}'.format(j)])

    date_time = datetime.datetime(int(date_0[0]), int(date_1[0]), int(date_2[0]))
    __data = [pd.to_datetime(Data.측정일시) == date]
    sas=datetime.date(2021, 8, 1)

    sas_data = Data.측정일시 == sas
    print(sas_data)

# DataFrame을 출력할 때 '...'로 생략되는 부분없이 전부다 출력하기위한 설정
pd.set_option('display.max_columns', None) #생략되는 행없이 출력
# pd.set_option('display.max_rows', None)

# github에 저장되어있는 csv파일을 불러오는 코드
Testdata = pd.read_csv('CSV/한국지역난방공사_인버터별 분단위 태양광발전 정보_20210831.csv', encoding='CP949')

# CSV파일에서 장소 열에서 발전소 위치를 중복없이 리스트로 만드는 코드
place = Testdata.장소 # if문에서 비교를 위한 '장소'열의 값을 place에 저장
place_list = ['정선한교'] # 장소의 값인 발전소 위치를 저장할 리스트
count_list=0 # place_list의 인덱스
for i in place:
    if place_list[count_list] == i: # 리스트에 있는 장소일 경우
        pass #아무것도 하지않음
    else:
        count_list = count_list + 1 # 리스트의 인덱스를 증가
        place_list.insert(count_list, i) # 리스트에 발전소 위치 추가

# 원본 CSV파일에서 발전소 위치 각각 표를 만듬
for i in range(0, len(place_list)): # 원본파일이 데이터가 많아서 장소별로 DataFrame을 생성
    globals()["Place_{}".format(i + 1)] = Testdata[Testdata.장소 == place_list[i]] # 자동변수할당 하여 Place_1, Place_2, ... , Place_10라는 Datafrrame 생성

