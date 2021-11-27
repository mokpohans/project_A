#   GUI 메인 화면 구성입니다.
import tkinter as tk
from tkinter import ttk
from Sys.Components import AdditionalWidgets as adwz


class Mainpage:
    def __init__(self, page):
        self._mainpage = page
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
        self.menu_base_label = ttk.Label(self._mainpage, width=self._window_width)
            ### 시간, 발전소 선택 베이스 레이블
        self.middle_base_label = ttk.Label(self._mainpage) # 좌->우 순서
            ## 날씨 표현 레이블
        self.weather_describe_label = ttk.Label(self._mainpage)
            ### 발전량, 발전금액 등 상태 레이블을 포함하는 베이스 레이블
        self.content_base_label = ttk.Label(self._mainpage)

        self.menu_base_label.pack(expand=True)
        self.middle_base_label.pack(expand=True, anchor=tk.W)
        self.weather_describe_label.pack(expand=True)
        self.content_base_label.pack(expand=True)

        ### 메뉴 베이스 채우기
            # 메뉴 선택 레이블
        self.menu_label = ttk.Label(self.menu_base_label, width=self._window_width)
        self.menus = adwz.linearmenu(self.menu_label)

            # 시간 관련 베이스 레이블
        self.time_base_label = ttk.Label(self.middle_base_label)
            # 발전소 선택 레이블
        self.plant_select_label = ttk.Label(self.middle_base_label)

        self.menu_label.pack(expand=True, anchor='w', side='left')
        self.time_base_label.pack(expand=True, anchor='w')
        self.plant_select_label.pack(expand=True)

        self.menus.create()

        ### 컨텐츠 베이스 채우기
            ## 발전 상태 레이블
        self.generate_state_label = ttk.Label(self.content_base_label)
            ## 인버터 상태 레이블
        self.invertor_state_label = ttk.Label(self.content_base_label)

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