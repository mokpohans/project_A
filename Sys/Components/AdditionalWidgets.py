import tkinter as tk
from datetime import datetime as dt
from tkinter import ttk
from PIL import Image

class timeprinter: # 임시 시간 출력기  예정 -> 시간 정보들을 년,월,일,시,분,초 단위로 얻어오는 함수 작성
    _parent = None                  #    -> 문자열을 해석해서 포맷에 맞춰 시간정보 얻어오는 방법도 찾아볼 것
    _printlabel = None
    _width = 0
    _height = 0
    time_format = "default"
    _std_time = "default"
    _current_time = "default"
    _entire_time_var = None

    _timechanged = False
    _rawtimedata = None
    _year = 0
    _month = 0
    _day = 0
    _hour = 0
    _minute = 0
    _second = 0

    def __init__(self, parent, timeformat="%Y-%m-%d %H:%M", width=300, height=50, fit=True):
        self._parent = parent
        self.time_format = timeformat

        self._entire_time_var = tk.StringVar()
        self._time_var_update_present()

        self._printlabel = ttk.Label(self._parent, width=self._width, textvariable=self._entire_time_var)  # 시간 출력을 위한 레이블
        self._printlabel.update()

        self._printlabel.pack_propagate(fit)
        self._printlabel.grid_propagate(fit)

    def _time_var_update_present(self):
        self._current_time = dt.now()          #   Python Format Code(사용한 것만 나타냄, 나머지는 검색할 것)
        self._year = self._current_time.year         # %Y : 년을 길게 숫자로(2021) / %y : 년을 짧게 숫자로(21)
        self._month = self._current_time.month       # %m : 월을 숫자로 표현(04)
        self._day = self._current_time.day           # %d : 날(일)을 숫자로 표현(1~31까지; 29)
        self._hour = self._current_time.hour         # %H : 시간을 24시간 표현방식으로(00~23 ; 23) / %h : 시간을 12시간 표현 방식으로(00~12; 11)
        self._minute = self._current_time.minute     # %M : 분을 표시(0~59; 15)
        self._second = self._current_time.second     # %S : 초를 표시(0~59; 46) / %f : 마이크로초 단위 표시
        self._entire_time_var.set(self._current_time.strftime(self.time_format))

    def _clocking(self):
        # print(f'timechanged signal is : {self._timechanged}')
        if(self._timechanged == False):
            self._time_var_update_present()
            self._printlabel.update()
            self._present_after = self._printlabel.after(500, self._clocking) # 일정 시간 뒤에 지정한 함수를 작동하도록 하는
                                                    # after함수를 재귀함으로서 일정 시간마다 반복하는 함수로 사용
        elif(self._timechanged == True):
            self._time_calculator()
            self._second += 1
            self._printlabel.update()
            self._calc_after = self._printlabel.after(980, self._clocking)

    def _time_calculator(self):
        # print(f'in _time_calculator; self._year : {self._year}, month : {self._month}, day : {self._day}, hour : {self._hour}')
        if(self._second > 59):
            self._second = 0
            self._minute += 1
        if(self._minute > 59):
            self._minute = 0
            self._hour += 1
        if(self._hour > 23):
            self._hour = 0
            self._day += 1
        if((self._year % 4) == 0): # 년도가 4로 나누어 떨어지고
            if(self._month == 2): # 2월 이면
                if(self._day > 29): # 29일까지
                    self._day = 1
                    self._month += 1
        elif(self._month == 2): # 년도가 4로 나누어 떨어지지 않고
            if(self._day > 28): # 2월 이면 28일까지
                self._day = 1
                self._month += 1
        elif(self._day > 31):
            self._day = 1
            self._month += 1
        if(self._month > 12):
            self._month = 1
            self._year += 1

        self._edited_time = dt(self._year, self._month, self._day, self._hour, self._minute, self._second)
        self._entire_time_var.set(self._edited_time.strftime(self.time_format))
        self._printlabel.update()

    # def _calculated_clocking(self):
    #     # print(f'timechanged signal is : {self._timechanged}')
    #     self._time_calculator()
    #     print(f'tempcount is : {self._tempcount}')
    #     if(self._tempcount != 0):
    #         self._second += 1
    #     elif(self._tempcount == 0):
    #         self._tempcount = 1
    #     self._printlabel.update()
    #     self._calc_after = self._printlabel.after(1000, self._calculated_clocking)

    def create(self):
        self._clocking()
        self._printlabel.pack(expand=True)

    def getTimeVar(self):
        return self._entire_time_var

    def setTimeVar(self, changevalue):
        self._entire_time_var.set(changevalue)

    def getTimeElements(self, element='second'):
        if(element=='year'):
            return self._year
        if(element=='month'):
            return self._month
        if(element=='day'):
            return self._day
        if(element=='hour'):
            return self._hour
        if(element=='minute'):
            return self._minute
        if(element=='second'):
            return self._second

    def setTimeElements(self, rawtime=None, year=0, month=0, day=0, hour=0, minute=0, second=0):
        self._rawtimedata = rawtime
        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
        self._minute = minute
        self._second = second
        # print(f'in timeprinter > setTimeElements activated; year : {self._year}, month : {self._month}, day : {self._day}, hour : {self._hour}')

    def setChangedState(self, state=False):
        self._timechanged = state

