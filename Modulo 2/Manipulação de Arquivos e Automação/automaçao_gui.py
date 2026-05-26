import pyautogui as at

def apertar_tab(qtd):
    for i in range(qtd):
        at.press("tab")
        at.sleep(0.01)

at.hotkey("win", "r")
at.write("chrome", 0.2)
at.press("enter")
at.write("www.deadshot.io", 0.1)
at.press("enter")
at.sleep(0.5)
