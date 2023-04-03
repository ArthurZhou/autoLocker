import os
import subprocess
import sys
import time

import psutil

process_name = sys.argv[1]

print("Process started!")
print("Target:", process_name)


while True:
    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid = proc.pid
            print("Pid:", pid)
            time.sleep(10)
            print("Locking process...")
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subprocess.call("powershell.exe \"" + os.path.join(os.path.dirname(__file__), "poc.exe") + "\" " + str(pid), startupinfo=si)
            while True:
                if psutil.pid_exists(pid):
                    time.sleep(5)
                else:
                    print("Target exited")
                    break
    print("Pending...")
    time.sleep(5)