class temp_Dclock: # 완전히 시간 표현 부분으로 사용할 예정; 예정 -> 엔트리에 값 넣고 변경 시 timeprinter의 내용이 변화하는 함수 예정
    _parent = None
    _baseFrame = None
    _edit_timepanel = None
    _edit_confirmbtn = None
    _print_timepanel = None

    _framebg = None
    _image_uri = None
    _image = None
    _images_uri = []
    _images = []

    _format = "%Y-%m-%d %H:%M"

    _time_text = ''
    _var_time_text = None

    _year = 0
    _month = 0
    _day = 0
    _hour = 0
    _minute = 0
    _second = 0

    _width = 0
    _height = 0

    def __init__(self, parent, width=500, height=100, frameBG=None, images=[], image=None):
        self._parent = parent
        self._width = width
        self._height = height
        self._var_time_text = tk.StringVar()
        self._framebg = frameBG
        self._images_uri = images
        self._image_uri = image

        self._baseFrame = ttk.Frame(self._parent, width=self._width, height=self._height)
        if(self._framebg != None):
            self._baseFrame.configure(style=self._framebg)
        self._baseFrame.grid_propagate(False)
        self._baseFrame.pack_propagate(False)
        self._baseFrame.rowconfigure(index=0, weight=1)
        self._baseFrame.columnconfigure(index=0, weight=1)

        self._makeimage(image=self._image_uri, images=self._images_uri)

        self._background_panel = ttk.Label(self._baseFrame, width=self._width)
        if(self._images):
            self._background_panel.configure(image=self._images[0])
        elif(self._image != None):
            self._background_panel.configure(image=self._image)
        self._background_panel.grid_propagate(False)
        self._background_panel.pack_propagate(False)
        for i in range(0, 3):
            self._background_panel.rowconfigure(index=i, weight=1)
        self._background_panel.columnconfigure(index=0, weight=1)
        self._background_panel.columnconfigure(index=1, weight=1)
        self._background_panel.grid(row=0, column=0, sticky=tk.NSEW)

        self._editpanel_create(self._background_panel, textvariable=self._var_time_text)
        self._printpanel_create(self._background_panel)
        self._format = self._timeprinter.time_format

        self._edit_confirmbtn.configure(command=lambda: self._parseEditedTime(self._var_time_text, self._format))

    def _makeimage(self, image=None, images=[]):
        if(image != None):
            self._image = tk.PhotoImage(file=image)
        if images:
            for i in range(0, len(images)):
                self._images.append(tk.PhotoImage(file=images[i]))

    def _editpanel_create(self, parent, textvariable, btntext=None):          # 사진 하늘 색 : #5cd9ff
        self._edit_timepanel = ttk.Label(parent, anchor='w', background="#5cd9ff") # 민트색 : #cfffe5
        for i in range(0, 3):
            self._edit_timepanel.rowconfigure(index=i, weight=1)
        self._edit_timepanel.columnconfigure(index=0, weight=3)
        self._edit_timepanel.columnconfigure(index=1, weight=1)
        self._edit_timepanel.pack_propagate(False)
        self._edit_timepanel.grid_propagate(False)

        self._edit_timepanel.grid(row=0, column=0, sticky=tk.EW)
        self._edit_entry = ttk.Entry(self._edit_timepanel, textvariable=textvariable)
        if(btntext==None):
            self._edit_confirmbtn = ttk.Button(self._edit_timepanel, text='변경')
        elif(btntext!=None):
            self._edit_confirmbtn = ttk.Button(self._edit_timepanel, text=btntext)
        self._edit_entry.grid(row=0, column=0, sticky=tk.E)
        self._edit_confirmbtn.grid(row=0, column=1, sticky=tk.EW)
        # self._edit_entry.grid(row=0, column=0)
        # self._edit_confirmbtn.grid(row=0, column=1)

    def _printpanel_create(self, parent):                               # 사진 하늘 색 : #5cd9ff
        self._print_timepanel = ttk.Label(parent, background="#5cd9ff") #사진 해 색 : #fffb8e
        self._print_timepanel.grid_propagate(False)                     # 민트색 : #cfffe5
        self._print_timepanel.pack_propagate(False)
        self._print_timepanel.grid(row=0, column=1, sticky=tk.EW)

        self._timeprinter = timeprinter(self._print_timepanel, width=int(self._width/2), height=self._height)
        self._timeprinter.create()

    def _parseEditedTime(self, textvariable, format):
        self._rawtimestr = textvariable.get()
        print(self._rawtimestr)
        self._parseDateTime = dt.strptime(self._rawtimestr, format)
        print(self._parseDateTime)
        self._year = self._parseDateTime.year  # %Y : 년을 길게 숫자로(2021) / %y : 년을 짧게 숫자로(21)
        self._month = self._parseDateTime.month  # %m : 월을 숫자로 표현(04)
        self._day = self._parseDateTime.day  # %d : 날(일)을 숫자로 표현(1~31까지; 29)
        self._hour = self._parseDateTime.hour  # %H : 시간을 24시간 표현방식으로(00~23 ; 23) / %h : 시간을 12시간 표현 방식으로(00~12; 11)
        self._minute = self._parseDateTime.minute  # %M : 분을 표시(0~59; 15)
        self._second = self._parseDateTime.second  # %S : 초를 표시(0~59; 46) / %f : 마이크로초 단위 표시

        # print(f'in parsing : year : {self._year}, month : {self._month}, day : {self._day}')

        self._timeprinter.setChangedState(True)
        self._timeprinter.setTimeElements(rawtime=self._parseDateTime, year=self._year, month=self._month, day=self._day, hour=self._hour,
                                          minute=self._minute, second=self._second)

    def create(self):
        self._baseFrame.pack(expand=True)

    def getTimeInfo(self, expand=''):
        if (expand == 'default')or(expand == ''):
            return str(f"{self._timeprinter.getTimeElements('year')}-" + "{0:0>2}".format(f"{self._timeprinter.getTimeElements('month')}") + "-" + "{0:0>2}".format(f"{self._timeprinter.getTimeElements('day')}")
                       + f" {self._timeprinter.getTimeElements('hour')}:" + "{0:0>2}".format(f"{self._timeprinter.getTimeElements('minute')}"))
        elif(expand == 'sec')or(expand == 'second'):
            self._second = self._timeprinter.getTimeElements(element='second')
            return str(self._timeprinter.getTimeVar().get() + " {0:0>2}".format(f"{self._second}"))



