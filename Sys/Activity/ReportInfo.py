## 보고서 메뉴
import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import DateEntry
import pandas as pd
from pandastable import Table
import CsvData
import CsvCreate
import datetime as dt

class ReportinfoPage:
    _window = None
    _windowtitle = ''
    _pagetitle = ''
    _plantname = ''
    _plant_df:pd.DataFrame = None

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

        self._default_time = self._plant_df['측정일시'][0]
        self._default_time_year = int(self._default_time[0:4])
        self._default_time_month = int(self._default_time[5:7])
        self._default_time_day = int(self._default_time[8:10])

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
        self._printbtn = ttk.Button(self._confirm_frame, text='출력')
        self._printbtn.pack(side='right', padx=5)

            # 날짜 입력 엔트리
        self._day_select = DateEntry(self._confirm_frame,
                                    year=self._default_time_year, month=self._default_time_month, day=self._default_time_day,
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

        self._data_table = Table(self._report_frame, dataframe=self._plant_df, height=600)
        self._data_table.show()


    ## 날짜선택 옵션 함수
    def btn_1(self):
        ## 기본 데이터 초기화
        self._day_select.delete(0, tk.END)
        if (self._type_select.get() == "시간별"):
            self._day_select.insert(0, "2021-08-00")
            self._lable_name.configure(text="날짜 [년도-월-일] 입력 : ")

        elif (type_select.get() == "일별"):
            day_selete.insert(0, "2021-00")
            lable_name.configure(text="날짜 [년도-월] 입력 : ")

        elif (type_select.get() == "월별"):
            day_selete.insert(0, "2000")
            lable_name.configure(text="날짜 [년도] 입력")

        else:
            day_selete.insert(0, "2021-08-01")
        day_selete.pack(side="right", padx=5)
