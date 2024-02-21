# 設定画面のUIを定義します。作業時間と休憩時間をユーザーがカスタマイズできるインターフェースが含まれます。
import tkinter as tk
from tkinter import simpledialog

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.settings = settings
        self.title("Settings")
        self.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        self.work_time_label = tk.Label(self, text="Work Duration (minutes):")
        self.work_time_label.pack(pady=(20, 0))

        self.work_time_entry = tk.Entry(self)
        self.work_time_entry.pack(pady=5)
        self.work_time_entry.insert(0, str(self.settings.get_work_duration() // 60))

        self.break_time_label = tk.Label(self, text="Break Duration (minutes):")
        self.break_time_label.pack(pady=(10, 0))

        self.break_time_entry = tk.Entry(self)
        self.break_time_entry.pack(pady=5)
        self.break_time_entry.insert(0, str(self.settings.get_break_duration() // 60))

        self.save_button = tk.Button(self, text="Save", command=self.save_settings)
        self.save_button.pack(pady=(20, 0))

    def save_settings(self):
        work_duration = int(self.work_time_entry.get()) * 60
        break_duration = int(self.break_time_entry.get()) * 60
        self.settings.set_work_duration(work_duration)
        self.settings.set_break_duration(break_duration)
        self.destroy()
