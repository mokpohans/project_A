#   GUI 메인 화면 구성입니다.
import tkinter as tk
from tkinter import ttk

import CsvCreate
from Sys.Components import AdditionalWidgets as adwz
from Sys.Activity import MeasureInfo as msi
from Sys.Activity import ReportInfo as rpi
from Sys.Activity import ErrorInfo as eri
import CsvData

class Mainpage:
    _inverts = []
    _generates = []

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

        self.defaultStyle = ttk.Style()
        self.defaultStyle.configure("defaultBackground.TFrame",
                                    background='ivory')

        print(self._display_width)
        print(self._display_height)
        print(self._window_width)
        print(self._window_height)


    def operate(self):
        #### 베이스 틀
            ### 메뉴, 시간, 날씨 포함하는 베이스 레이블
        self._mainpage.rowconfigure(index=0, weight=1)
        self.menu_base_Frame = ttk.Frame(self._mainpage, style="defaultBackground.TFrame")
            ### 시간, 발전소 선택 베이스 레이블
        self._mainpage.rowconfigure(index=1, weight=3)
        self.middle_base_Frame = ttk.Frame(self._mainpage, style="defaultBackground.TFrame") # 좌->우 순서
            ### 발전량, 발전금액 등 상태 레이블을 포함하는 베이스 레이블
        self._mainpage.rowconfigure(index=2, weight=3)
        self.content_base_Frame = ttk.Frame(self._mainpage, style="defaultBackground.TFrame")

        self.menu_base_Frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.middle_base_Frame.grid(row=1, column=0, sticky=tk.NSEW)
        self.content_base_Frame.grid(row=2, column=0, sticky=tk.NSEW)

        ### 메뉴 베이스 채우기
            # 메뉴 선택 레이블
        self.menu_label = ttk.Label(self.menu_base_Frame, width=self._window_width, background='ivory')
        self.menus = adwz.linearmenu(self.menu_label, 3, index='menus', texts=['계측정보', '보고서', '장애목록'])

        self.menu_label.pack(expand=True, anchor=tk.E, ipadx=100)
        self.menus.create()

        # self.menus.elementManipulate(index=0, command=None) # command에 들어갈 함수 만들어서 내용 수정할 것.
        # self.menus.elementManipulate(index=0, command=lambda: self.test_change())
        self.menus.elementManipulate(index='menus', seq=0, command=self.Wake_MeasureInfo)
        self.menus.elementManipulate(index='menus', seq=1, command=self.Wake_ReportInfo)
        self.menus.elementManipulate(index='menus', seq=2, command=self.Wake_ErrorInfo)

        # print(f'in Minapage, locals() print : {locals()}')

        ### 미들 베이스 채우기
         #미들 베이스 칸 배분
        self.middle_base_Frame.rowconfigure(index=0, weight=1)
        self.middle_base_Frame.columnconfigure(index=0, weight=1)
        self.middle_base_Frame.columnconfigure(index=1, weight=1)
        self.middle_base_Frame.grid_propagate(False)
        self.middle_base_Frame.pack_propagate(False)
            # 시간 관련 베이스 생성
        self.time_base_frame = ttk.Frame(self.middle_base_Frame, style="defaultBackground.TFrame")
        self.time_base_frame.pack_propagate(False)
        self.time_base_frame.grid_propagate(False)
        self.timepart_label = ttk.Label(self.time_base_frame)
#테스팅
        self.timepart = adwz.temp_Dclock(self.timepart_label, width=1000, height=500,
                                         frameBG="defaultBackground.TFrame",
                                         images=['./Resources/images/dayNnight/day_small.png', './Resources/images/dayNnight/night001.png'])

        # self.timepart = adwz.tempweather(self.time_base_label, 'test', width=300, height=300)
        # self.timeprint = adwz.timeprinter(self.time_base_label, width=self.time_base_label.winfo_width(), fit=False)
        # self.test_clock = adwz.temp_digitalclock(self.time_base_label, width=int(self._window_width/2), height=int(self._window_height/24))
