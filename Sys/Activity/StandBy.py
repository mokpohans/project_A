#   GUI 메인 화면 구성입니다.
import tkinter
from tkinter import ttk


class Standby:
    def __init__(self, page):
        self._mainpage = page
        # self._screenwidth = self._mainpage.winfo_screenwidth()
        # self._screenheight = self._mainpage.winfo_screenheight()

    def operate(self):
        #### 베이스 틀
            ### 메뉴, 시간, 날씨 포함하는 베이스 레이블
        self.menu_base_label = ttk.Label(self._mainpage)
            ### 시간, 발전소 선택 베이스 레이블
        self.middle_base_label = ttk.Label(self._mainpage, anchor='w') # 좌->우 순서
            ## 날씨 표현 레이블
        self.weather_describe_label = ttk.Label(self._mainpage)
            ### 발전량, 발전금액 등 상태 레이블을 포함하는 베이스 레이블
        self.content_base_label = ttk.Label(self._mainpage)

        self.menu_base_label.pack(expand=True)
        self.middle_base_label.pack(expand=True)
        self.weather_describe_label.pack(expand=True)
        self.content_base_label.pack(expand=True)

        ### 메뉴 베이스 채우기
            # 메뉴 선택 레이블
        self.menu_label = ttk.Label(self.menu_base_label)
            # 시간 관련 베이스 레이블
        self.time_base_label = ttk.Label(self.middle_base_label)
            # 발전소 선택 레이블
        self.plant_select_label = ttk.Label(self.middle_base_label)

        self.menu_label.pack(expand=True)
        self.time_base_label.pack(expand=True)
        self.plant_select_label.pack(expand=True)

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