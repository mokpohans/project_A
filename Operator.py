#   Operator.py는 게시자입니다.
import tkinter
from tkinter import ttk
from Sys.Activity import MainPage

main_window = tkinter.Tk()

#     현재 모니터 디스플레이 사이즈(나중에 비율 맞출때 쓰기)
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

print(screen_width)
print(screen_height)
print(main_window.winfo_width())
print(main_window.winfo_height())

default_width = 1280    # 디폴트 너비, 높이
default_height = 960

#     타이틀(Solar Electricity Monitoring System)
main_window.title("S.E.M.S")
#     디폴트 사이즈 설정
main_window.geometry(f"{default_width}x{default_height}")


main_page = MainPage.Mainpage(main_window)
main_page.operate()

main_window.mainloop()