#테스팅

            # 발전소 선택 레이블
        self.plantselect_base_frame = ttk.Frame(self.middle_base_Frame, style="defaultBackground.TFrame")
        self.plantselect_base_frame.pack_propagate(False)
        self.plantselect_base_frame.grid_propagate(False)
        self.plant_select_label = ttk.Label(self.plantselect_base_frame, background='#cfffe5') # 민트색 : #cfffe5
        self.plantselect_base_frame.update()
        print(f'plant_select_base_frame is {self.plantselect_base_frame.winfo_width()} x {self.plantselect_base_frame.winfo_height()}')

        self.plant_choose = adwz.imagechooser(self.plant_select_label,
                                              images=['./Resources/images/plants/P001_JH_SolarPlant.png', './Resources/images/plants/P002_TG_SolarPlant.png'
                                                  , './Resources/images/plants/P003_SCH_SolarPlant.png', './Resources/images/plants/P004_G1C_SolarPlant.png'
                                                  , './Resources/images/plants/P005_G2C_SolarPlant.png', './Resources/images/plants/P006_G3C_SolarPlant.png'
                                                  , './Resources/images/plants/P007_PG_SolarPlant.png', './Resources/images/plants/P008_YS_SolarPlant.png'
                                                  , './Resources/images/plants/P009_B1P_SolarPlant.png', './Resources/images/plants/P010_B2P_SolarPlant.png'],
                                              indications=['정선한교', '태곡태양광발전소', '서천태양광발전소', '광양항 제1자전거도로 태양광발전소',
                                                           '광양항 제2자전거도로 태양광발전소', '광양항 제3자전거도로 태양광발전소', '판교가압장 태양광발전소',
                                                           '양산 태양광발전소', '분당지사 제1호 주차장 태양광발전소', '분당지사 제2호 주차장 태양광발전소'],
                                              anchor=tk.NE, width=950, height=int(self._mainpage.winfo_height()/2))


        self.time_base_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.plantselect_base_frame.grid(row=0, column=1, sticky=tk.NSEW)
        self.timepart_label.pack(expand=True, anchor=tk.E)
        self.plant_select_label.pack(expand=True, anchor=tk.W)

#테스팅
        self.timepart.create()

