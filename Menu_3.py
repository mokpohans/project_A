## 장애목록
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandastable import Table

##테스트 데이터
df_data = pd.read_csv("Resources/csv_files/한국지역난방공사_인버터별 분단위 태양광발전 정보_20210831.csv",
                      encoding="cp949")#장애 목록을 만들어서 넣을 예정

## 장소, 데이터 테이블, 데이터, 데이터 샘플
global place, data_table, data, df_jeongsun

cal_start = "start"

cal_end = "end"

place_name = "정선한교"

# 정선한교만 있는 데이터 플레임 생성
jeongsun = (df_data.장소 == place_name)
df_jeongsun = df_data[jeongsun]

## index 컬럼 출력
df_jeongsun.columns


## 공백 프레임 생성 메소드
def f_x(frame_name, x):
    instant_frame = ttk.Frame(frame_name)
    instant_frame.pack(side="left", padx=x)


def f_y(frame_name, y):
    instant_frame = ttk.Frame(frame_name)
    instant_frame.pack(side="top", padx=y)


## 출력 버튼 메소드
def out_btr():
    ##대신data 변수
    global data_table, df_jeongsun

    ## 테이블 지우기
    data_table.clearTable()
    data_table.destroy()

    ##테이블 작성 부분
    data_table = Table(frame_2, dataframe=df_jeongsun, height=600)

    data_table.show()


## 윈도우 생성
menu3_window = tk.Tk()

# 현재 모니터 디스플레이 사이즈(나중에 비율 맞출때 쓰기)
screen_width = menu3_window.winfo_screenwidth()

screen_height = menu3_window.winfo_screenheight()

default_width = 1000  # 디폴트 너비, 높이
default_height = 750

# 타이틀(Solar Electricity Monitoring System)
menu3_window.title("장애목록")

# 디폴트 사이즈 설정
menu3_window.geometry(f"{default_width}x{default_height}")

## 프레임 구분
frame_1 = ttk.Frame(menu3_window, relief="raised", height=100)
frame_1.pack(side="top", fill="both", padx=2, pady=2, expand=True)

## frame_1 내부 프레임 1
## 장소명
frame_1_1 = ttk.Frame(frame_1, relief="solid", height=50)
frame_1_1.pack(side="top", padx=10, fill="x", expand=True)

##lable 위젯 생성
place_name = ttk.Label(frame_1_1, text="장애 목록")
place_name.pack(anchor="center", ipadx=5, ipady=5, fill="both", expand=True)

## place_name 위치 및 폰트 속성 설정
place_name.config(anchor="center", font=("한컴바탕", 24))

##frame_1의 내부 프레임 2
frame_1_2 = ttk.Frame(frame_1)
frame_1_2.pack(side="top", fill="both", expand=True, padx=10, pady=5)

##날짜입력 위젯생성

##출력 버튼 위젯 생성
output_btr = ttk.Button(frame_1_2, text="출력", command=out_btr)
output_btr.pack(side="right", padx=5)

##날짜 범위 끝
day_end = ttk.Entry(frame_1_2, textvariable=cal_end, width=20)
day_end.insert(0, cal_end)
day_end.pack(side="right")

## "~"
in_instans = ttk.Label(frame_1_2, text=" ~ ")
in_instans.pack(side="right", padx=5)
in_instans.configure(state='readonly')

## 날짜 범위 시작
day_start = ttk.Entry(frame_1_2, textvariable=cal_start, width=20)
day_start.insert(0, cal_start)
day_start.pack(side="right")

##lable 위젯 생성
lable_name = ttk.Label(frame_1_2, text="날짜입력 : ")
lable_name.pack(side="right")

##장애목록 출력 프레임
frame_2 = ttk.Frame(menu3_window, height=600, relief="solid")
frame_2.pack(side="top", fill="both", expand=True)

data_table = Table(frame_2, dataframe=df_data, height=600)
data_table.show()

menu3_window.mainloop()
