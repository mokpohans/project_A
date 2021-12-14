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
    __temp_1 = None
    __temp_2 = None
    result = None
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

        self._error_select = ttk.Combobox(self._confirm_frame, values=['모듈 과부화', '인버터 운전상태 오류'], width=20)
        self._error_select.set('오류 종류 선택')
        self._error_select.configure(state='readonly')
        self._error_select.pack(side='left', padx=5)

        self._applybtn = ttk.Button(self._confirm_frame, text='적용', width=15, command=self._btn1)
        self._applybtn.pack(side='left', padx=5)



        ## 날짜 입력 위젯 생성
            # 출력 버튼 위젯 생성
        self._printbtn = ttk.Button(self._confirm_frame, text='출력', command=self._Get_Data)
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

    def _btn1(self):
        if (self._error_select.get() == '모듈 과부화'):
            self._f = 1
        elif (self._error_select.get() == '인버터 운전상태 오류'):
            self._f = 2
        else:
            messagebox.showerror('선택 오류', '오류 종류를 선택을 해주세요')


    def _Get_Data(self):
        self._start_Date = self._day_start.get_date()
        self._end_Date = self._day_end.get_date()
        self._btn1()
        self._place = CsvData.Period_Date(self._plant_df, str(self._start_Date), str(self._end_Date))
        self._error_table = CsvCreate.Error_Table_Create(self._place, self._f)
        self.out_btr()

        ## 출력 버튼 메소드
    def out_btr(self):
        ##대신data 변수
        ## 테이블 지우기
        self.data_table.clearTable()
        self.data_table.destroy()

        ##테이블 작성 부분
        self.data_table = Table(self._print_frame, dataframe=self._error_table.loc[
            : , ["측정일시", "장소", "인버터전류(R상)", "인버터전류(S상)", "인버터전류(T상)", "인버팅후 금일발전량", '외부온도(인버터단위)',
                           '모듈온도(인버터단위)']], height=600)

        self.data_table.show()