#테스팅
        self.plant_choose.create()

        ### 컨텐츠 베이스 채우기
         #컨텐츠 베이스 칸 할당
        self.content_base_Frame.grid_propagate(False)
        self.content_base_Frame.pack_propagate(False)
        self.content_base_Frame.rowconfigure(index=0, weight=1)
        self.content_base_Frame.rowconfigure(index=1, weight=1)
        self.content_base_Frame.columnconfigure(index=0, weight=1)
            ## 발전 상태 프레임
        self.generate_state_frame = ttk.Frame(self.content_base_Frame, style="defaultBackground.TFrame")
            ## 인버터 상태 프레임
        self.invertor_state_frame = ttk.Frame(self.content_base_Frame, style="defaultBackground.TFrame")

        self.generate_state_frame.grid(row=0, column=0, sticky=tk.NSEW, pady=5)
        self.invertor_state_frame.grid(row=1, column=0, sticky=tk.NSEW, pady=5)

        ##발전량, 발전금액, 출력량 채우기
        self.generate_state_frame.grid_propagate(False)
        self.generate_state_frame.pack_propagate(False)
        for i in range(0, 4):
            self.generate_state_frame.rowconfigure(index=i, weight=1)
        self.generate_state_frame.columnconfigure(index=0, weight=1)
            # 발전량 레이블
        self.generate_quantity_label = ttk.Label(self.generate_state_frame, background='ivory')
            # 발전금액 레이블
        self.generate_fee_label = ttk.Label(self.generate_state_frame, background='ivory')
            # 출력량 레이블
        self.generate_emit_label = ttk.Label(self.generate_state_frame, background='ivory')

            # 인덱스와 상태들 보이기
        self.generate_index_label = ttk.Label(self.generate_state_frame, background='#cfffe5') # 민트색 : #cfffe5
        self.generate_indexs = adwz.linearmenu(self.generate_index_label, partitions=4, index='invert_indexs', texts=['', '일간', '월간', '누적'], width=1100, height=50)
        self.generate_quanitiy_state = adwz.linearmenu(self.generate_quantity_label, partitions=4, index='발전량', texts=['발전량', '0', '0', '0'], width=1100, height=50)
        self.generate_fee_state = adwz.linearmenu(self.generate_fee_label, partitions=4, index='발전금액', texts=['발전금액', '0', '0', '0'], width=1100, height=50)
        self.generate_emit_state = adwz.linearmenu(self.generate_emit_label, partitions=4, index='현재출력량', texts=['현재출력량', '0', '', ''], width=1100, height=50)

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
        self.index_label = ttk.Label(self.invertor_state_frame, background='ivory') # 민트색 : #cfffe5
            # 인버터 1 레이블
        self.invertor_1_label = ttk.Label(self.invertor_state_frame, background='ivory')
            # 인버터 2 레이블
        self.invertor_2_label = ttk.Label(self.invertor_state_frame, background='ivory')
            # 인버터 3 레이블
        self.invertor_3_label = ttk.Label(self.invertor_state_frame, background='ivory')
            # 모듈 온도 레이블
        self.module_temper_label = ttk.Label(self.invertor_state_frame, background='ivory')

        self.index_label.grid(row=0, column=0, sticky=tk.NSEW)
        self.invertor_1_label.grid(row=1, column=0, sticky=tk.NSEW)
        self.invertor_2_label.grid(row=2, column=0, sticky=tk.NSEW)
        self.invertor_3_label.grid(row=3, column=0, sticky=tk.NSEW)
        self.module_temper_label.grid(row=4, column=0, sticky=tk.NSEW)

        self.indexstate_content = adwz.KVlabel(self.index_label, type='readonly',
                                               key_text='index', value_text='state', width=self._mainpage.winfo_width())
        self.invertor1_content = adwz.KVlabel(self.invertor_1_label, type='showcase', key_text='invertor 1',
                                              images=['./Resources/images/invertor_light/invertor_null.png',
                                                      './Resources/images/invertor_light/invertor_green.png',
                                                      './Resources/images/invertor_light/invertor_red.png'],
                                              width=self._mainpage.winfo_width())
        self.invertor2_content = adwz.KVlabel(self.invertor_2_label, type='showcase', key_text='invertor 2',
                                              images=['./Resources/images/invertor_light/invertor_null.png',
                                                      './Resources/images/invertor_light/invertor_green.png',
                                                      './Resources/images/invertor_light/invertor_red.png'],
                                              width=self._mainpage.winfo_width())
        self.invertor3_content = adwz.KVlabel(self.invertor_3_label, type='showcase', key_text='invertor 3',
                                              images=['./Resources/images/invertor_light/invertor_null.png',
                                                      './Resources/images/invertor_light/invertor_green.png',
                                                      './Resources/images/invertor_light/invertor_red.png'],
                                              width=self._mainpage.winfo_width())
        self.moduletemper_content = adwz.KVlabel(self.module_temper_label, type='readonly',
                                                 key_text='module temperature', value_text='state', width=self._mainpage.winfo_width())

        self.indexstate_content.create(padx=135)
        self.invertor1_content.create(padx=135)
        self.invertor2_content.create(padx=135)
        self.invertor3_content.create(padx=135)
        self.moduletemper_content.create(padx=135)

        self.test_live_timechecker()

    ## 메뉴1번 계측정보 열기(Toplevel)
    def Wake_MeasureInfo(self):
        self.MSI_toplevel = tk.Toplevel(self._mainpage, width=self._display_width, height=self._display_height)
                                     #
        self.MSI_toplevel.grab_set() #toplevel_id.grab_set() 해야지 메인윈도우와 탑레벨간 이벤트, 매개변수 상호작용이 가능하다.
                                     #
        measureinfo = msi.MeasureinfoPage(window=self.MSI_toplevel, windowtitle=self.plant_choose.getPlantName() + '계측정보', pagetitle='계측정보',
                                          plantname=self.plant_choose.getPlantName(), timeinfo=self.timepart.getTimeInfo())
        measureinfo.operate()

    ## 메뉴2번 보고서 열기(Toplevel)
    def Wake_ReportInfo(self):
        self.RPI_toplevel = tk.Toplevel(self._mainpage, width=self._display_width, height=self._display_height)
                                     #
        self.RPI_toplevel.grab_set() #toplevel_id.grab_set() 해야지 메인윈도우와 탑레벨간 이벤트, 매개변수 상호작용이 가능하다.
                                     #
        reportinfo = rpi.ReportinfoPage(window=self.RPI_toplevel, windowtitle=self.plant_choose.getPlantName() + ' 보고서', pagetitle='보고서',
                                        plantname=self.plant_choose.getPlantName())
        reportinfo.operate()

    def Wake_ErrorInfo(self):
        self.ERI_toplevel = tk.Toplevel(self._mainpage, width=self._display_width, height=self._display_height)
                                     #
        self.ERI_toplevel.grab_set() #toplevel_id.grab_set() 써야 메인윈도우와 탑레벨간 이벤트, 매개변수 상호작용이 가능하다.
                                     #
        errorinfo = eri.ErrorInfoPage(window=self.ERI_toplevel, windowtitle=self.plant_choose.getPlantName() + ' 장애 목록', pagetitle='장애목록',
                                      plantname=self.plant_choose.getPlantName())
        errorinfo.operate()
