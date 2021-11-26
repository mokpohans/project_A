import tkinter
from tkinter import ttk


class tempweather: # 임시 날씨 판
    _parent = None
    def __init__(self,parent, comment):
        self._parent = parent

        self.timesetlabel = ttk.Label(self._parent)
        self.timeprintlabel = ttk.Label(self._parent)

        self.timesetlabel.pack(expand=True)
        self.timeprintlabel.pack(expand=True)

        self.comment_label = ttk.Label(self.timesetlabel, text=comment)
        self.year_combobox = ttk.Combobox(self.timesetlabel,)
        self.year_label = ttk.Label(self.timesetlabel, text='년')
        self.month_combobox = ttk.Combobox(self.timesetlabel, )
        self.month_label = ttk.Label(self.timesetlabel, text='월')
        self.day_combobox = ttk.Combobox(self.timesetlabel, )
        self.day_label = ttk.Label(self.timesetlabel, text='일')
        self.hour_combobox = ttk.Combobox(self.timesetlabel, )
        self.hour_label = ttk.Label(self.timesetlabel, text='시')
        self.minute_combobox = ttk.Combobox(self.timesetlabel, )
        self.minute_label = ttk.Label(self.timesetlabel, text='분')
        self.second_combobox = ttk.Combobox(self.timesetlabel, )
        self.second_label = ttk.Label(self.timesetlabel, text='초')

class linearmenu: # 실험중
    _parent = None

    def __init__(self, parent):
        self._parent = parent

        self.menus = ttk.Panedwindow(self._parent, width=1000, height=100, orient='horizontal')
        self.measureinfoBtn = ttk.Button(self._parent, text='계측정보')
        self.reportBtn = ttk.Button(self._parent, text='보고서')
        self.deviceerrorBtn = ttk.Button(self._parent, text='장애목록')

        self.menus.add(self.measureinfoBtn, weight=1)
        self.menus.add(self.reportBtn, weight=1)
        self.menus.add(self.deviceerrorBtn, weight=1)

    def create(self):
        pass
        self.menus.pack()

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
        self.KVlabel = ttk.Label(self._parent, anchor=tkinter.W)

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