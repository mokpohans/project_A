## 보고서 메뉴
import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import DateEntry
import pandas as pd
from pandastable import Table

## 장소, 데이터 테이블, 데이터, 데이터 샘플
global place_name, data_table, data, df_jeongsun, df

##테스트 데이터
df_data = pd.read_csv("Resources/csv_files/한국지역난방공사_인버터별 분단위 태양광발전 정보_20210831.csv",
                      encoding="cp949") #선택한 발전소의 테이블을 출력할 예정

## 장소 임시 지정
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


## 날짜선택 옵션 함수
def btr_1():
    ## 기본 데이터 초기화
    day_selete.delete(0, tk.END)
    if (type_select.get() == "시간별"):
        day_selete.insert(0, "2019-08-00")
        lable_name.configure(text="날짜 [년도-월-일] 입력 : ")

    elif (type_select.get() == "일별"):
        day_selete.insert(0, "2019-00")
        lable_name.configure(text="날짜 [년도-월] 입력 : ")

    elif (type_select.get() == "월별"):
        day_selete.insert(0, "2000")
        lable_name.configure(text="날짜 [년도] 입력")

    else:
        day_selete.insert(0, "2019-08-01")
    day_selete.pack(side="right", padx=5)


## 출력 버튼 메소드
def out_table():
    ##대신data 변수
    global data_table, df_jeongsun, df

    ## 테이블 지우기
    data_table.clearTable()
    data_table.destroy()

    data_table = Table(frame_2, dataframe=df, height=600)
    data_table.show()


## 윈도우 생성
menu2_window = tk.Tk()

# 현재 모니터 디스플레이 사이즈(나중에 비율 맞출때 쓰기)
screen_width = menu2_window.winfo_screenwidth()

screen_height = menu2_window.winfo_screenheight()

default_width = 1000  # 디폴트 너비, 높이
default_height = 750

# 타이틀(Solar Electricity Monitoring System)
menu2_window.title("보고서")

# 디폴트 사이즈 설정
menu2_window.geometry(f"{default_width}x{default_height}")

## 프레임 구분
frame_1 = ttk.Frame(menu2_window, relief="raised", height=100)
frame_1.pack(side="top", fill="both", padx=2, pady=2, expand=True)

## frame_1 내부 프레임 1
## 장소명
frame_1_1 = ttk.Frame(frame_1, relief="solid", height=50)
frame_1_1.pack(side="top", padx=10, fill="x", expand=True)

##lable 위젯 생성
place_name = ttk.Label(frame_1_1, text=place_name + "  보고서")
place_name.pack(anchor="center", ipadx=5, ipady=5, fill="both", expand=True)

## place_name 위치 및 폰트 속성 설정
place_name.config(anchor="center", font=("한컴바탕", 24))

##frame_1의 내부 프레임 2
frame_1_2 = ttk.Frame(frame_1)
frame_1_2.pack(side="top", fill="both", expand=True, padx=10, pady=5)

## 기간 종류
type_select = ttk.Combobox(frame_1_2, values=["시간별", "일별", "월별"], width=20)

type_select.set("시간별/일별/월별 선택")
type_select.configure(state='readonly')
type_select.pack(side="left", padx=5)
##기간 종류 적용 버튼 위젯 생성
op_btr = ttk.Button(frame_1_2, text="적용", command=btr_1, width=15)
op_btr.pack(side="left", padx=5)

##출력 버튼 위젯 생성
output_btr = ttk.Button(frame_1_2, text="출력", command=out_table)
output_btr.pack(side="right", padx=5)

##날짜 선택
##날짜입력 위젯생성
day_selete = DateEntry(frame_1_2, year=day.year, month=day.month, day= day.day ,date_pattern='yyyy/MM/dd', state="readonly")
day_selete.pack(side="right")
day_selete.bind("<<DateEntrySelected>>")

##lable 위젯 생성
lable_name = ttk.Label(frame_1_2, text="날짜입력 : ")
lable_name.pack(side="right")

##보고서 출력 프레임
frame_2 = ttk.Frame(menu2_window, height=600, relief="solid")
frame_2.pack(side="top", fill="both", expand=True)

data_table = Table(frame_2, dataframe=df_data, height=600)
data_table.show()

menu2_window.mainloop()


