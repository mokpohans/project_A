#   GUI 메인 화면 구성입니다.
import tkinter as tk
from tkinter import ttk
from Sys.Components import AdditionalWidgets as adwz


class Mainpage:
    def __init__(self, page):
        self._mainpage = page
        self._mainpage.grid_propagate(False)
        self._mainpage.pack_propagate(False)
        self._mainpage.columnconfigure(index=0, weight=1)
        for i in range(0, 3, 1):
            self._mainpage.rowconfigure(index=i, weight=1)
        self._mainpage.update()
        self._display_width = self._mainpage.winfo_screenwidth()
        self._display_height = self._mainpage.winfo_screenheight()
        self._window_width = self._mainpage.winfo_width()
        self._window_height = self._mainpage.winfo_height()

        print(self._display_width)
        print(self._display_height)
        print(self._window_width)
        print(self._window_height)


    def operate(self):
        #### 베이스 틀
            ### 메뉴, 시간, 날씨 포함하는 베이스 레이블
        self.menu_base_Frame = ttk.Frame(self._mainpage)
            ### 시간, 발전소 선택 베이스 레이블
        self.middle_base_Frame = ttk.Frame(self._mainpage) # 좌->우 순서
        self.middle_base_Frame.rowconfigure(index=0, weight=1)
        self.middle_base_Frame.columnconfigure(index=0, weight=1)
        self.middle_base_Frame.columnconfigure(index=1, weight=1)
        self.middle_base_Frame.grid_propagate(False)
        self.middle_base_Frame.pack_propagate(False)
            ### 발전량, 발전금액 등 상태 레이블을 포함하는 베이스 레이블
        self.content_base_Frame = ttk.Frame(self._mainpage)

        self.menu_base_Frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.middle_base_Frame.grid(row=1, column=0, sticky=tk.NSEW)
        ## 날씨 표현 레이블
        # self.weather_describe_label = ttk.Label(self._mainpage)
        # self.weather_describe_label.pack(expand=True)
        self.content_base_Frame.grid(row=2, column=0, sticky=tk.NSEW)

        ### 메뉴 베이스 채우기
            # 메뉴 선택 레이블
        self.menu_label = ttk.Label(self.menu_base_Frame, width=self._window_width)
        self.menus = adwz.linearmenu(self.menu_label, 3, texts=['계측정보', '보고서', '장애목록'])

            # 시간 관련 베이스 레이블
        self.time_base_frame = ttk.Frame(self.middle_base_Frame)
        self.time_base_frame.pack_propagate(False)
        self.time_base_frame.grid_propagate(False)
        self.timepart_label = ttk.Label(self.time_base_frame)
#테스팅
        self.timepart = adwz.temp_Dclock(self.timepart_label, width=1000, height=100)

        # self.timepart = adwz.tempweather(self.time_base_label, 'test', width=300, height=300)
        # self.timeprint = adwz.timeprinter(self.time_base_label, width=self.time_base_label.winfo_width(), fit=False)
        # self.test_clock = adwz.temp_digitalclock(self.time_base_label, width=int(self._window_width/2), height=int(self._window_height/24))
#테스팅

            # 발전소 선택 레이블
        self.plantselect_base_frame = ttk.Frame(self.middle_base_Frame)
        self.plantselect_base_frame.pack_propagate(False)
        self.plantselect_base_frame.grid_propagate(False)
        self.plant_select_label = ttk.Label(self.plantselect_base_frame)
#테스팅
        self.temp_plant = adwz.temp_imagechooser(self.plant_select_label, image='./Resources/images/temp_bird.png', indications=['a', 'b', 'c'], anchor=tk.NE, width=700, height=int(self._mainpage.winfo_height()/3))
#테스팅

        self.time_base_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.plantselect_base_frame.grid(row=0, column=1, sticky=tk.NSEW)
        self.timepart_label.pack(expand=True)
        self.plant_select_label.pack(expand=True)
        self.menu_label.pack(expand=True, anchor=tk.E, ipadx=100)

        self.menus.create()
#테스팅
        self.timepart.create()
        # self.timeprint.create()
        # self.test_clock.create()
        self.temp_plant.create()
#테스팅

        ### 컨텐츠 베이스 채우기
            ## 발전 상태 레이블
        self.generate_state_label = ttk.Label(self.content_base_Frame)
            ## 인버터 상태 레이블
        self.invertor_state_label = ttk.Label(self.content_base_Frame)

        self.generate_state_label.pack(expand=True)
        self.invertor_state_label.pack(expand=True)

            # 발전량 레이블
        self.generate_quantity_label = ttk.Label(self.generate_state_label)
            # 발전금액 레이블
        self.generate_fee_label = ttk.Label(self.generate_state_label)
            # 출력량 레이블
        self.generate_emit_label = ttk.Label(self.generate_state_label)

        self.generate_quantity_label.pack(expand=True)
        self.generate_fee_label.pack(expand=True)
        self.generate_emit_label.pack(expand=True)

            # 인버터 1 레이블
        self.invertor_1_label = ttk.Label(self.invertor_state_label)
            # 인버터 2 레이블
        self.invertor_2_label = ttk.Label(self.invertor_state_label)
            # 인버터 3 레이블
        self.invertor_3_label = ttk.Label(self.invertor_state_label)
            # 모듈 온도 레이블
        self.module_temper_label = ttk.Label(self.invertor_state_label)

        self.invertor_1_label.pack(expand=True)
        self.invertor_2_label.pack(expand=True)
        self.invertor_3_label.pack(expand=True)
        self.module_temper_label.pack(expand=True)

        # self.test = AdditionalWidgets.KVlabel(self.invertor_1_label, type='readonly', key_text='test1', value_text='test2')
        # self.test.create()