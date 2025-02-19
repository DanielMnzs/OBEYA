import pyautogui
import pandas as pd
import time
import PIL
from pyscreeze import ImageNotFoundException


pyautogui.hotkey("win")
time.sleep(2)
pyautogui.write("OPERA")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.leftClick(276, 48)
time.sleep(2)
pyautogui.write("SCI")
time.sleep(5)
pyautogui.press("down")
time.sleep(2)
pyautogui.press("enter")
time.sleep(3)
pyautogui.leftClick(164, 181)
time.sleep(2)
pyautogui.write("ILPNS PENDENTES")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.leftClick(437, 292)
time.sleep(2)
pyautogui.leftClick(126, 372)
time.sleep(1)
pyautogui.leftClick(111, 709)
time.sleep(4)
pyautogui.leftClick(464, 701)
procurar = "NÃO ENCONTRADO"
imagem = r"//depo0903/gpa$/PAC/Daniel Menezes/Python/OBEYA/PLAY.png"
x = 100
finish = r"//depo0903/gpa$/PAC\Daniel Menezes/Python/OBEYA/FINISH.png"


while True:
    try: 
        localizacao = pyautogui.locateCenterOnScreen(imagem,confidence=0.583)
        if localizacao:
            pyautogui.click(localizacao)
            time.sleep(1)
            pyautogui.leftClick(195, 245)
            time.sleep(0.5)
            pyautogui.hotkey("alt", "tab")
            break
            
        else:
            print("IMAGEM NÃO ENCONTRADA...")
            time.sleep(1)
    except pyautogui.ImageNotFoundException:
        print("IMAGEM NÃO FUNCIONAL...")
        time.sleep(1)

#PROCURAR
pyautogui.leftClick(66, 193)
time.sleep(1)
pyautogui.leftClick(459, 193)
time.sleep(1)
pyautogui.write("Gestão de Corte")
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)
pyautogui.leftClick(257, 342)
time.sleep(2)
pyautogui.leftClick(124, 376)
time.sleep(1)
pyautogui.leftClick(124, 713)
time.sleep(2)
pyautogui.leftClick(514, 183)
time.sleep(1)
pyautogui.hotkey("backspace")
time.sleep(1)
pyautogui.write("1")
pyautogui.leftClick(454, 702)

while True:
    try:
        localizacao = pyautogui.locateCenterOnScreen(imagem,confidence=0.583)
        if localizacao:
            print("IMAGEM ENCONTRADA")
            pyautogui.leftClick(localizacao)
            time.sleep(0.5)
            pyautogui.leftClick(179, 237)
            time.sleep(0.5)
            pyautogui.hotkey("alt", "tab")
            break
    except:
        print("IMAGEM NÃO ENCONTRADA")
        time.sleep(0.5)        

time.sleep(1)
pyautogui.leftClick(73, 193)
time.sleep(1)
pyautogui.hotkey("ctrl", "a")
time.sleep(1)
pyautogui.write("tracking de agendamentos")
time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.leftClick(246, 292)
time.sleep(2)
pyautogui.leftClick(126, 373)
time.sleep(1)
pyautogui.leftClick(123, 707)

while True:
    try:
        pyautogui.locateCenterOnScreen(finish)
        if finish:
            print("IMAGEM ENCONTRADA")
            pyautogui.leftClick(846, 178)
            time.sleep(1)
            pyautogui.hotkey("backspace")
            time.sleep(1)
            pyautogui.write("1")
            time.sleep(1)
            pyautogui.click(finish)
            time.sleep(1)
            break
    except:
        print("IMAGEM NÃO ENCONTRADA")
        time.sleep(1)

while True:
    try:
        localizacao = pyautogui.locateCenterOnScreen(imagem, confidence=0.545)
        if localizacao:
            print("IMAGEM ENCONTRADA")
            pyautogui.doubleClick(846, 180)
            time.sleep(0.5)
            pyautogui.write("1")
            time.sleep(0.5)
            pyautogui.click(imagem)
            time.sleep(1)
            pyautogui.leftClick(187, 238)
            time.sleep(1)
            pyautogui.hotkey("alt", "tab")
            break
    except:
        print("IMAGEM NÃO ENCONTRADA!")
        time.sleep(1)


        



        