# 테스팅
    def test_live_timechecker(self):
        # print(f"live time checking : {self.timepart.getTimeInfo()} & live location chekcing : {self.plant_choose.getPlantName()}")
        # self._invert_R, self._invert_S, self._invert_T = CsvData.Get_RST_InvertState(time=self.timepart.getTimeInfo(), plantname=self.plant_choose.getPlantName())
        self._generates = CsvData.Get_Generate_State(time=self.timepart.getTimeInfo(), plantname=self.plant_choose.getPlantName())
        print(self._generates)
        #발전량, 발전금액, 출력량 부분
        self.generate_quanitiy_state.elementManipulate(index='발전량', seq=1, text=self._generates[0])
        self.generate_quanitiy_state.elementManipulate(index='발전량', seq=2, text=self._generates[3])
        self.generate_quanitiy_state.elementManipulate(index='발전량', seq=3, text=self._generates[5])
        self.generate_fee_state.elementManipulate(index='발전금액', seq=1, text=self._generates[1])
        self.generate_fee_state.elementManipulate(index='발전금액', seq=2, text=self._generates[4])
        self.generate_fee_state.elementManipulate(index='발전금액', seq=3, text=self._generates[6])
        self.generate_emit_state.elementManipulate(index='현재출력량', seq=1, text=self._generates[2])

        self._inverts = CsvData.Get_RST_InvertState(time=self.timepart.getTimeInfo(), plantname=self.plant_choose.getPlantName())
        #인버터 상태표시등
        self.invertor1_content.showcase_configure(index=self._inverts[0])
        self.invertor2_content.showcase_configure(index=self._inverts[1])
        self.invertor3_content.showcase_configure(index=self._inverts[2])

        # 약 20초마다 검사(딱 20초면 실행되는데 소모되는 시간때문에 문제가 생길 수 있음)
        self.test_live_timecheck = self.content_base_Frame.after(980, self.test_live_timechecker)


    def msi_closing(self):
        self.MSI_toplevel.quit()

        self.MSI_toplevel.protocol("WM_DELETE_WINDOW", self.msi_closing)

    def rpi_closing(self):
        self.RPI_toplevel.quit()

        self.RPI_toplevel.protocol("WM_DELETE_WINDOW", self.rpi_closing)

    def eri_closing(self):
        self.ERI_toplevel.quit()

        self.ERI_toplevel.protocol("WM_DELETE_WINDOW", self.eri_closing)
#테스팅