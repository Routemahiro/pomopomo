# ユーザー設定の保存と読み込みを担当します。設定変更に対応するためのインターフェースもここに含まれます。
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\program\pomodoro\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def close_settings_window(parent_window, settings_window):
    settings_window.destroy()  # 設定ウィンドウを破棄
    parent_window.deiconify()  # 親ウィンドウを再表示

window = Tk()

window.geometry("500x300")
window.configure(bg = "#F2F1DC")


canvas = Canvas(
    window,
    bg = "#F2F1DC",
    height = 300,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    161.0,
    23.0,
    anchor="nw",
    text="作業時間",
    fill="#222222",
    font=("x12y12pxMaruMinya", 20 * -1)
)

canvas.create_rectangle(
    161.0,
    62.0,
    480.0,
    65.0,
    fill="#BF3939",
    outline="")

canvas.create_text(
    161.0,
    85.0,
    anchor="nw",
    text="休憩時間（短）",
    fill="#222222",
    font=("x12y12pxMaruMinya", 20 * -1)
)

canvas.create_rectangle(
    161.0,
    124.0,
    463.0,
    127.0,
    fill="#4E6BED",
    outline="")

canvas.create_text(
    161.0,
    147.0,
    anchor="nw",
    text="休憩時間（長）",
    fill="#222222",
    font=("x12y12pxMaruMinya", 20 * -1)
)

canvas.create_rectangle(
    161.0,
    186.0,
    480.0,
    189.0,
    fill="#4E6BED",
    outline="")

image_character = PhotoImage(
    file=relative_to_assets("character.png"))
character = canvas.create_image(
    77.0,
    147.0,
    image=image_character
)

button_change = PhotoImage(
    file=relative_to_assets("change_button_to_main_window.png"))
change_button = Button(
    image=button_change,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("change_button_to_main_window clicked"),
    relief="flat"
)
change_button.place(
    x=340.0,
    y=215.0,
    width=140.0,
    height=57.0
)

button_no_change = PhotoImage(
    file=relative_to_assets("no_change_to_main_window.png"))
no_change_to_main_window = Button(
    image=button_no_change,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("no_change_to_main_window clicked"),
    relief="flat"
)
no_change_to_main_window.place(
    x=166.0,
    y=221.0,
    width=108.07017517089844,
    height=44.0
)

canvas.create_rectangle(
    #　ここはプルダウン形式で作業の分数を選択できるようにする場所に、仮置きで図形を置いています（分数は1分～60分まで選択可能とする）
    321.0,
    23.0,
    463.0,
    55.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    #　ここはプルダウン形式で短い休憩の分数を選択できるようにする場所に、仮置きで図形を置いています（分数は1分～60分まで選択可能とする）
    321.0,
    85.0,
    463.0,
    117.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    #　ここはプルダウン形式で長い休憩の分数を選択できるようにする場所に、仮置きで図形を置いています（分数は1分～60分まで選択可能とする）
    321.0,
    150.0,
    463.0,
    182.0,
    fill="#FFFFFF",
    outline="")
window.resizable(False, False)
window.mainloop()
