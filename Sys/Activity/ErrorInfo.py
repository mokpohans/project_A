## 장애목록
import tkinter as tk
import tkinter.ttk as ttk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandastable import Table
import CsvCreate
import CsvData

class ErrorInfoPage:
    _window = None
    _windowtitle = ''
    _pagetitle = ''
    _plantname = ''
    _plant_df: pd.DataFrame = None

    # _default_time = None
    # _default_time_year = None
    # _default_time_month = None
    # _default_time_day = None

    cal_start = 'start'
    cal_end = 'end'

    data_table = None
    data = None

    font_path = "C:/Windows/Fonts/GULIM.TTC"
    # font = font_manager.FontProperties(fname=font_path).get_name()

    def __init__(self, window, windowtitle='', pagetitle='', plantname=''):
        self._window = window
        self._windowtitle = windowtitle
        self._pagetitle = pagetitle
        self._plantname = plantname

        self._plant_df = CsvCreate.Matching_Place_csv(self._plantname)

        # self._default_time = self._plant_df['측정일시'][0]
        # self._default_time_year = int(self._default_time[0:4])
        # self._default_time_month = int(self._default_time[5:7])
        # self._default_time_day = int(self._default_time[8:10])

        # print(f'sliced => {self._default_time_year}, {self._default_time_month}, {self._default_time_day}')

        # 윈도우 너비, 높이
        self._window_width = self._window.winfo_screenwidth()
        self._window_height = self._window.winfo_screenheight()
        # 디폴트 너비, 높이
        self._default_width = 1280
        self._default_height = 960

        self._window.geometry(f"{self._window_width}x{self._window_height}")

        if (self._windowtitle != ''):
            self._window.title(self._windowtitle)

        print(f'in MeasureInfo; plantname : {self._plantname} check')

    def operate(self):
        self._baseframe = ttk.Frame(self._window)
        self._baseframe.pack_propagate(False)
        self._baseframe.grid_propagate(False)
        self._baseframe.pack(side='top', fill='both', padx=2, pady=2, expand=True)

        ## 프레임 구분 ( 타이틀 베이스 )
        self._title_base_frame = ttk.Frame(self._baseframe, relief='raised', height=100)
        self._title_base_frame.pack(side='top', fill='both', padx=2, pady=2, expand=True)

        ## 타이틀 담당 프레임
        # 발전소명
        self._title_frame = ttk.Frame(self._title_base_frame, relief='solid', height=50)
        self._title_frame.pack(side='top', padx=10, fill='x', expand=True)

        # 발전소 명시 라벨 생성
        self._placename_label = ttk.Label(self._title_frame, text=self._plantname + ' 보고서')
        self._placename_label.pack(anchor='center', ipadx=5, ipady=5, fill='both', expand=True)
        # 폰트, 위치 등 설정
        self._placename_label.config(anchor='center', font=(self.font_path, 24))

        ## 기간설정 및 출력 버튼 프레임
        self._confirm_frame = ttk.Frame(self._title_base_frame)
        self._confirm_frame.pack(side="top", fill='both', expand=True, padx=10, pady=5)

        ## 날짜 입력 위젯 생성
            # 출력 버튼 위젯 생성
        self._printbtn = ttk.Button(self._confirm_frame, text='출력')
        self._printbtn.pack(side='right', padx=5)

        ##날짜 범위 끝
        self._day_end = ttk.Entry(self._confirm_frame, text=self.cal_end, width=20)
        self._day_end.insert(0, self.cal_end)
        self._day_end.pack(side="right")

        ## "~"
        self._in_instans = ttk.Label(self._confirm_frame, text=' ~ ')
        self._in_instans.pack(side="right", padx=5)
        self._in_instans.configure(state='readonly')

        ##날짜 범위 시작
        self._day_start = ttk.Entry(self._confirm_frame, text=self.cal_start, width=20)
        self._day_start.insert(0, self.cal_start)
        self._day_start.pack(side="right")

        ## 텍스트 라벨 생성
        self._label_name = ttk.Label(self._confirm_frame, text='날짜입력 :')
        self._label_name.pack(side="right")

        ##장애목록 출력 프레임
        self._print_frame = ttk.Frame(self._window, height=600, relief='solid')
        self._print_frame.pack(side="top", fill='both', expand=True)

        self.data_table = Table(self._print_frame, dataframe=self._plant_df, height=600)
        self.data_table.show()