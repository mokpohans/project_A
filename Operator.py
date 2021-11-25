#### Operator가 메인입니다.
import tkinter
from tkinter import ttk

main_window = tkinter.Tk()
    
    # 현재 모니터 디스플레이 사이즈(나중에 비율 맞출때 쓰기)
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

default_width = 1000    # 디폴트 너비, 높이
default_height = 750

    # 타이틀(Solar Electricity Monitoring System)
main_window.title("S.E.M.S")
main_window.geometry(f"{default_width}x{default_height}")
    # 디폴트 사이즈 설정
main_window.mainloop()