import datetime
from tkinter import messagebox
import CsvData
import CsvCreate
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import DateEntry
from matplotlib.figure import Figure

global i, count, Data, value

day = datetime.date.today()

def Get_Data():
    global Data
    Date = day_selete.get_date()
    Data = CsvCreate.Date_Day(CsvCreate.Place_1, str(Date))
    try:
        if len(Data) == 0:
            messagebox.showerror("기간 오류", "해당 기간의 데이터가 없습니다.\n 다시 선택해주세요.")
    except TypeError:
        messagebox.showerror("기간 오류", "해당 기간의 데이터가 없습니다.\n 다시 선택해주세요.")
    else:
        out_btr()

## 공백 프레임 생성 메소드
def f_x(frame_name, x):
    instant_frame = ttk.Frame(frame_name)
    instant_frame.pack(side="right", padx=x)

def f_y(frame_name, y):
    instant_frame = ttk.Frame(frame_name)
    instant_frame.pack(side="top", padx=y)

def xlable(time):
    global count
    if time == 1 :
        __max = 25
    elif time == 2:
        __max = CsvData.Months(day_selete.get_date()) + 1
    elif time == 3:
        __max = 13
    lable = [i for i in range(1, __max)]
    count = __max
    return lable

## 출력 버튼 메소드
def out_btr():
    btr_2()
    ##전에 그려진 그래프 데이터 지우기
    ax.clear()

    ## 테스트 코드
    global i, count, value

    ##그래프 작성 부분####

    years = xlable(i)
    values = value

    x = np.arange(count - 1)
    plt.bar(x, values)
    plt.xticks(x, years)

    ax.set_xlabel("dice")

    ax.set_ylabel("relative frequency")
    ##그래프 작성 부분####

    ##그래프를 캔버스에 그리기
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

## 날짜선택 옵션 함수
def btr_1():
    global i
    i = 0
    if (type_select.get() == "시간별"):
        i = 1

    elif (type_select.get() == "일별"):
        i = 2

    elif (type_select.get() == "월별"):
        i = 3

    else:
        messagebox.showerror("선택 오류", "기간선택을 해주세요.")

def btr_2():
    global value
    day = day_selete.get_date()
    if (type_select_1.get() == "발전량"):
        data = '인버팅후 금일발전량'
    elif (type_select_1.get() == "발전금액"):
        data = '인버팅후 누적발전량'
    elif (type_select_1.get() == "출력량"):
        data = '인버팅후 인버터전력'
    else:
        messagebox.showerror("선택 오류", "계측종류를 해주세요.")
    value = CsvCreate.create_csv(CsvCreate.Place_1, str(day), str(data), i)

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
output_btr = ttk.Button(frame_1_2, text="출력", command=Get_Data)
output_btr.pack(side="right", padx=5)

## 계측종류 선택 프레임
type_select_1 = ttk.Combobox(frame_1_2, values=["발전량", "발전금액", "출력량"],  state="readonly")
type_select_1.pack(side="right", padx=5)
type_select_1.set("계측종류 선택")

##날짜 선택
##날짜입력 위젯생성
day_selete = DateEntry(frame_1_2, year=day.year, month=day.month, day= day.day ,date_pattern='yyyy/MM/dd', state="readonly")
day_selete.pack(side="right")
day_selete.bind("<<DateEntrySelected>>")

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