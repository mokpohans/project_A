#   Operator.py는 게시자입니다.
import tkinter
from tkinter import ttk

import CsvCreate
from Sys.Activity import MainPage
CsvCreate
main_window = tkinter.Tk()

#     현재 모니터 디스플레이 사이즈(나중에 비율 맞출때 쓰기)
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

default_width = 1280    # 디폴트 너비, 높이
default_height = 960

#     타이틀(Solar Electricity Monitoring System)
main_window.title("S.E.M.S")
#     디폴트 사이즈 설정
main_window.geometry(f"{default_width}x{default_height}")


main_page = MainPage.Mainpage(main_window)
main_page.operate()

def on_closing():
    global main_window
    main_window.destroy()

main_window.protocol("WM_DELETE_WINDOW", on_closing)

main_window.mainloop()