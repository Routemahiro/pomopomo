# アプリケーションのメインウィンドウ（UI）を定義します。タイマーの残り時間、状態表示、設定ボタンなどが含まれます。
from pathlib import Path
from tkinter import Toplevel

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\program\pomodoro\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("500x300")
window.configure(bg = "#F2F1DC")


def open_settings_window():
    window.withdraw()  # メインウィンドウを隠す
    settings_window = Toplevel(window)  # 設定ウィンドウを生成
    settings_window.geometry("500x300")
    # ここでsettings_windowの詳細設定を行う
    # 設定ウィンドウを閉じた時の動作
    settings_window.protocol("WM_DELETE_WINDOW", lambda: window.deiconify())

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
button_start = PhotoImage(
    file=relative_to_assets("start.png"))
start = Button(
    image=button_start,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("start clicked"),
    relief="flat"
)
start.place(
    x=37.0,
    y=185.0,
    width=344.0,
    height=84.93595886230469
)

canvas.create_text(
    51.0,
    32.0,
    anchor="nw",
    text="25:00",
    fill="#222222",
    font=("x12y12pxMaruMinya", 80 * -1)
)

canvas.create_rectangle(
    40.0,
    144.0,
    381.0,
    156.0,
    fill="#BF3939",
    outline="")

button_settings = PhotoImage(
    file=relative_to_assets("settings.png"))
settings = Button(
    image=button_settings,
    borderwidth=0,
    highlightthickness=0,
    command=open_settings_window,  # 設定画面を開く関数を呼び出す
    relief="flat"
)
settings.place(
    x=416.0,
    y=210.0,
    width=60.0,
    height=60.0
)

button_download = PhotoImage(
    file=relative_to_assets("download.png"))
download = Button(
    image=button_download,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("download clicked"),
    relief="flat"
)
download.place(
    x=416.0,
    y=144.0,
    width=60.0,
    height=60.0
)
window.resizable(False, False)
window.mainloop()