import tkinter as tk
from tkinter import ttk
from datetime import datetime

class windowSizeHelper: # 별 의미 X
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

class timeprinter: # 임시 시간 출력기  예정 -> 시간 정보들을 년,월,일,시,분,초 단위로 얻어오는 함수 작성
    _parent = None                  #    -> 문자열을 해석해서 포맷에 맞춰 시간정보 얻어오는 방법도 찾아볼 것
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

    def __init__(self, parent, format="%Y/%m/%d %H:%M", width=300, height=50, fit=True):
        self._parent = parent
        self._format = format

        self._entire_time_var = tk.StringVar()
        self._time_var_update()

        self._printlabel = ttk.Label(self._parent, width=self._width, textvariable=self._entire_time_var)  # 시간 출력을 위한 레이블

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

class temp_Dclock: # 완전히 시간 표현 부분으로 사용할 예정; 예정 -> 엔트리에 값 넣고 변경 시 timeprinter의 내용이 변화하는 함수 예정
    _parent = None
    _baseFrame = None
    _edit_timepanel = None
    _edit_confirmbtn = None
    _print_timepanel = None

    _time_text = ''
    _var_time_text = None

    _year = 0
    _str_year = None
    _month = 0
    _str_month = None
    _day = 0
    _str_day = None
    _hour = 0
    _str_hour = None
    _minute = 0
    _str_minute = None
    _second = 0
    _str_second = None

    _width = 0
    _height = 0

    def __init__(self, parent, width=500, height=100):
        self._parent=parent
        self._width = width
        self._height = height
        self._var_time_text = tk.StringVar()

        self._baseFrame = ttk.Frame(self._parent, width=int(self._width/2), height=self._height)
        self._baseFrame.grid_propagate(False)
        self._baseFrame.pack_propagate(False)
        self._baseFrame.rowconfigure(index=0, weight=1)
        self._baseFrame.columnconfigure(index=0, weight=1)
        self._baseFrame.columnconfigure(index=1, weight=1)

        self._editpanel_create(self._baseFrame, textvariable=self._var_time_text)
        self._printpanel_create(self._baseFrame)

    def _editpanel_create(self, parent, textvariable, btntext=None):
        self._edit_timepanel = ttk.Label(parent, anchor='w', background="red")
        self._edit_timepanel.rowconfigure(index=0, weight=1)
        self._edit_timepanel.columnconfigure(index=0, weight=1)
        self._edit_timepanel.columnconfigure(index=1, weight=1)
        self._edit_timepanel.pack_propagate(False)
        self._edit_timepanel.grid_propagate(False)
        self._edit_timepanel.grid(row=0, column=0, sticky=tk.EW)

        self._edit_entry = ttk.Entry(self._edit_timepanel, textvariable=textvariable)
        if(btntext==None):
            self._edit_confirmbtn = ttk.Button(self._edit_timepanel, text='변경')
        elif(btntext!=None):
            self._edit_confirmbtn = ttk.Button(self._edit_timepanel, text=btntext)
        self._edit_entry.grid(row=0, column=0)
        self._edit_confirmbtn.grid(row=0, column=1)

    def _printpanel_create(self, parent):
        self._print_timepanel = ttk.Label(parent, background="yellow")
        self._print_timepanel.grid_propagate(False)
        self._print_timepanel.pack_propagate(False)
        self._print_timepanel.grid(row=0, column=1, sticky=tk.EW)

        self._timprinter = timeprinter(self._print_timepanel, width=int(self._width/2), height=self._height)
        self._timprinter.create()

    def create(self):
        self._baseFrame.pack(expand=True)

class temp_digitalclock: # 임시 날씨 판 -> 폐기 예정
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

class temp_imagechooser: # 발전소 이미지-선택기
    _parent = None
    _baseFrame = None
    _image = None
    _indications=[]
    _chooser = None

    _width = 0
    _height = 0

    def __init__(self, parent, image=None, indications=[], width=500, height=500):
        self._parent = parent
        self._image = image
        self._indications = indications
        self._width = width
        self._height = height

        self._baseFrame = ttk.Frame(self._parent, width=self._width, height=self._height)

class linearmenu: # 현재 사용중인 메뉴판; 예정 -> 각 버튼을 누르면 toplevel이 뜨고 해당 액티비티클래스가 뜨도록 할 함수 작성 예정
    _parent = None
    _width = 0
    _hegiht = 0
    _partitions = 0
    _texts = []

    def __init__(self, parent, partitions, texts=[], width=300, height=50):
        self._parent = parent
        self._partitions = partitions
        self._width = width
        self._hegiht = height
        self._texts = texts

        self._linearbase = ttk.Frame(self._parent, width=800, height=70)
        self._linearbase.pack_propagate(False)
        self._linearbase.grid_propagate(False)

        self._buttoncreate(self._linearbase, self._partitions, texts=self._texts)

    def _buttoncreate(self, parent, amount, texts=[]):
        for i in range(0, amount):
            self._linearbase.rowconfigure(index=0, weight=1)
            self._linearbase.columnconfigure(index=i, weight=1)
            if not texts: #텍스트s에 값이 없을 때
                locals()[f'button{i}'] = ttk.Button(parent, text=f'button{i}').grid(row=0, column=i, sticky=tk.NSEW)
            elif texts: # 텍스트s에 값이 있을 때
                if(str(type(texts[i])) == "<class 'str'>"):
                    locals()[f'button{i}'] = ttk.Button(parent, text=texts[i]).grid(row=0, column=i, sticky=tk.NSEW)
                elif():
                    print("error occured, please put 'str' type in texts by a list")

    def create(self):
        self._linearbase.pack(expand=True)

class menuboard:    # 동일한 테마를 가지는 버튼 리스트(식당 메뉴판 연상) -> 보류
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