class imagesizehelper:
    _image_uri = None
    _images_uri = []
    _width = 0
    _height = 0
    _tempimg = None
    _resized = None

    def __init__(self, image=None, images=[], width=0, height=0):
        self._image_uri = image
        self._images_uri = images
        self._width = width
        self._height = height

    def doResize(self, width, height):
        self._width = width
        self._hegiht = height

        if(self._image_uri != None):
            self._tempimg = Image.open(self._image_uri)
            self._resized = self._tempimg.resize((int(self._width), int(self._height)))
            self._resized.save(self._image_uri)
        if(self._images_uri):
            for i in range(0, len(self._images_uri)):
                self._tempimg = Image.open(self._images_uri[i])
                self._resized = self._tempimg.resize((int(self._width), int(self._height)))
                self._resized.save(self._images_uri[i])

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

    def __init__(self, parent, image=None, images=[], indications=[], anchor=tk.NE, rowparts=3, columnparts=3, width=500, height=500):
        self._parent = parent
        self._image_uri = image
        self._images_uri = images
        self._indications = indications
        self._width = width
        self._height = height

        self.imgMG = imagesizehelper(image=self._image_uri, images=self._images_uri, width=self._width, height=self._height)

        self._baseFrame = ttk.Frame(self._parent, width=self._width, height=self._height)
        self._baseFrame.rowconfigure(index=0, weight=1)
        self._baseFrame.columnconfigure(index=0, weight=1)
        self._baseFrame.grid_propagate(False)
        self._baseFrame.pack_propagate(False)

        self.imgMG.doResize(width=self._width, height=self._height)
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

    def _createchooser_by_anchor(self, parent, width=30, onceamount=5, indications=[], anchor=tk.NE):
        if(self._imagelabel != None):
            self._chooser = ttk.Combobox(parent, width=width, height=onceamount, values=indications, state='readonly')
            self._chooser.current(0)
            self._chooser.pack(anchor=anchor, padx=int(self._width/18), pady=int(self._height/18))
            self._chooser.bind("<<ComboboxSelected>>", lambda event: self._callbackFunc())

    def _makeimage(self, image=None, images=[]):
        if(image != None):
            self._image = tk.PhotoImage(file=image)
        if(images):
            for i in range(0, len(images)):
                self._images.append(tk.PhotoImage(file=images[i]))

    def create(self):
        self._baseFrame.pack(expand=True)

    def _callbackFunc(self):
        self._imgnumb = self._indications.index(str(self._chooser.get()))
        self._imagelabel.configure(image=self._images[self._imgnumb])
        self._imagelabel.update()

    def getPlantName(self):
        return str(self._chooser.get())

