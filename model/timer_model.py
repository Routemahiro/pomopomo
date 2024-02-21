# タイマーの状態（作業中、休憩中）と設定情報（作業時間、休憩時間）を管理します。
import time

class TimerModel:
    def __init__(self):
        self._remaining_time = 0  # 残り時間（秒）
        self._is_working = True  # 作業セッション中か休憩セッション中か
        self._is_running = False  # タイマーが動作中かどうか

    def start_timer(self, duration):
        self._remaining_time = duration
        self._is_running = True

    def pause_timer(self):
        self._is_running = False

    def resume_timer(self):
        self._is_running = True

    def reset_timer(self):
        self._remaining_time = 0
        self._is_running = False

    def update_time(self):
        if self._is_running and self._remaining_time > 0:
            self._remaining_time -= 1
        elif self._remaining_time <= 0:
            self._is_running = False

    def toggle_session(self):
        self._is_working = not self._is_working

    @property
    def remaining_time(self):
        return self._remaining_time

    @property
    def is_working(self):
        return self._is_working

    @property
    def is_running(self):
        return self._is_running
