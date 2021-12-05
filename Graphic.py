## 계측 정보 메뉴
from tkinter import messagebox

import CsvCreate as tc
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import DateEntry
from matplotlib.figure import Figure

## 테스트 변수
global i
i = 0

def print_sel(e):
    prid = day_selete.get_date() #DateTime 타입 반환
    print(prid)

## 공백 프레임 생성 메소드
def f_x(frame_name, x):
    instant_frame = ttk.Frame(frame_name)
    instant_frame.pack(side="right", padx=x)

def f_y(frame_name, y):
    instant_frame = ttk.Frame(frame_name)
    instant_frame.pack(side="top", padx=y)


## 출력 버튼 메소드
def out_btr():
    ##전에 그려진 그래프 데이터 지우기
    ax.clear()

    ## 테스트 코드
    global i
    i += 1
    print("기간종류 : " + type_select.get())
    print("계측종류 : " + type_select_1.get())
    print(i)

    ##그래프 작성 부분####
    x = np.arange(3)
    years = ['2018', '2019', '2020']
    values = [10 / i, 40 * i, 9 * i]

    plt.bar(x, values)
    plt.xticks(x, years)

    ax.set_xlabel("dice")

    ax.set_ylabel("relative frequency")
    ##그래프 작성 부분####

    ##그래프를 캔버스에 그리기
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

def result(Select):
    if Select == 1:


## 날짜선택 옵션 함수
def btr_1():
    if (type_select.get() == "시간별"):
        print(type_select.get())

    elif (type_select.get() == "일별"):
        print(type_select.get())

    elif (type_select.get() == "월별"):
        print(type_select.get())

    else:
        messagebox.showinfo("선택 오류", "기간선택을 해주세요4")



menu1_window = tk.Tk()

# 현재 모니터 디스플레이 사이즈(나중에 비율 맞출때 쓰기)
screen_width = menu1_window.winfo_screenwidth()

screen_height = menu1_window.winfo_screenheight()

default_width = 1000  # 디폴트 너비, 높이
default_height = 750

# 타이틀(Solar Electricity Monitoring System)
menu1_window.title("(발전장소) 계측정보")

# 디폴트 사이즈 설정
menu1_window.geometry(f"{default_width}x{default_height}")

## 프레임 구분
frame_1 = ttk.Frame(menu1_window, relief="raised", height=100)
frame_1.pack(side="top", fill="both", padx=2, pady=2, expand=True)

## frame_1 내부 프레임 1
## 장소명
frame_1_1 = ttk.Frame(frame_1, relief="solid", height=50)
frame_1_1.pack(side="top", padx=10, fill="x", expand=True)

##lable 위젯 생성
place_name = ttk.Label(frame_1_1, text="OOO발전소 " + " 계측 정보")
place_name.pack(anchor="center", ipadx=5, ipady=5,
                fill="both", expand=True)

## place_name 위치 및 폰트 속성 설정
place_name.config(anchor="center", font=("한컴바탕", 24))

##frame_1의 내부 프레임 2
frame_1_2 = ttk.Frame(frame_1)
frame_1_2.pack(side="top", fill="both", expand=True, padx=10, pady=5)

## 기간 종류
type_select = ttk.Combobox(frame_1_2, values=["시간별", "일별", "월별"], width=20, state="readonly")
type_select.pack(side="left", padx=5)
type_select.set("시간별/일별/월별 선택")

##기간 종류 적용 버튼 위젯 생성
op_btr = ttk.Button(frame_1_2, text="적용", command=btr_1, width=15)
op_btr.pack(side="left", padx=5)

##출력 버튼 위젯 생성
output_btr = ttk.Button(frame_1_2, text="출력", command=out_btr)
output_btr.pack(side="right", padx=5)

## 계측종류 선택 프레임
type_select_1 = ttk.Combobox(frame_1_2, values=["발전량", "발전금액", "출력량"],  state="readonly")
type_select_1.pack(side="right", padx=5)
type_select_1.set("계측종류 선택")

##날짜 선택
##날짜입력 위젯생성
day_selete = DateEntry(frame_1_2, year=2021, month=12, day=2, date_pattern='yyyy/MM/dd', state="readonly")
day_selete.pack(side="right")
day_selete.bind("<<DateEntrySelected>>", print_sel)

##lable 위젯 생성
lable_name = ttk.Label(frame_1_2, text="날짜입력 : ")
lable_name.pack(side="right")

##그래프 출력 프레임
frame_2 = ttk.Frame(menu1_window, height=650, relief="solid")
frame_2.pack(side="top", fill="both", expand=True)

# 캔버스를 생성 , figsize -> 가로,세로 크기 조정
fig = plt.figure(figsize=(10, 10))

## 그래프 좌표 정의
ax = fig.add_subplot(111)

## 캔버스 정의
canvas = FigureCanvasTkAgg(fig, master=frame_2)

menu1_window.mainloop()