class linearmenu: # 현재 사용중인 메뉴판; 예정 -> 각 버튼을 누르면 toplevel이 뜨고 해당 액티비티클래스가 뜨도록 할 함수 작성 예정
    _parent = None
    _width = 0
    _hegiht = 0
    _partitions = 0
    _texts = []
    _textVars = []
    _command = None
    # 테스트 1) locals() 버튼 변수들을 생성 즉시 리스트로 넣는다. -> 리스트 내용 확인해볼 것 -> 실패 : 전부 None으로만 기록된다.
    _X_btnlist = []
    # 테스트 2) 딕셔너리를 생성해서 텍스트 내용 -> 해당 버튼 담당 구성
    _X_btnDict = {}

    def __init__(self, parent, partitions, texts=[], command=None, width=800, height=70):
        self._parent = parent
        self._partitions = partitions
        self._width = width
        self._hegiht = height
        self._texts = texts
        self._command = command

        self._linearbase = ttk.Frame(self._parent, width=self._width, height=self._hegiht)
        self._linearbase.pack_propagate(False)
        self._linearbase.grid_propagate(False)

        self._buttoncreate(self._linearbase, self._partitions, texts=self._texts, command=self._command)
        # print(f"in linearmenu_lobby locals()button_numbering like this : {locals()}")
        print(f"in linearmenu_lobby globals()button_numbering like this : {globals()['__button0']}")
        # print(f"in linearmenu_lobby, For test list is : {self._X_btnlist}")

    def _buttoncreate(self, parent, amount, texts=[], command=None):
        for i in range(0, amount):
            self._linearbase.rowconfigure(index=0, weight=1)
            self._linearbase.columnconfigure(index=i, weight=1)
            if not texts: #텍스트s에 값이 없을 때
                # locals()[f'button{i}'] = ttk.Button(parent, text=f'button{i}', command=command).grid(row=0, column=i, sticky=tk.NSEW)
                globals()[f'__button{i}'] = ttk.Button(parent, text=f'button{i}', command=command)
                globals()[f'__button{i}'].grid(row=0, column=i, sticky=tk.NSEW)
                # globals()[f'{texts[i]}'] = ttk.Button(parent, text=f'button{i}', command=command).grid(row=0, column=i, sticky=tk.NSEW)
            elif texts: # 텍스트s에 값이 있을 때
                if(str(type(texts[i])) == "<class 'str'>"):
                #원래 적혀 있던 내용 -> grid를 함께 쓴 것이 지금 까지 안된 원인.
                    # locals()[f'button{i}'] = ttk.Button(parent, text=texts[i], command=command).grid(row=0, column=i, sticky=tk.NSEW)
                #버튼 번호별로 생성 -> 번호가 겹치면서 리스트에 들어감, 속성이 겹치는지 확인해 볼 것.
                    # locals()[f'button{i}'] = ttk.Button(parent, text=texts[i], command=command)
                    # locals()[f'button{i}'].grid(row=0, column=i, sticky=tk.NSEW)

                #locals에서 입력한 텍스트(계측정보, 보고서 등)를 변수명으로 활용 -> 사용가능하나 한글이므로 주의할 것.
                    # locals()[f'{texts[i]}'] = ttk.Button(parent, text=texts[i], command=command)
                    # locals()[f'{texts[i]}'].grid(row=0, column=i, sticky=tk.NSEW)

                #globals에서 버튼 번호별로 생성 -> 번호가 겹치면서 list에 쌓인다. 속성이 겹치는지 확인해 볼 것
                    globals()[f'__button{i}'] = ttk.Button(parent, text=texts[i], scommand=command)
                    globals()[f'__button{i}'].grid(row=0, column=i, sticky=tk.NSEW)

                #globas에서 입력한 텍스트(계측정보, 보고서 등)를 변수명으로 활용 -> 요놈은 사용불가 -> grid를 같이 쓴 순간부터 삭제됨
                    # globals()[f'{texts[i]}'] = ttk.Button(parent, text=texts[i], command=command).grid(row=0, column=i, sticky=tk.NSEW)

                #globals에서 입력한 텍스트(계측정보, 보고서 등)를 변수명으로 활용 -> 사용가능하나 한글이므로 주의할 것.
                    # globals()[f'{texts[i]}'] = ttk.Button(parent, text=texts[i], command=command)
                    # globals()[f'{texts[i]}'].grid(row=0, column=i, sticky=tk.NSEW)

                    # print(f"in creating buttons locals()button_numbering like this : {locals()[f'button{i}']}")
                    # print(f"in creating buttons locals()button_numbering like this : {locals()}")
                    # print(f"in creating buttons globals()button_numbering like this : {globals()}")
                    # print(f"in creating buttons globals()button_numbering like this : {globals()[f'{texts[i]}']}")
                    # self._X_btnlist.append(locals()[f'button{i}'])
                    # self._X_btnlist.append(locals()[f'{texts[i]}'])
                    # self._X_btnlist.append(globals()[f'button{i}'])
                elif():
                    print("error occured, please put 'str' type in texts by a list")
        # print(f"in _buttoncreate locals()button_numbering like this : {locals()}")
        # print(f"in _buttoncreate globals()button_numbering like this : {globals()}")
        # print(f"in _buttoncreate, For test list is : {self._X_btnlist}")

    def elementManipulate(self, index=0, command=None, compound=None, cursor=None,
                          image=None, style=None, takefocus=None, text=None, textvariable=None,
                          underline=None, width=None):
        if(index > self._partitions):
            print("Error: Out of Range! Check your index number & partitions number")
        elif(index <= self._partitions):
            globals()[f'__button{index}'].configure(command=command, compound=compound, cursor=cursor,
                                                  image=image, style=style, takefocus=takefocus,
                                                  text=text, textvariable=textvariable,
                                                  underline=underline, width=width)
            globals()[f'__button{index}'].update()

    def create(self):
        self._linearbase.pack(expand=True)

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
    _image_uri = None
    _image = None
    _images_uri = []
    _images = []

    def __init__(self, parent, type, key_text, value_text='default', width=500, height=50, anchor='center', image=None, images=[]):
        self._parent = parent
        self._type = type
        self._key_text = key_text
        self._value_var = tk.StringVar()
        self._value_var.set(value_text)
        self._width = width
        self._height = height
        self._anchor = anchor
        self._image_uri = image
        self._images_uri = images
        self._kvframe = ttk.Frame(self._parent, width=self._width, height=self._height)

        self._kvframe.grid_propagate(False)
        self._kvframe.pack_propagate(False)
        self._kvframe.rowconfigure(index=0, weight=1)
        self._kvframe.columnconfigure(index=0, weight=1)
        self._kvframe.columnconfigure(index=1, weight=1)

        self._makeimage(image=self._image_uri, images=self._images_uri)

        if(self._type == 'editable'):
            self._keypart = ttk.Label(self._kvframe, text=self._key_text, background='#cfffe5', width=int(self._width/2), anchor=self._anchor)
            self._valuepart = ttk.Entry(self._kvframe, width=int(self._width/2))
            if(self._value_var.get() != 'default'):
                self._valuepart.configure(textvariable=self._value_var)

            self._keypart.grid(row=0, column=0, sticky=tk.NSEW)
            self._valuepart.grid(row=0, column=1, sticky=tk.NSEW)

        elif(self._type == 'readonly'):
            self._keypart = ttk.Label(self._kvframe, text=self._key_text, background='#cfffe5', width=int(self._width/2), anchor=self._anchor)
            self._valuepart = ttk.Label(self._kvframe, background='#cfffe5', width=int(self._width/2), anchor='center')
            if (self._value_var.get() != 'default'):
                self._valuepart.configure(textvariable=self._value_var)

            self._keypart.grid(row=0, column=0, sticky=tk.NSEW)
            self._valuepart.grid(row=0, column=1, sticky=tk.NSEW)

        elif(self._type == 'showcase'):
            self._keypart = ttk.Label(self._kvframe, text=self._key_text, background='#cfffe5', width=int(self._width/2), anchor=self._anchor)
            self._valuepart = ttk.Label(self._kvframe, background='#cfffe5', width=int(self._width/2), anchor='center')
            self._keypart.grid_propagate(False)
            self._keypart.pack_propagate(False)
            self._valuepart.grid_propagate(False)
            self._valuepart.pack_propagate(False)
            if(self._image != None):
                self._valuepart_imglabel = ttk.Label(self._valuepart, background='#cfffe5', image=self._image, width=int(self._width/2), anchor='center')
                self._valuepart_imglabel.pack_propagate(False)
                self._valuepart_imglabel.update()
                self._valuepart_imglabel.pack(expand=True, fill='both')
                # self._valuepart.pack(expand=True)
                # self._valuepart.configure(image=self._image, anchor=tk.W)
                # self._valuepart.update()
            elif(self._images):
                self._valuepart_imglabel = ttk.Label(self._valuepart, background='#cfffe5', image=self._images[0],
                                                     width=int(self._width / 2), anchor='center')
                self._valuepart_imglabel.pack_propagate(False)
                self._valuepart_imglabel.update()
                self._valuepart_imglabel.pack(expand=True, fill='both')

            self._keypart.grid(row=0, column=0, sticky=tk.NSEW)
            self._valuepart.grid(row=0, column=1, sticky=tk.NSEW)

    def _makeimage(self, image=None, images=[]):
        if(image != None):
            self._image = tk.PhotoImage(file=image)
        if(images):
            for i in range(len(images)):
                self._images.append(tk.PhotoImage(file=images[i]))

    def create(self, padx=0, pady=0, ipadx=0, ipady=0):
        self._kvframe.pack(expand=True, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

    def showcase_configure(self, key_config='', image=None, images=[], index=0):
        if(key_config != ''):
            self._keypart.configure(text=key_config)
        if(image != None):
            self._image_uri = image
            self._makeimage(image=self._image_uri, images=self._images_uri)
            self._valuepart_imglabel.configure(image=self._image)
        if(images):
            self._images_uri = images
            self._makeimage(image=self._image_uri, images=self._images_uri)
            self._valuepart_imglabel.configure(image=self._images[index])
        self._valuepart_imglabel.configure(image=self._images[index])