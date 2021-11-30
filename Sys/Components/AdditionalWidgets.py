import tkinter as tk
from tkinter import ttk
from datetime import datetime

class windowSizeHelper:
    _parent = None
    _mainpage = None
    _parent_width=0 # 부모위젯의 너비, 높이
    _parent_height=0
    _window_width=0 # tikinter 창의 너비, 높이
    _widnow_height=0
    _display_width=0 # 모니터 해상도의 너비, 높이
    _display_height=0

    def __init__(self, parent, root=None):
        self._parent = parent
        self._parent.update()
        self._parent_width = self._parent.winfo_width()
        self._parent_height = self._parent.winfo_height()

        if(root != None):
            self._mainpage = root
            self._mainpage.update()
            self._window_width = self._mainpage.winfo_width()
            self._window_height = self._mainpage.winfo_height()
            self._display_width = self._mainpage.winfo_screenwidth()
            self._display_height = self._mainpage.winfo_screenheight()
        elif(root == None):
            self._parent.update()
            self._window_width = self._parent_width
            self._window_height = self._parent_height
            self._display_width = self._parent.winfo_screenwidth()
            self._display_height = self._parent.winfo_screenheight()

    def getParentWidth(self):
        parentwidth = self._parent_width
        return parentwidth
    def getParentHeight(self):
        parentheight = self._parent_height
        return parentheight
    def getWindowWidth(self):
        windowwidth = self._window_width
        return windowwidth
    def getWindowHeight(self):
        windowheight = self._window_height
        return windowheight
    def getDisplayWidth(self):
        displaywidth = self._display_width
        return displaywidth
    def getDisplayHeight(self):
        displayheight = self._display_height
        return displayheight

class timeprinter: # 임시 시간 출력기
    _parent = None
    _printlabel = None
    _width = 0
    _height = 0
    _format = "default"
    _std_time = "default"
    _current_time = "default"
    _entire_time_var = None

    _year = 0
    _month = 0
    _day = 0
    _hour = 0
    _minute = 0
    _second = 0

    def __init__(self, parent, format="%Y년 %m월 %d일 %H시 %M분 %S초", timeVar = None ,width=300, height=50, fit=True):
        self._parent = parent
        self._format = format

        self._entire_time_var = tk.StringVar()
        self._time_var_update()

        self._printlabel = ttk.Label(self._parent, width=self._width, textvariable = self._entire_time_var)  # 시간 출력을 위한 레이블

        self._printlabel.pack_propagate(fit)
        self._printlabel.grid_propagate(fit)

    def _time_var_update(self):
        self._current_time = datetime.now()          #   Python Format Code(사용한 것만 나타냄, 나머지는 검색할 것)
        self._year = self._current_time.year         # %Y : 년을 길게 숫자로(2021) / %y : 년을 짧게 숫자로(21)
        self._month = self._current_time.month       # %m : 월을 숫자로 표현(04)
        self._day = self._current_time.day           # %d : 날(일)을 숫자로 표현(1~31까지; 29)
        self._hour = self._current_time.hour         # %H : 시간을 24시간 표현방식으로(00~23 ; 23) / %h : 시간을 12시간 표현 방식으로(00~12; 11)
        self._minute = self._current_time.minute     # %M : 분을 표시(0~59; 15)
        self._second = self._current_time.second     # %S : 초를 표시(0~59; 46) / %f : 마이크로초 단위 표시
        self._entire_time_var.set(self._current_time.strftime(self._format))

    def _clocking(self):
        self._time_var_update()
        self._printlabel.after(500, self._clocking) # 일정 시간 뒤에 지정한 함수를 작동하도록 하는
                                                    # after함수를 재귀함으로서 일정 시간마다 반복하는 함수로 사용

    def create(self):
        self._clocking()
        self._printlabel.pack(expand=True)


