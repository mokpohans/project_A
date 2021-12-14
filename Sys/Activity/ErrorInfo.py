## 장애목록
import tkinter.ttk as ttk
from datetime import datetime
from tkinter import messagebox

import pandas as pd
from pandastable import Table
import CsvCreate
from tkcalendar import DateEntry

import CsvData


class ErrorInfoPage:
    _window = None
    _windowtitle = ''
    _pagetitle = ''
    _plantname = ''
    _plant_df: pd.DataFrame = None

    cal_start = 'start'
    cal_end = 'end'

    data_table = None
    data = None

    font_path = "C:/Windows/Fonts/GULIM.TTC"

    def __init__(self, window, windowtitle='', pagetitle='', plantname=''):
        self._window = window
        self._windowtitle = windowtitle
        self._pagetitle = pagetitle
        self._plantname = plantname

        self._plant_df = CsvCreate.Matching_Place_csv(self._plantname)


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

        self._st_time = CsvData.Csv_First_Date(self._plantname)
        self._start_day = datetime.strptime(self._st_time[0], '%Y-%m-%d')
        self._ed_time = CsvData.Csv_Last_Date(self._plantname)
        self._end_day = datetime.strptime(self._ed_time[-1], '%Y-%m-%d')

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
        self._placename_label = ttk.Label(self._title_frame, text=self._plantname + ' 오류 목록')
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
        self._day_end = DateEntry(self._confirm_frame,year=self._end_day.year,month=self._end_day.month, day=self._end_day.day,
                                    date_pattern='yyyy/MM/dd',state="readonly")
        self._day_end.pack(side="right")

        ## "~"
        self._in_instans = ttk.Label(self._confirm_frame, text=' ~ ')
        self._in_instans.pack(side="right", padx=5)
        self._in_instans.configure(state='readonly')

        ##날짜 범위 시작
        self._day_start = DateEntry(self._confirm_frame,year=self._start_day.year,month=self._start_day.month, day=self._start_day.day,
                                    date_pattern='yyyy/MM/dd',state="readonly")
        self._day_start.pack(side="right")

        ## 텍스트 라벨 생성
        self._label_name = ttk.Label(self._confirm_frame, text='날짜입력 :')
        self._label_name.pack(side="right")

        ##장애목록 출력 프레임
        self._print_frame = ttk.Frame(self._window, height=600, relief='solid')
        self._print_frame.pack(side="top", fill='both', expand=True)

        self.data_table = Table(self._print_frame, dataframe=self._plant_df, height=600)
        self.data_table.show()

    def _Get_Data(self):
        self._Date = self._day_start.get_date()
        self._Data = CsvCreate.Date_Day(CsvCreate.Matching_Place_csv(self._plantname), str(self._Date))
        self._Date = self._day_start.get_date()
        self._Data = CsvCreate.Date_Day(CsvCreate.Matching_Place_csv(self._plantname), str(self._Date))
        try:
            if len(self._Data) == 0:
                messagebox.showerror("기간 오류", "해당 기간의 데이터가 없습니다.\n 다시 선택해주세요.")
        except TypeError:
            messagebox.showerror("기간 오류", "해당 기간의 데이터가 없습니다.\n 다시 선택해주세요.")
        else:
            self._out_btn()