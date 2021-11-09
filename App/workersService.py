import pyautogui
import config as c
import time
import datetime

class worker:

    def findWorkers() -> bool:
            
            print("START Worker Select Process => ") 
            count = 0
            time.sleep(1)
            
            while pyautogui.locateAllOnScreen(c.worker_button,confidence=.7) is None and pyautogui.locateOnScreen(c.worker_heroes_button,confidence=.7) is not None and count < 10:
            
                if pyautogui.leftClick(c.worker_stamina_bar,confidence=.7) is False :
                    count += 1
                    pyautogui.scroll(-5)
                    time.sleep(1)
            
                    if pyautogui.locateAllOnScreen(c.worker_button,confidence=.7) is not None:
                        break
            
                time.sleep(1)                    
            
            print("click " + str(count) + " in image : " + c.worker_heroes_button)
            count = 0
            while count < 2 :
                
                count += 1
                lastLocation = 0
                location = pyautogui.locateAllOnScreen(c.worker_button, confidence=.7)
                
                for l in location:
                    
                    if(pyautogui.locateAllOnScreen(c.worker_button,confidence=.7) is None ):
                        break
                    
                    if lastLocation <= 0 or lastLocation < l.top  :
                        lastLocation = l.top + 25
                        print("location selected ", l) 
                        time.sleep(0.5)
                        pyautogui.leftClick(l)
                        time.sleep(0.5)
                        pyautogui.leftClick(l)
                        time.sleep(0.5)
                lastLocation = 0
                
                for i in range(0,9):
                    pyautogui.leftClick()
                                
                    pyautogui.scroll(-15)
                    pyautogui.scroll(-15)

                    time.sleep(0.5)
            count = 0

            print("End Worker Select Process") 
            
            while pyautogui.locateOnScreen(c.start_farm_treasure_image, confidence=.7) is None and count < 10:
                pyautogui.leftClick(pyautogui.locateOnScreen(c.general_close_button, confidence=.7))
                print("Trying start the farm") 
                count += 1
                time.sleep(1)
            count = 0
            time.sleep(1)
            
            while pyautogui.locateOnScreen(c.start_farm_treasure_image, confidence=.7) is not None and count < 10:
                pyautogui.leftClick(pyautogui.locateOnScreen(c.start_farm_treasure_image, confidence=.7))
                count += 1
                time.sleep(1)
            count = 0

            time.sleep(1)

            print("Farm Start! ")
            time.sleep(1)

            pyautogui.screenshot(c.imagePath + str(datetime.date(2021,11,9)) + "_log.png")
            
            return True
   # findWorkers() # < teste