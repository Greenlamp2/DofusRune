import win32gui

import psutil
import win32process

from windowMgr import WindowMgr


class ScreenManager:
    def __init__(self):
        self.windows = []

    def enum_window_callback(self, hwnd, pid):
        tid, current_pid = win32process.GetWindowThreadProcessId(hwnd)
        if pid == current_pid and win32gui.IsWindowVisible(hwnd):
            self.windows.append(hwnd)

    def get_process_by_name(self, name):
        w = win32gui
        p = w.GetWindowText(w.GetForegroundWindow())
        processes = [item for item in psutil.process_iter() if item.name() == name]
        return processes

    def get_pid_by_name(self, name):
        w = win32gui
        p = w.GetWindowText(w.GetForegroundWindow())
        processes = [item for item in psutil.process_iter() if item.name() == name]
        pids = [process.pid for process in processes]
        return pids

    def get_windows_name_by_pid(self, pid):
        win32gui.EnumWindows(self.enum_window_callback, pid)
        res = [win32gui.GetWindowText(item) for item in self.windows]
        return res

    def get_all_windows_name_by_pid_list(self, pid_list):
        result = []
        for pid in pid_list:
            win32gui.EnumWindows(self.enum_window_callback, pid)
            res = [win32gui.GetWindowText(item) for item in self.windows]
            result.append(res)
        return result

    def set_focus_by_window_name(self, name):
        we = WindowMgr()
        we.find_window_wildcard(name)
        we.set_foreground()

    def example(self):
        """
        sm = ScreenManager()
        print(sm.get_process_by_name("Dofus.exe")[0])
        pids = sm.get_pid_by_name("Dofus.exe")
        print(pids[0])
        print(sm.get_windows_name_by_pid(pids[0]))
        sm.set_focus_by_window_name("Greenlamp-Arrow")"""
        pass




