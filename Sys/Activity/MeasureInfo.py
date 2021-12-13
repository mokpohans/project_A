#계측 정보에 대한 GUI 구성
import tkinter as tk
from tkinter import ttk
from Sys.Components import AdditionalWidgets as adwz
import datetime
from tkinter import messagebox
import CsvData
import CsvCreate
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import DateEntry
from matplotlib import font_manager, rc

from matplotlib.figure import Figure

class MeasureinfoPage:
    _window = None
    _plantname = ''
    _timeinfo = ''
    _windowtitle = ''
    _pagetitle = ''
    _Xlable= ''
    _Ylable = ''
    _Day = ''

    _day = None
    _i = None
    _count = None
    _Data = None
    _value = None
    _Place = None
    font_path = "C:/Windows/Fonts/GULIM.TTC"
    font = font_manager.FontProperties( fname = font_path ).get_name()
    rc('font', family=font)


    def __init__(self, window, windowtitle='', pagetitle='', plantname='', timeinfo=''):

        self._window = window
        self._window.grid_propagate(False)
        self._window.pack_propagate(False)
        self._window.update()
        self._windowtitle = windowtitle
        self._pagetitle = pagetitle
        self._plantname = plantname
        self._Place = CsvCreate.Matching_Place_csv(plantname)
        self._timeinfo = timeinfo

        #윈도우 너비, 높이
        self._window_width = self._window.winfo_screenwidth()
        self._window_height = self._window.winfo_screenheight()
        #디폴트 너비, 높이
        self._default_width = 1280
        self._default_height = 960

        self._window.geometry(f"{self._window_width}x{self._window_height}")

        if(self._windowtitle != ''):
            self._window.title(self._windowtitle)

        print(f'in MeasureInfo; plantname : {self._plantname}, timeinfo : {self._timeinfo} check')

        self._day = datetime.date.today()

    def operate(self):
        self._baseframe = ttk.Frame(self._window)
        self._baseframe.pack_propagate(False)
        self._baseframe.grid_propagate(False)
        self._baseframe.pack(side='top', fill='both', padx=2, pady=2, expand=True)

        ###타이틀 프레임
        self._title_baseframe = ttk.Frame(self._baseframe, relief='raised', height=100)
        self._title_baseframe.pack_propagate(False)
        self._title_baseframe.grid_propagate(False)
        self._title_baseframe.pack(side='top', fill='both', padx=2, pady=2, expand=True)

        ##타이틀담당 frame
        self._titleframe = ttk.Frame(self._title_baseframe, relief='solid', height=50)
        self._titleframe.pack(side='top', padx=10, fill='x', expand=True)

        #타이틀 위젯 생성
        self._titlelabel = ttk.Label(self._titleframe, text=f'{self._plantname} 계측 정보')
        self._titlelabel.pack(anchor='center', ipadx=5, ipady=5, fill='both', expand=True)
        #타이틀 위치 및 폰트 속성 설정
        self._titlelabel.config(anchor='center', font=('한컴바탕', 24))


        ###그래프 출력 프레임
        self._graph_print_frame = ttk.Frame(self._baseframe, height=650, relief='solid')
        self._graph_print_frame.pack(side='top', fill='both', expand=True)

        ##캔버스 생성, figsize => 가로, 세로 크기 조정
        self._fig = plt.figure(figsize=(10, 10))

        ## 그래프 좌표 정의
        self._ax = self._fig.add_subplot(111)
        self._ax_1 = self._ax.twinx()
        self._ax_2 = self._ax_1.twinx()
        ## 캔버스 정의
        self._canvas = FigureCanvasTkAgg(self._fig, master=self._graph_print_frame)

        ##기간 설정 프레임
        self._timeconfigframe = ttk.Frame(self._title_baseframe)
        self._timeconfigframe.pack(side='top', fill='both', expand=True, padx=10, pady=5)


        ### 타이틀 프레임 채우기
        #기간 종류
        self._time_type_select = ttk.Combobox(self._timeconfigframe, values=['시간별', '일별', '월별'], width=20, state='readonly')
        self._time_type_select.pack(side='left', padx=5)
        self._time_type_select.set('시간별/일별/월별 선택')

        #기간 종류 적용 버튼 위젯 생성
        self._confirm_btn = ttk.Button(self._timeconfigframe, text='적용', width=15)
        self._confirm_btn.pack(side='left', padx=5)

        ##계측 출력 버튼 위젯 생성
        self._print_btn = ttk.Button(self._timeconfigframe, text='출력')
        self._print_btn.pack(side='right', padx=5)

        ##계측 종류 선택 part
        self._measure_type_select = ttk.Combobox(self._timeconfigframe, values=['발전량', '발전금액', '출력량'], state='readonly')
        self._measure_type_select.pack(side='right', padx=5)
        self._measure_type_select.set('계측종류 선택')

        ##날짜 선택 part
        self._dayselect = DateEntry(self._timeconfigframe, year=self._day.year,
                                    month=self._day.month, day=self._day.day, date_pattern='yyyy/MM/dd',
                                    state='readonly')
        self._dayselect.pack(side='right')
        self._dayselect.bind("<<DataEntrySelected>>")

        ##날짜 선택 text
        self._textlabel = ttk.Label(self._timeconfigframe, text="날짜 입력 :")
        self._textlabel.pack(side='right')

        self._confirm_btn.configure(command=lambda: self._btn1())
        self._print_btn.configure(command=lambda: self._Get_Data())

    def _Get_Data(self):
        self._Date = self._dayselect.get_date()
        self._Data = CsvCreate.Date_Day(CsvCreate.Matching_Place_csv(self._plantname), str(self._Date))
        try:
            if len(self._Data) == 0:
                messagebox.showerror("기간 오류", "해당 기간의 데이터가 없습니다.\n 다시 선택해주세요.")
        except TypeError:
            messagebox.showerror("기간 오류", "해당 기간의 데이터가 없습니다.\n 다시 선택해주세요.")
        else:
            self._out_btn()

    def _xlabel(self, time):
        if(time == 1):
            self.__max = 25
        elif(time == 2):
            self.__max = CsvData.Months(self._dayselect.get_date())+1
        elif(time == 3):
            self.__max = 13

        self.label = [i for i in range(1, self.__max)]
        self._count = self.__max
        return self.label

    def _out_btn(self):
        self._btn2()
        ## 전에 그려진 그래프 데이터 지우기
        self._ax.clear()
        self._ax_1.clear()
        self._ax_2.clear()
        ##막대 그래프 작성 부분##
        self._years = self._xlabel(self._i)
        self.x = np.arange(self._count - 1)
        self._ax.bar(self.x, self._value[0],  color='red')
        plt.xticks(self.x)

        self._ax.set_xlabel(self._Day + self._Xlable)
        self._ax.set_ylabel(self._Day + self._Ylable)

        self._ax.patch.set_visible(False)
        ##실선선 그래프 작성부분##

        if (self._measure_type_select.get() != '발전금액'):
            self._ax_1.plot(self.x, self._value[1], '-s', color='green', markersize=7, linewidth=5)
            self._ax_2.plot(self.x, self._value[2], color='blue', markersize=7, linewidth=5, alpha=0.7)
            self._ax_1.set_zorder(self._ax.get_zorder() + 10)
            self._ax_2.set_zorder(self._ax_1.get_zorder() + 10)
        else:
            pass
        ## 그래프를 캔버스에 그리기
        self._canvas.draw()
        self._canvas.get_tk_widget().pack(fill='both', expand=True)

    def _btn1(self):
        self._i = 0
        if(self._time_type_select.get() == '시간별'):
            self._i = 1
            self._Xlable = '시간 단위'
            self._Day = '금일'
        elif(self._time_type_select.get() == '일별'):
            self._i = 2
            self._Xlable = '일 단위'
            self._Day = '금월'
        elif(self._time_type_select.get() == '월별'):
            self._i = 3
            self._Xlable = '월 단위'
            self._Day = '금년'
        else:
            messagebox.showerror('선택 오류', '기간 선택을 해주세요')

    def _btn2(self):
        self._day = self._dayselect.get_date()
        if(self._measure_type_select.get() == '발전량'):
            self._data = '인버팅후 금일발전량'
            self._Ylable = '발전량'
        elif(self._measure_type_select.get() == '발전금액'):
            self._data = '인버팅후 누적발전량'
            self._Ylable = '발전 금액'
        elif(self._measure_type_select.get() == '출력량'):
            self._data = '인버팅후 인버터전력'
            self._Ylable = '출력량'
        else:
            messagebox.showerror('선택 오류', '계측종류를 선택해주세요')
        self._value = CsvCreate.TransF_Date(CsvCreate.Matching_Place_csv(self._plantname), str(self._day), str(self._data), self._i)