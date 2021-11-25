#### Operator가 메인입니다.
import tkinter
from tkinter import ttk

main_window = tkinter.Tk()

screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

default_width = 1000
default_height = 750

main_window.title("S.E.M.S")
main_window.geometry(f"{default_width}x{default_height}")

main_window.mainloop()