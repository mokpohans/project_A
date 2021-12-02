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
        self._printlabel.after(400, self._clocking) # 일정 시간 뒤에 지정한 함수를 작동하도록 하는
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

class imagechooser: # 발전소 이미지-선택기
    _parent = None
    _baseFrame = None
    _imagelabel = None
    _chooser = None
    _image_uri = None
    _image = None
    _images_uri = []
    _images = []
    _indications = []

    _width = 0
    _height = 0

    def __init__(self, parent, image=None, images=[], indications=[], anchor=tk.NE, rowparts=3, columnparts=3,width=500, height=500):
        self._parent = parent
        self._image_uri = image
        self._images_uri = images
        self._indications = indications
        self._width = width
        self._height = height

        self._baseFrame = ttk.Frame(self._parent, width=self._width, height=self._height)
        self._baseFrame.rowconfigure(index=0, weight=1)
        self._baseFrame.columnconfigure(index=0, weight=1)
        self._baseFrame.grid_propagate(False)
        self._baseFrame.pack_propagate(False)

        self._makeimage(image=self._image_uri, images=self._images_uri)

        self._createimglabel(self._baseFrame, width=self._width, height=self._height, image=self._image, images=self._images)
        self._createchooser_by_anchor(self._baseFrame, indications=self._indications)

    def _createimglabel(self, parent, width, height, image=None, images=[]):
        self._imagelabel = ttk.Label(parent, width=width)
        self._imagelabel.pack_propagate(False)
        self._imagelabel.grid_propagate(False)
        if(image != None):
            self._imagelabel.configure(image=image)
        if(images):
            self._imagelabel.configure(image=images[0])
        self._imagelabel.grid(row=0, column=0, sticky=tk.NSEW)

    def _createchooser_by_anchor(self, parent, width=20, onceamount=5, indications=[], anchor=tk.NE):
        if(self._imagelabel != None):
            # for i in range(0, rowparts, 1):
            #     self._imagelabel.rowconfigure(index=i, weight=1)
            # for j in range(0, columnparts, 1):
            #     self._imagelabel.columnconfigure(index=j, weight=1)
            self._chooser = ttk.Combobox(parent, width=width, height=onceamount, values=indications, state='readonly')
            self._chooser.current(0)
            self._chooser.pack(anchor=anchor, padx=int(self._width/18), pady=int(self._height/18))

    def _makeimage(self, image=None, images=[]):
        if(image != None):
            self._image = tk.PhotoImage(file=image)
        if(images):
            for i in images:
                self._images.append(tk.PhotoImage(file=images[i]))

    def create(self):
        self._baseFrame.pack(expand=True)

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
    _value_var = None
    _kvframe = None
    _keypart = None
    _valuepart = None
    _width = 0
    _height = 0
    _anchor = 'center'

    def __init__(self, parent, type, key_text, value_text='default', width=500, height=50, anchor='center'):
        self._parent = parent
        self._type = type
        self._key_text = key_text
        self._value_var = tk.StringVar()
        self._value_var.set(value_text)
        self._width = width
        self._height = height
        self._anchor = anchor
        self._kvframe = ttk.Frame(self._parent, width=self._width, height=self._height)

        self._kvframe.grid_propagate(False)
        self._kvframe.pack_propagate(False)
        self._kvframe.rowconfigure(index=0, weight=1)
        self._kvframe.columnconfigure(index=0, weight=1)
        self._kvframe.columnconfigure(index=1, weight=1)

        if(self._type == 'editable'):
            self._keypart = ttk.Label(self._kvframe, text=self._key_text, background='ghostwhite', width=int(self._width/2), anchor=self._anchor)
            self._valuepart = ttk.Entry(self._kvframe, width=int(self._width/2))
            if(self._value_var.get() != 'default'):
                self._valuepart.configure(textvariable=self._value_var)

            self._keypart.grid(row=0, column=0, sticky=tk.NSEW)
            self._valuepart.grid(row=0, column=1, sticky=tk.NSEW)

        elif(self._type == 'readonly'):
            self._keypart = ttk.Label(self._kvframe, text=self._key_text, background='ghostwhite', width=int(self._width/2), anchor=self._anchor)
            self._valuepart = ttk.Label(self._kvframe, background='gray', width=int(self._width/2), anchor='center')
            if (self._value_var.get() != 'default'):
                self._valuepart.configure(textvariable=self._value_var)

            self._keypart.grid(row=0, column=0, sticky=tk.NSEW)
            self._valuepart.grid(row=0, column=1, sticky=tk.NSEW)

    def create(self):
        self._kvframe.pack(expand=True)