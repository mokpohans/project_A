## 보고서 메뉴
import datetime
import tkinter.ttk as ttk
from tkinter import messagebox

from tkcalendar import DateEntry
import pandas as pd
from pandastable import Table
import CsvData
import CsvCreate
from datetime import datetime

class ReportinfoPage:
    _window = None
    _windowtitle = ''
    _pagetitle = ''
    _plantname = ''
    _plant_df:pd.DataFrame = None
    _place : pd.DataFrame = None

    _i = None
    _default_time = None
    _default_time_year = None
    _default_time_month = None
    _default_time_day = None

    data_table = None
    data = None
    df = None

    font_path = "C:/Windows/Fonts/GULIM.TTC"
    # font = font_manager.FontProperties(fname=font_path).get_name()

    def __init__(self, window, windowtitle='', pagetitle='', plantname=''):
        self._window = window
        self._windowtitle = windowtitle
        self._pagetitle = pagetitle
        self._plantname = plantname

        self._plant_df = CsvCreate.Matching_Place_csv(self._plantname)

        print(f'sliced => {self._default_time_year}, {self._default_time_month}, {self._default_time_day}')

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
        self.str = CsvData.Csv_First_Date(self._plantname)
        self._day = datetime.strptime(self.str, '%Y-%m-%d')

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
        self._placename_label.config(anchor='center', font=("C:/Windows/Fonts/GULIM.TTC", 24))

        ## 기간설정 및 출력 버튼 프레임
        self._confirm_frame = ttk.Frame(self._title_base_frame)
        self._confirm_frame.pack(side='top', fill='both', expand=True, padx=10, pady=5)

            # 기간 종류
        self._type_select = ttk.Combobox(self._confirm_frame, values=['시간별', '일별', '월별'], width= 20)

        self._type_select.set('시간별/일별/월별 선택')
        self._type_select.configure(state='readonly')
        self._type_select.pack(side='left', padx=5)

            #기간 종류 적용 버튼 위젯 생성
        self._applybtn = ttk.Button(self._confirm_frame, text='적용', width=15)
        self._applybtn.pack(side='left', padx=5)

        ## 날짜 선택
            # 출력 버튼 위젯 생성
        self._printbtn = ttk.Button(self._confirm_frame, text='출력', command = self._btn1)
        self._printbtn.pack(side='right', padx=5)

            # 날짜 입력 엔트리
        self._day_select = DateEntry(self._confirm_frame,
                                     year=self._day.year,month=self._day.month, day=self._day.day,
                                    date_pattern='yyyy/MM/dd',
                               state="readonly")
        self._day_select.pack(side="right")
        self._day_select.bind("<<DateEntrySelected>>")

            ##날짜입력 라벨 생성
        self._lable_name = ttk.Label(self._confirm_frame, text="날짜입력 : ")
        self._lable_name.pack(side="right")

        ##보고서 출력 프레임
        self._report_frame = ttk.Frame(self._baseframe, height=600, relief="solid")
        self._report_frame.pack(side="top", fill="both", expand=True)



    ## 날짜선택 옵션 함수
    def _btn1(self):
        self._i = 0
        if(self._type_select.get() == '시간별'):
            self._i = 1
        elif(self._type_select.get() == '일별'):
            self._i = 2
        elif(self._type_select.get() == '월별'):
            self._i = 3
        else:
            messagebox.showerror('선택 오류', '기간 선택을 해주세요')
        self._Date = self._day_select.get_date()
        self._place = CsvData.Trans_DF(self._plant_df, str(self._Date),self._i)
        self.out_table()

    def _Get_Data(self):
        self._Data = CsvCreate.Date_Day(CsvCreate.Matching_Place_csv(self._plantname), str(self._Date))
        try:
            if len(self._Data) == 0:
                messagebox.showerror("기간 오류", "해당 기간의 데이터가 없습니다.\n 다시 선택해주세요.")
        except TypeError:
            messagebox.showerror("기간 오류", "해당 기간의 데이터가 없습니다.\n 다시 선택해주세요.")
        else:
            self._btn1()

    def out_table(self):
        ## 테이블 지우기
        if self.data_table != None:
            self.data_table.clearTable()
            self.data_table.destroy()
        else:
            pass
        self.data_table = Table(self._report_frame, dataframe= self._place, height=600)
        self.data_table.show()