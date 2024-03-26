import pyautogui
import time
import subprocess
import re
from datetime import datetime

# Specify the full path to the Chrome executable
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Open Google Chrome
subprocess.Popen([chrome_path])

# Give some time for Chrome to open
time.sleep(4)

# Simulate pressing Alt+D to focus on the address bar
pyautogui.hotkey("alt", "d")

# Type the URL
pyautogui.typewrite("192.168.0.1")

# Press Enter
pyautogui.press("enter")

# Give some time for the page to load
time.sleep(4)
# Type "admin"
pyautogui.typewrite("admin")

# Press Enter
pyautogui.press("enter")

time.sleep(3)

pyautogui.hotkey("Esc")

# Simulate pressing "System Tool" in the menu➖➖➖➖➖➖➖➖➖➖➖➖
for i in range(0, 18):
    pyautogui.press("tab")
time.sleep(5)

pyautogui.press("enter")

# Simulate pressing "System Log"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
for i in range(0, 9):
    pyautogui.press("tab")

pyautogui.press("enter")

for i in range(0, 7):
    pyautogui.press("tab")
time.sleep(3)
# Simulate pressing To save "System Log" files
pyautogui.press("enter")
time.sleep(3)
pyautogui.typewrite("Router_Logfile.txt")  # log File Name
time.sleep(3)
pyautogui.hotkey("alt", "d")
pyautogui.typewrite("E:\Codeing\Python Language\Projects\Project_08_TP-Router_LogFiles")  # log File Path
pyautogui.press("enter")
pyautogui.hotkey("alt", "s")



# Simulate pressing "Log Out"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
time.sleep(5)
pyautogui.hotkey("Esc")
for i in range(0, 39):
    pyautogui.press("tab")

pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("enter")

# Simulate pressing "Closeing Chrome"
pyautogui.hotkey("ctrl", "w")


print("Successfully Router Logfile Download")


#🔴 Enter Youer A Specific Download Path
file_path = r"E:\Codeing\Python Language\Projects\Project_08_TP-Router_LogFiles\Router_Logfile.txt"



target_mac = "EE:16:69:E1:50:24"  #🔴 Enter Youer Target PC MAC Address

# Read the log file
with open(file_path, "r") as file:
    log_lines = file.readlines()

# Regular expression pattern to match lines with the target MAC address
pattern = rf"(\d{{4}}-\d{{2}}-\d{{2}}\s+\d{{2}}:\d{{2}}:\d{{2}}).*Recv REQUEST from {re.escape(target_mac)}\s+"

# Find and print lines matching the pattern
print("The List Of Date,Times when the client was Connected to the Router")
for line in log_lines:
    match = re.search(pattern, line)
    if match:
        date_time_str = match.group(1)
        date_time_obj = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        formatted_date_time = date_time_obj.strftime("%Y-%m-%d %I:%M:%S %p")
        print("Date and Time:", formatted_date_time)




