#계측 정보에 대한 GUI 구성
import tkinter as tk
from tkinter import ttk
from Sys.Components import AdditionalWidgets as adwz

class Measureinfo:
    def __init__(self, parent):
        self._parent = parent
        self._parent.grid_propagate(False)
        self._parent.pack_propagate(False)

    def operate(self):
        # self.testbaseframe = ttk.Frame(self._parent)
        # self.testbaseframe.grid_propagate(False)
        # self.testbaseframe.pack_propagate(False)
        # self.testbaseframe.pack(expand=True)
        # self.testbutton = ttk.Button(self.testbaseframe, text='testing in MeasureInfo')
        self.testbutton = ttk.Button(self._parent, text='testing in MeasureInfo')
        self.testbutton.pack(expand=True)

