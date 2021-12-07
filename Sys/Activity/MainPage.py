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
        self._mainpage.rowconfigure(index=0, weight=1)
        self.menu_base_Frame = ttk.Frame(self._mainpage)
            ### 시간, 발전소 선택 베이스 레이블
        self._mainpage.rowconfigure(index=1, weight=1)
        self.middle_base_Frame = ttk.Frame(self._mainpage) # 좌->우 순서
            ### 발전량, 발전금액 등 상태 레이블을 포함하는 베이스 레이블
        self._mainpage.rowconfigure(index=2, weight=3)
        self.content_base_Frame = ttk.Frame(self._mainpage)

        self.menu_base_Frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.middle_base_Frame.grid(row=1, column=0, sticky=tk.NSEW)
        self.content_base_Frame.grid(row=2, column=0, sticky=tk.NSEW)

        ### 메뉴 베이스 채우기
            # 메뉴 선택 레이블
        self.menu_label = ttk.Label(self.menu_base_Frame, width=self._window_width)
        self.menus = adwz.linearmenu(self.menu_label, 3, texts=['계측정보', '보고서', '장애목록'])

        self.menu_label.pack(expand=True, anchor=tk.E, ipadx=100)
        self.menus.create()

        ### 미들 베이스 채우기
         #미들 베이스 칸 배분
        self.middle_base_Frame.rowconfigure(index=0, weight=1)
        self.middle_base_Frame.columnconfigure(index=0, weight=1)
        self.middle_base_Frame.columnconfigure(index=1, weight=1)
        self.middle_base_Frame.grid_propagate(False)
        self.middle_base_Frame.pack_propagate(False)
            # 시간 관련 베이스 생성
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

        self.plant_choose = adwz.imagechooser(self.plant_select_label, image='./Resources/images/temp_bird.png', indications=['a', 'b', 'c'], anchor=tk.NE, width=700, height=int(self._mainpage.winfo_height()/5))


        self.time_base_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.plantselect_base_frame.grid(row=0, column=1, sticky=tk.NSEW)
        self.timepart_label.pack(expand=True)
        self.plant_select_label.pack(expand=True)

#테스팅
        self.timepart.create()
#테스팅
        # self.timeprint.create()
        self.plant_choose.create()

        ### 컨텐츠 베이스 채우기
         #컨텐츠 베이스 칸 할당
        self.content_base_Frame.grid_propagate(False)
        self.content_base_Frame.pack_propagate(False)
        self.content_base_Frame.rowconfigure(index=0, weight=1)
        self.content_base_Frame.rowconfigure(index=1, weight=1)
        self.content_base_Frame.columnconfigure(index=0, weight=1)
            ## 발전 상태 프레임
        self.generate_state_frame = ttk.Frame(self.content_base_Frame)
            ## 인버터 상태 프레임
        self.invertor_state_frame = ttk.Frame(self.content_base_Frame)

        self.generate_state_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.invertor_state_frame.grid(row=1, column=0, sticky=tk.NSEW)

        ##발전량, 발전금액, 출력량 채우기
        self.generate_state_frame.grid_propagate(False)
        self.generate_state_frame.pack_propagate(False)
        for i in range(0,4):
            self.generate_state_frame.rowconfigure(index=i, weight=1)
        self.generate_state_frame.columnconfigure(index=0, weight=1)
            # 발전량 레이블
        self.generate_quantity_label = ttk.Label(self.generate_state_frame)
            # 발전금액 레이블
        self.generate_fee_label = ttk.Label(self.generate_state_frame)
            # 출력량 레이블
        self.generate_emit_label = ttk.Label(self.generate_state_frame)

            # 인덱스와 상태들 보이기
        self.generate_index_label = ttk.Label(self.generate_state_frame)
        self.generate_indexs = adwz.linearmenu(self.generate_index_label, partitions=4, texts=['', '일간', '월간', '누적'], width=800, height=50)
        self.generate_quanitiy_state = adwz.linearmenu(self.generate_quantity_label, partitions=4, texts=['발전량', '0', '0', '0'], width=800, height=50)
        self.generate_fee_state = adwz.linearmenu(self.generate_fee_label, partitions=4, texts=['발전금액', '0', '0', '0'], width=800, height=50)
        self.generate_emit_state = adwz.linearmenu(self.generate_emit_label, partitions=4, texts=['출력량', '0', '0', '0'], width=800, height=50)

        self.generate_index_label.grid(row=0, column=0)
        self.generate_quantity_label.grid(row=1, column=0)
        self.generate_fee_label.grid(row=2, column=0)
        self.generate_emit_label.grid(row=3, column=0)

        self.generate_indexs.create()
        self.generate_quanitiy_state.create()
        self.generate_fee_state.create()
        self.generate_emit_state.create()

            ## 인버터 상태 프레임 칸 배분
        self.invertor_state_frame.grid_propagate(False)
        self.invertor_state_frame.pack_propagate(False)
        for i in range(0, 5, 1):
            self.invertor_state_frame.rowconfigure(index=i, weight=1)
        self.invertor_state_frame.columnconfigure(index=0, weight=1)
        
            # [종류 : 상태]를 나타내는 인덱스 레이블
        self.index_label = ttk.Label(self.invertor_state_frame, text='index:state', background='red')
            # 인버터 1 레이블
        self.invertor_1_label = ttk.Label(self.invertor_state_frame, text='invertor1', background='yellow')
            # 인버터 2 레이블
        self.invertor_2_label = ttk.Label(self.invertor_state_frame, text='invertor2', background='green')
            # 인버터 3 레이블
        self.invertor_3_label = ttk.Label(self.invertor_state_frame, text='invertor3', background='blue')
            # 모듈 온도 레이블
        self.module_temper_label = ttk.Label(self.invertor_state_frame, text='module_temperature', background='violet')

        self.index_label.grid(row=0, column=0, sticky=tk.NSEW)
        self.invertor_1_label.grid(row=1, column=0, sticky=tk.NSEW)
        self.invertor_2_label.grid(row=2, column=0, sticky=tk.NSEW)
        self.invertor_3_label.grid(row=3, column=0, sticky=tk.NSEW)
        self.module_temper_label.grid(row=4, column=0, sticky=tk.NSEW)

        self.indexstate_content = adwz.KVlabel(self.index_label, type='readonly',
                                               key_text='index', value_text='state', width=self._mainpage.winfo_width())
        self.invertor1_content = adwz.KVlabel(self.invertor_1_label, type='showcase', key_text='invertor 1',
                                              image="./Resources/images/test_button_img.png",
                                              width=self._mainpage.winfo_width())
        self.invertor2_content = adwz.KVlabel(self.invertor_2_label, type='showcase', key_text='invertor 2',
                                              image="./Resources/images/test_button_img.png",
                                              width=self._mainpage.winfo_width())
        self.invertor3_content = adwz.KVlabel(self.invertor_3_label, type='showcase', key_text='invertor 3',
                                              image="./Resources/images/test_button_img.png",
                                              width=self._mainpage.winfo_width())
        self.moduletemper_content = adwz.KVlabel(self.module_temper_label, type='readonly',
                                                 key_text='module temperature', value_text='state', width=self._mainpage.winfo_width())

        self.indexstate_content.create(padx=80)
        self.invertor1_content.create(padx=80)
        self.invertor2_content.create(padx=80)
        self.invertor3_content.create(padx=80)
        self.moduletemper_content.create(padx=80)