class temp_digitalclock: # 임시 날씨 판
    _parent = None
    _packagebase = None #(painedwindow) 시간 설정부 , 시간 출력부 구성 예정
    _controlpanel = None #(painedwindow) 시간 설정부; 레이블-콤보박스-레이블-콤보박스...
    _controlbtn = None #(button) 시간 설정 확정
    
    _year = ['2021']
    _str_year = None
    _month = ['08']
    _str_month = None
    _day = [f'{d}' for d in range(1, 32, 1)]
    _str_day = None
    _hour = [f'{h}' for h in range(0, 24, 1)]
    _str_hour = None
    _minute = [f'{m}' for m in range(0, 60, 1)]
    _str_minute = None
    _second = [f'{s}' for s in range(0, 60, 1)]
    _str_second = None

    _width=0
    _height=0 # painedwindow 크기
    def __init__(self, parent, width=300, height=50):
        self._parent = parent
        self._width = width
        self._height= height

        _str_year = tk.StringVar()
        _str_month = tk.StringVar()
        _str_day = tk.StringVar()
        _str_hour = tk.StringVar()
        _str_minute = tk.StringVar()
        _str_second = tk.StringVar()

        self._setpackagebase()

        # self.timesetlabel = ttk.Label(self._parent)
        # self.timeprintlabel = ttk.Label(self._parent)
        #
        # self.timesetlabel.pack(expand=True)
        # self.timeprintlabel.pack(expand=True)
        #
        # self.comment_label = ttk.Label(self.timesetlabel, text=comment)


    def _setpackagebase(self):
        self.teststyle = ttk.Style()
        self.teststyle.configure('test.TLabel', background='green')

        self._packagebase = ttk.Label(self._parent, width=self._width, style='test.TLabel')

        self._setcontrolpanel(self._packagebase)
        self._controlpanel.pack(expand=True)

    def _setcontrolpanel(self, parent):
        self._controlpanel = ttk.Panedwindow(parent, width=self._width, height=self._height, orient=tk.HORIZONTAL)
        self._year_combobox = ttk.Combobox(self._controlpanel, width=2, values=self._year, textvariable=self._str_year, state='readonly')
        self._year_combobox.current(0)
        self._year_label = ttk.Label(self._controlpanel, text='년')
        self._month_combobox = ttk.Combobox(self._controlpanel, width=1, values=self._month, textvariable=self._str_month, state='readonly')
        self._month_combobox.current(0)
        self._month_label = ttk.Label(self._controlpanel, text='월')
        self._day_combobox = ttk.Combobox(self._controlpanel, width=1, values=self._day, textvariable=self._str_day, state='readonly')
        self._day_combobox.current(0)
        self._day_label = ttk.Label(self._controlpanel, text='일')
        self._hour_combobox = ttk.Combobox(self._controlpanel, width=1, values=self._hour, textvariable=self._str_hour, state='readonly')
        self._hour_combobox.current(0)
        self._hour_label = ttk.Label(self._controlpanel, text='시')
        self._minute_combobox = ttk.Combobox(self._controlpanel, width=1, values=self._minute, textvariable=self._str_minute, state='readonly')
        self._minute_combobox.current(0)
        self._minute_label = ttk.Label(self._controlpanel, text='분')
        self._second_combobox = ttk.Combobox(self._controlpanel, width=1, values=self._second, textvariable=self._str_second, state='readonly')
        self._second_combobox.current(0)
        self._second_label = ttk.Label(self._controlpanel, text='초')
        self._controlbtn = ttk.Button(self._controlpanel, text='변경') # command부분 만들것

        self._controlpanel.add(self._year_combobox, weight=1)
        self._controlpanel.add(self._year_label, weight=1)
        self._controlpanel.add(self._month_combobox, weight=1)
        self._controlpanel.add(self._month_label, weight=1)
        self._controlpanel.add(self._day_combobox, weight=1)
        self._controlpanel.add(self._day_label, weight=1)
        self._controlpanel.add(self._hour_combobox, weight=1)
        self._controlpanel.add(self._hour_label, weight=1)
        self._controlpanel.add(self._minute_combobox, weight=1)
        self._controlpanel.add(self._minute_label, weight=1)
        self._controlpanel.add(self._second_combobox, weight=1)
        self._controlpanel.add(self._second_label, weight=1)
        self._controlpanel.add(self._controlbtn, weight=1)

    def setbackgroundimage(self, width=_width, height=_height, image=None):
        pass

    def create(self):
        self._packagebase.pack(expand=True)


class linearmenu: # 현재 사용하는 메뉴 판
    _parent = None  # 프로젝트 거의 완성될 때 쯤 수정하거나, 프로젝트 끝나고 더 깔끔하게 업데이트 할 것.

    def __init__(self, parent, width=300, height=50):
        self._parent = parent

        self.menus = ttk.Panedwindow(self._parent, width=800, height=70, orient='horizontal')
        self.measureinfoBtn = ttk.Button(self.menus, text='계측정보')
        self.reportBtn = ttk.Button(self.menus, text='보고서')
        self.deviceerrorBtn = ttk.Button(self.menus, text='장애목록')

        self.menus.add(self.measureinfoBtn, weight=1)
        self.menus.add(self.reportBtn, weight=1)
        self.menus.add(self.deviceerrorBtn, weight=1)

    def create(self):
        pass
        self.menus.pack(padx=100)

class tmep_linearmenu:
    _parent = None
    _width = 0
    _hegiht = 0
    _partitions = 0

    def __init__(self, parent, partitions, width=300, height=50):
        self._parent = parent
        self._partitions = partitions
        self._width = width
        self._hegiht = height

        self._linearbase = ttk.Frame(self._parent, width=800, height=70)
        self._linearbase.rowconfigure(index=1, weight=1)
        self._linearbase.columnconfigure(index=self._partitions, weight=1)

        self._linearbase.pack(expand=True)

        self._buttoncreate(self._linearbase, self._partitions)

    def _buttoncreate(self, parent, amount):
        for i in range(0, amount):
            globals()["button{}".format(i)] = ttk.Button(parent, text=f'button{i}')

        #globals()[]
        button1.grid(row=0, column=0, sticky=tk.NS)

class menuboard:    # 동일한 테마를 가지는 버튼 리스트(식당 메뉴판 연상)
    pass

class KVlabel:  # 키-값 형태 레이블(인버터1 : 인버터1 상태 등의 표기에 사용하도록)
    _parent = None
    _type = 'default'
    _key_text = 'default'
    _value_text = 'default'
    def __init__(self, parent, type, key_text, value_text='default'):
        self._parent = parent
        self._type = type
        self._key_text = key_text
        self._value_text=value_text
        self.KVlabel = ttk.Label(self._parent, anchor=tk.W)

        if(self._type == 'editable'):
            self._key_label = ttk.Label(self.KVlabel, text=self._key_text)
            self._value_label = ttk.Entry(self.KVlabel)
            if(self._value_text != 'default'):
                self._value_label.configure(text=self._value_text)

            self.KVlabel.pack(expand=True)
            self._key_label.grid(row=0, column=0)
            self._value_entry.grid(row=0, column=1)
        elif(self._type == 'readonly'):
            self._key_label = ttk.Label(self.KVlabel, text=self._key_text)
            self._value_label = ttk.Label(self.KVlabel)
            if (self._value_text != 'default'):
                self._value_label.configure(text=self._value_text)

            self.KVlabel.pack(expand=True)
            self._key_label.grid(row=0, column=0)
            self._value_label.grid(row=0, column=1)

    def create(self):
        self.KVlabel.pack(expand=True)
        self._key_label.grid(row=0, column=0)
        self._value_label.grid(row=0, column=1)